// Esta fue mi solucion al problema que se me planteo.
function digitalRoot(n) {
    // ...
    if(n < 10) return n
    let control = n
    let ReturnValue
    while(true) {
        const str = String(control)
        ReturnValue = 0
        for(let i = 0; i <= str.length - 1 ; i++ ){
            ReturnValue += Number(str[i])
        }      
        if(ReturnValue < 10) {
            break
        }
        control = ReturnValue
    }
    return ReturnValue
  }

console.log(digitalRoot(15))
console.log(digitalRoot(235))
console.log(digitalRoot(4335))

// esta fue la solucion que me humillo 

const digitalRoot2 = (n) => (n-1) % 9 + 1

console.log(digitalRoot2(15))
console.log(digitalRoot2(235))
console.log(digitalRoot2(4335))

