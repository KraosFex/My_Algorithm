function desconocida(nombre, cb){
    setTimeout(()=> {
        console.log(`Bicho loco pero que'jesto, tu ta loco ${nombre}`)
        cb(nombre)
    }, 1000)
}

function buenoSi(nombre){
    setTimeout(()=>{
        console.log(`Bueno si estoy loco, loco por meterte el webo ${nombre}`)
    }, 1500)
}

function yoNosToyLoco(nombre){
    console.log("Nooo yo nostoy loco mijitaaaa!!! yo...");
    buenoSi('Mariantonia')
}

desconocida('Luis Daniel', yoNosToyLoco)
