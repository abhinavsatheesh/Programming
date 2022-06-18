const http = require('https'); // or 'https' for https:// URLs
const fs = require('fs');
var path = require('path')
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
readline.question('Enter Link', link => {
	console.log("Link entered " + link)
	cwd = process.cwd()
    extension = path.extname(link)
	const file = fs.createWriteStream("file" + extension);
	const request = http.get(link, function(response) {
	response.pipe(file);
	});
	console.log("Download Complete!")
  readline.close();
});