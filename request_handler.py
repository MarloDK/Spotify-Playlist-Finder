
from dotenv import load_dotenv
#from requests import post, get
from flask import Flask, request, Response, jsonify
from flask_cors import CORS, cross_origin
import json
import re
import spotify_api_handler as spotify


app = Flask(__name__)
cors = CORS(app, resources={r"/searchPlaylists": {"origins": "*"}})
app.config['CORS_HEADERS'] = "Content-Type"
@cross_origin(origin='*',headers=['Content-Type','Authorization'])

@app.route('/searchPlaylists', methods=["GET"])
def search_playlists():
    token = spotify.get_token()
    print("Token: " + token)

    search_term = request.args.get('searchTerm')
    print("Searching for playlists with query: \'" + search_term + "\'")
    

    
    valid_playlists = []

    for i in range(20):
        print(f"Finding playlists... ({i*50+50}/{50*20})")

        playlists = spotify.search_for_playlists(token, search_term, 50, 50*i)

        for idx,playlist in enumerate(playlists):
            playlist_info = spotify.get_playlist_information(token, playlist['id'])
            
            playlist_followers = playlist_info['followers']['total']
            playlist_contact = spotify.get_email_in_playlist_description(playlist_info)

            if playlist_contact != None and playlist_followers > 1000:
                playlist_name = re.sub(r'[^\x00-\x7F]', '', playlist_info['name'])
                playlist_owner = playlist_info['owner']['display_name']
                playlist_tracks = spotify.get_tracks_in_playlist(token, playlist['id'])
                #print(f"{idx+1}. {playlist_name} ({playlist_owner})")
                #print("Followers:" + str(playlist_followers))
                #print("Email: " + str(playlist_contact))

                valid_playlists.append({
                    "name": playlist_name,
                    "owner": playlist_owner,
                    "link": playlist['external_urls']['spotify'],
                    "tracks": playlist_tracks,
                    "followers": playlist_followers,
                    "contact": str(playlist_contact)
                })

    response = jsonify({"playlists": valid_playlists})
    print(valid_playlists)
    response.headers.add('Access-Control-Allow-Origin', '*')
    

    return response

if __name__ == "__main__":
    app.run(port=9000)