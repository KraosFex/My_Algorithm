function arranque(user, horasDeConversacion){
    console.log("Iniciando proceso, espere un poco...")
    setTimeout(()=>{
        hola(user, horasDeConversacion)
    }, 1500)
}

function hola(nombre, horasDeConversacion){
    console.log(`Hola, usuario ${nombre}`)
    conversacion(nombre, horasDeConversacion, adios)
}

function adios(nombre){
    console.log(`Adios, usuario ${nombre}`)
}

function hablar(){
    console.log("Blaa, bla, blaa, blaa")
}

function conversacion(nombre, cantidad, adios){
    if(cantidad > 0){
        setTimeout(()=>{
            hablar()
            conversacion(nombre,--cantidad, adios)
        },1200)
    }
    else{
        adios(nombre)
    }
}

arranque('David', 5)