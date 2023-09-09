from dotenv import load_dotenv
import os
import base64
from requests import post, get
import json
import re

#region Auth
load_dotenv()

client_id = os.getenv("CLIENT_ID")
client_secret = os.getenv("CLIENT_SECRET")

def get_token():
    auth_string = client_id + ":" + client_secret
    auth_bytes = auth_string.encode("utf-8")
    auth_base64 = str(base64.b64encode(auth_bytes), "utf-8")

    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {"grant_type": "client_credentials"}
    result = post(url, headers=headers, data=data)
    json_result = json.loads(result.content)
    token = json_result["access_token"]
    return token

def get_auth_header(token):
    return {"Authorization": "Bearer " + token}
#endregion

#region Artist Search
def search_for_artist(token, artist_name):
    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)
    query = f"?q={artist_name}&type=artist&limit=1"

    query_url = url + query
    result = get(query_url, headers=header)
    json_result = json.loads(result.content)["artists"]["items"]
    if len(json_result) == 0:
        print("No artist with this name exists...")
        return None
    return json_result[0]
    
def get_songs_by_artist(token, artist_id):
    url = f"https://api.spotify.com/v1/artists/{artist_id}/top-tracks?market=US"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)["tracks"]
    return json_result
#endregion

#region Playlist Search
def search_for_playlists(token, searchTerm, limit, offset):
    url = "https://api.spotify.com/v1/search"
    header = get_auth_header(token)
    query = f"?q={searchTerm}&type=playlist&limit={limit}&offset={offset}"

    query_url = url + query
    result = get(query_url, headers=header)
    json_result = json.loads(result.content)["playlists"]['items']
    if len(json_result) == 0:
        print("No playlists found...")
        return {}
    return json_result

def get_playlist_information(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}"
    header = get_auth_header(token)
    result = get(url, headers=header)
    json_result = json.loads(result.content)
    return json_result

def get_email_in_playlist_description(playlist_information):
    description = playlist_information['description']

    regex = re.compile(r"([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\"([]!#-[^-~ \t]|(\\[\t -~]))+\")@([-!#-'*+/-9=?A-Z^-~]+(\.[-!#-'*+/-9=?A-Z^-~]+)*|\[[\t -Z^-~]*])")

    match = re.findall(regex, description)

    if len(match) <= 0:
        return None
    else:
        description_segments = description.split(" ")
        for idx, segment in enumerate(description_segments):
            if segment.__contains__("@") and len(segment) > 2:
                return segment
    return match[0][0] + "@" + match[0][4]

def get_tracks_in_playlist(token, playlist_id):
    url = f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks"
    header = get_auth_header(token)

    result = get(url, headers=header)
    json_result = json.loads(result.content)['items']

    tracks = len(json_result)
    if tracks == 0:
        print("No tracks in playlist...")
    return tracks

#endregion