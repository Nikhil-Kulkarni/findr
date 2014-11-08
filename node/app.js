var express = require('express');
var app = express();
var name = "asdf";

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/views/styles'));

app.get('/', function(req, res) {
	res.render('default');
});

app.post('/nextPage', function(req, res) {
	console.log('Location: ' + req.body.location);
})

// app.get('/list', function(req, res) {
// 	var location = req.body.loc;
// 	var cuisine = req.body.cuisine;
// 	var restriction = req.body.restriction;
// 	console.log(location + cuisine + restriction);
// 	res.render('list');
// })

app.post('/list', function(req, res) {
	var location = req.body.loc;
	var cuisine = req.body.cuisine;
	var restriction = req.body.restriction;
	console.log(location + cuisine + restriction);
	res.render('list');
})

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