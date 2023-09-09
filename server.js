const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios')

const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded( { extended: false } ));
app.use('/public', express.static(__dirname + '/public'));

class playlist {
    name = "";
    owner = "";
    email = "ass@gmail.com";

    link = "https://open.spotify.com/playlist/4PH8zI5tvZvw8YsrTs9jfM?si=7f833facff47433d";

    songs = 0;
    followers = 0;

    constructor(name, owner, songs, followers) {
        this.name = name;
        this.owner = owner;
        this.songs = songs;
        this.followers = followers;
    }
}


app.get('/', (req, res) => {
    var playlistArray = [];

    var newPlaylist = new playlist("Test Playlist", "Test User", 9999, 999999);
    var newPlaylist2 = new playlist("Test Playlist2", "Test User2", 4214, 442872);
    playlistArray.push(newPlaylist, newPlaylist2);


    res.render('pages/home', { playlistEntries: playlistArray });
});

app.post('/search', async (req, res) => {
    let data = req.body;

    axios.post('http://127.0.0.1:9000/searchPlaylists', {
        searchTerm: data.searchTerm
    })
    .then((response) => {
        console.log(response.data);
    }, (error) => {
        console.warn(error);
    });

    res.redirect('/results');
});

app.listen(8080);