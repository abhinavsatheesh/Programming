const fbdl = require("fbdl-core");
const fs = require("fs");
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
 

readline.question('Enter Facebook Link', link => {
	console.log("Link entered " + link)
	fbdl.download(link)
    .then(res => {
        res.pipe(fs.createWriteStream("./video.mp4"));
    });
	console.log("Download Complete!")
  readline.close();
});

 