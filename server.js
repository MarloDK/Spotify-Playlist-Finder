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

app.listen(8080);