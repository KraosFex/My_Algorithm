// Me parece interesante recordar lo siguiente.
// Asi la funcion sea creada despues de su invocacion, si la funcion
// es una declaracion de funcion, esto no importara. Gracias a el 
// hoisting. una fucionalidad de js.

console.log(`En el futuro: ${futuro()}`)

function futuro() {
    return 'Ganaras millones por que tu futuro es brillante'
}