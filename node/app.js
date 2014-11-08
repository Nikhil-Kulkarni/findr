var express = require('express');
var app = express();

app.set('view engine', 'ejs');
app.use(express.static(__dirname + '/views/styles'));

app.get('/', function(req, res){
	res.render('default', {
		title: 'Home',
		users:['Nikhil', 'app', 'random']
		});
});



app.get('/me', function(req, res){
	res.send('@nikhkulkarni');
});

app.get('/who/:name?', function(req, res) {
	var name = req.params.name;
	res.send(name);
});

app.get('/who/:name?/:title?', function(req, res) {
	var name = req.params.name;
	var title = req.params.title;
	res.send('name: ' + name + '<br></br> title: ' + title);
});

app.get('*', function(req, res) {
	res.send('bad route');
});

var server = app.listen(3000, function() {
	console.log('Listening on port 3000');
})