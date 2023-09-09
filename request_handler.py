
from dotenv import load_dotenv
#from requests import post, get
from flask import Flask, request
import json
import re
import spotify_api_handler as spotify


app = Flask(__name__)

@app.route('/searchPlaylists', methods= ["POST"])
def search_playlists():
    request_data = request.get_json()
    print(request_data)
    token = spotify.get_token()
    print("Token: " + token)

    search_term = request_data['searchTerm']
    print("Searching for playlists with query: \'" + search_term + "\'")
    playlists = spotify.search_for_playlists(token, search_term, 50)

    
    valid_playlists = {}
    for idx,playlist in enumerate(playlists):
        playlist_info = spotify.get_playlist_information(token, playlist['id'])
        
        playlist_name = re.sub(r'[^\x00-\x7F]', '', playlist_info['name'])
        playlist_owner = playlist_info['owner']['display_name']
        playlist_followers = playlist_info['followers']['total']
        playlist_contact = spotify.get_email_in_playlist_description(playlist_info)

        if playlist_contact != None and playlist_followers > 1000:
            print(f"{idx+1}. {playlist_name} ({playlist_owner})")
            print("Followers:" + str(playlist_followers))
            print("Email: " + str(playlist_contact))

            valid_playlists[playlist_name] = {
                "owner": playlist_owner,
                "followers": playlist_followers,
                "contact": str(playlist_contact)
            }

            print('\n')

    valid_playlists_json = json.dumps(valid_playlists, indent=4)

    return valid_playlists_json

if __name__ == "__main__":
    app.run(port=9000)