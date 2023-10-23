const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios')

const app = express();

app.set('view engine', 'ejs');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded( { extended: false } ));
app.use('/public', express.static(__dirname + '/public'));



app.get('/', (req, res) => {
    res.render('pages/home');
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
