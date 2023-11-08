var fs = require('fs')
var cwd = process.cwd()
var directories = fs.readdirSync(cwd)
console.log(directories)