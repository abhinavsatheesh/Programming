const fs = require('fs');
const ytdl = require('ytdl-core');
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
});
 
readline.question('Enter YouTube Link', link => {
	console.log("Link entered " + link)
	ytdl(link).pipe(fs.createWriteStream('video.mp4'));
	console.log("Download Complete!")
  readline.close();
});
// TypeScript: import ytdl from 'ytdl-core'; with --esModuleInterop
// TypeScript: import * as ytdl from 'ytdl-core'; with --allowSyntheticDefaultImports
// TypeScript: import ytdl = require('ytdl-core'); with neither of the above

