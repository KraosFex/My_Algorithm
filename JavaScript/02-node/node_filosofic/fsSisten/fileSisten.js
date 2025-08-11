const fs = require("fs");

function readFile(rute, cb){
    fs.readFile(rute, (err, data) => {
        cb(data.toString(  ))
    })
}

readFile(__dirname+"/ArchivoDelectura.txt", console.log)
