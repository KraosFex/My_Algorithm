// Este ejemplo si no lo entendi para nada
// Esto es a lo que llaman cierres o closures
 function multiplicar(factor){
    return numero => numero * factor
 }

 let duplicar = multiplicar(11)

 console.log(duplicar(5))

 console.log(duplicar(6))

 console.log(duplicar(7))


 // Explicacion del ejemplo, que la verdad no entendi nadita:
 /*
 * En este ejemplo, se llama a multiplicar y esta crea un entorno en el que su 
 * parametro factor esta ligado a 10. El valor de funcion que retorna, el cual es
 * almacenado en duplicar, recuerda este entorno. Asi que cuando duplicar es llamada
 * multiplica su argumento por 5
 */