const fs = require('fs')
const stream = require('stream')
const util = require('util')

let readableStream = fs.createReadStream(`${__dirname}/input.txt`)
readableStream.setEncoding('utf-8')

const Transform = stream.Transform;

function Mayus() {
    Transform.call(this);
}

util.inherits(Mayus, Transform);

Mayus.prototype._transform = function (chunk, codif, cb) {
    chuckMayus = chunk.toString().toUpperCase();
    this.push(chuckMayus);
    cb()
}

let mayus = new Mayus();

readableStream
    .pipe(mayus)
    .pipe(process.stdout)

