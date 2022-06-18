var os = require('os');
if (os.type() === "Windows_NT") {
  system = "Windows";
}

else {
  system = os.type()
}
console.log("System: " + system)
console.log("Node Name: " + os.hostname())
console.log("Version: " + os.release())
console.log("Machine: " + os.arch())
console.log("Current Working Directory: " + process.cwd())

