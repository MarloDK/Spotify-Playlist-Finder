const axios = require('axios');
const { header } = require('express/lib/request');
require('dotenv').config();

// Load .env data
const clientId = process.env.CLIENT_ID;
const clientSecret = process.env.CLIENT_SECRET;

function GetToken() {
    var authString = `${clientId}:${clientSecret}`;
    var auth_base64 = btoa(authString);


    var url = "https://accounts.spotify.com/api/token";
    var headers = {
        "Authorization": "Basic " + auth_base64,
        "Content-Type": "application/x-www-form-urlencoded"
    };
    var data = {"grant_type": "client_credentials"};

    var result = axios.post(url, {headers: headers});
    var resultsJSON = JSON.parse(result.content);

    /*
        PYTHON EXAMPLE
    */

    /*auth_string = client_id + ":" + client_secret
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
    return token*/
}

function GetAuthHeader(token) {
    return {"Authorization": "Bearer " + token}
}

function SearchForPlaylists(token, searchTerm, limit) {

}

function GetPlaylistInformation(token, playlistId) {

}

function GetEmailInPlaylistDescription(playlistInformation) {

}