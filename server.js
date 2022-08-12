var express = require('express');
var app = express();
var http = require('http').Server(app);
var io = require('socket.io')(http);
var child = require('child_process');
const multer = require("multer");
let filename;
app.use(express.static('public'));

app.get('/', function(req, res){
	res.sendFile(__dirname + '/index.html');
	// Setup Storage
	const storage = multer.diskStorage({
		// Set the destination where the files should be stored on disk
		destination: function (req, file, cb) {cb(null, "uploads");},
		// Set the file name on the file in the uploads folder
		filename: function (req, file, cb) {
			filename = file.fieldname + "-" + Date.now()+".mp4"
			cb(null, file.fieldname + "-" + Date.now()+".mp4");
		},
	});
		// Setup multer
		const upload = multer({ storage: storage }); // { destination: "uploads/"}
		// Setup the upload route
		app.post("/upload", upload.single("data"), (req, res) => {
		console.log(req.file);
		res.redirect('/blur');
		console.log('file uploded to server!');
		});
		
});
app.get('/blur', function(req, res){
	res.sendFile(__dirname + '/blur.html');
})
app.get('/run', function(req, res){
	res.sendFile(__dirname + '/run.html');
	io.on('connection', function(socket){
		var python = child.spawn( 'python', ['Run.py',"uploads/"+filename],[]);

		python.stdout.on('data',function(data){
			console.log(data.toString());
			socket.emit('newdata', data.toString());
		});
		socket.on('user_choice', (msg) => {
			console.log('user choice:',msg);
			console.log('creating file choice.txt..');
			const fs = require('fs');

			fs.writeFile('./choice/choice.txt', msg, err => {
			if (err) {console.error(err);}})
			// file written successfully
		});

		python.stderr.on('data', function (data) {
			console.log(data.toString());
			console.log('Failed to start child process.');
		})
	})
})

http.listen(8080, function(){console.log('listening on *:8080');});
