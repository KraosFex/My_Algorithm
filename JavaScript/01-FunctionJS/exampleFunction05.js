// Esta funcion es un buen ejemplo para demostar el caso anterio,
// donde el segundo argumento que recive es obcional.

function potencia(base, exponente = 2) {
    let resultado = 1;
    for ( let cuenta =  0; cuenta < exponente; cuenta ++){
        resultado *= base
    }
    return resultado
}

console.log(potencia(25))

console.log(potencia(25,5))