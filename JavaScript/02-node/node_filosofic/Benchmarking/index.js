//  Truquitos en el codigo que nadie quiere que sepas mi pana
// console.time('')
// console.timeEnd('')

// Acostumbrarse a usar el debugging del codigo

// Error first callbacks (Primera vez que lo escucho)
// como se ve a nivel de codigo
function asincrona(callback) {
    // ...
    setTimeout(function () {
        try {
            let a = 3 + z
            callback(null, a)
        } catch (e) {
            callback(e)
        }
    }, 1000)
}

asincrona(function (err, data) {
    if (err) {
        console.error(err);
        return err
    } else {
        console.log(`Very fine ${data}`)
    }
})
