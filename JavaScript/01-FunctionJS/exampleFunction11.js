function humanReadable (seconds) {
    // 1 => es 1s
    // 60 => 60s => es 1m
    // console.log(min)
    let min = Math.floor(seconds/60)
    let hour = Math.floor(min / 60)
    let sec = Math.ceil((seconds/60 - min) * 60) 
    
    console.log(min /(seconds / 3600))

    if(sec >= 60) {
        sec = 0
    }

    if(min >= 60) {
        min= 0
    }

    const timeH = hour >= 10 ? hour : "0" + hour
    const timeM = min >= 10 ? min : "0" + min
    const timeS = sec >= 10 ? sec : "0" + sec

    if(seconds/60 >= 1 && seconds/60 < 60) {
        return `00:${timeM}:${timeS}`
    }
    else if(seconds/60 >= 60){
        return `${timeH}:${timeM}:${timeS}`
    }
    return `00:00:${seconds > 10 ? seconds : "0" + seconds}`;
}

console.log(humanReadable(90)) // => 00:01:30
console.log(humanReadable(3599)) // => 00:59:59
console.log(humanReadable(3600)) // => 01:00:00
console.log(humanReadable(45296)) // => 12:34:56

