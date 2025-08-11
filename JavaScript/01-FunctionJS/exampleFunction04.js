// js es muy abierto con la cantidad de los argumento que 
// reciben las funciones. Por lo que si a una funcion se le pasan
// mas argumentos de los que recibe, estos seran descartados y se tomara
// los primeros argumentos. y si no se le pasa nungun argumento, js
// asiganra undefine por defecto.

function cuadrado(x) {
    return x * x
}

console.log(cuadrado(8,'hola', true))

// Esto tambien puede ser usado en nuestro favor, por ejemplo.
function cuadrado(x) {
    if(x === undefined) return undefined
    return x * x
}

console.log(cuadrado())

// tambien se puede configurar para que la funcion asigne otro valor por defecto
// si no se le pasa nada;

function suma(a, b = 1) {
    console.log( a + b)
}

suma(5, 7)
suma(5)



