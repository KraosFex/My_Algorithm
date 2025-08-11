function encontrarSolucion(objetivo){
    function encontrar(actual, historia){
        if(actual === objetivo){
            return historia;
        } else if( actual > objetivo){
            return null;
        } else {
            return encontrar(actual + 5, `(${historia}) + 5)`) || 
                   encontrar(actual * 3, `(${historia}) * 3)`);
        }
    }
    return encontrar(1, "1");
}

console.log(encontrarSolucion(20))
console.log(encontrarSolucion(21))
console.log(encontrarSolucion(22))
console.log(encontrarSolucion(23))
console.log(encontrarSolucion(24))
console.log(encontrarSolucion(25))
