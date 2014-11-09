var express = require('express');
var app = express();
var name = "asdf";
var bodyParser = require('body-parser');
var loc;
var cuisine;
var restrictions;

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/views/styles'));
app.use(bodyParser());

app.get('/', function(req, res) {
	res.render('default');
});

app.post('/list', function(req, res) {
	loc = req.body.loc;
	cuisine = req.body.cuisine;
	restrictions = req.body.restrictions;
	console.log(loc);
	console.log(cuisine);
	console.log(restrictions);
	res.render('list');
})

app.get('/list', function(req, res) {
	res.send(loc, cuisine, restrictions);
})

/* TESTING CODE BELOW ------>  CODE ABOVE*/
app.get('/who/:name?/:title?', function(req, res) {
	var name = req.params.name;
	var title = req.params.title;
	res.send('name: ' + name + '<br></br> title: ' + title);
});

app.get('*', function(req, res) {
	res.send('bad route');
});

var server = app.listen(5000, function() {
	console.log('Listening on port 5000');
})