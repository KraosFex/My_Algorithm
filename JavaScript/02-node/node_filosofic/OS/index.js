const os = require('os')

const SIZE = 1024;

function KB(bytes) {
    return bytes / SIZE;
}

function MB(bytes) {
    return KB(bytes) / SIZE;
}

function GB(bytes) {
    return MB(bytes) / SIZE;
}
console.log(os.totalmem())
console.log(os.freemem())
console.log(KB(os.freemem()))
console.log(MB(os.freemem()))
console.log(GB(os.freemem()))
console.log(os.cpus())

