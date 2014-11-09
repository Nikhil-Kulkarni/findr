var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var mongoose = require('mongoose');
var PythonShell = require('python-shell');
var pyshell = new PythonShell('ClassifyRestaurants_Multiclassification.py');
var s = require('string');
var fs = require('fs');
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
	// var options = {
 //  		mode: 'text',
 //  		scriptPath: 'C:/Users/IMSA Student/Desktop/findr/node/python',
 //  		args: [loc, cuisine, restrictions]
	// };
	var result;
	var wstream = fs.createWriteStream('myOutput.txt');
	wstream.write(loc + '\n');
	wstream.write(cuisine + '\n');
	wstream.write(restrictions + '\n');
	wstream.end();

	PythonShell.run('ClassifyRestaurants_Multiclassification.py', function(err, results) {
		if (err) {
			throw err;
		}
		console.log('Results:  %j', results);
			res.render('list',{name: results[0], link: results[2],
								name2: results[1], link2: results[3]});

	});

});


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