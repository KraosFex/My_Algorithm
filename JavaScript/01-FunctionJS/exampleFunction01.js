// Esto es un ejemplo de lo que puede llegar a ser una funcion.
// En este caso se puede ver como una funcion puede ser invocada dentro de otra
// y a la vez es un buen ejemplo para demostra lo que es el entorno lexico de
// funcion.

// NOTA: No recomiendo tener este tipo de funcion llamadas dentro de otras como rutina.
const humus = function (factor) {
  const ingrediente = function (cantidad, unidad, nombre) {
    let cantidadDeIngrediente = cantidad * factor;
    if (cantidadDeIngrediente > 1) {
      unidad += "s";
    }
    console.log(`${cantidadDeIngrediente} ${unidad} ${nombre}`);
  };
  ingrediente(7, "taza", "avena");
};
