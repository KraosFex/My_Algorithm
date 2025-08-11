// ejemplo de funciones recursivas
// Este ejemplo es igual al anterior, el tema es que en 
// cuestion de consumo de recursos esta funcion es una mierda

function potencia(base, exponente){
    if(exponente === 0){
        return 1;
    } else {
        return base * potencia(base, exponente -1)
    }
}

console.log(potencia(2,3))
console.log(potencia(3,2))
console.log(potencia(4,5))
console.log(potencia(5,4))
console.log(potencia(6,7))
console.log(potencia(7,6))
