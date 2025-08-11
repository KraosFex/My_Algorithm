// ejemplo 1
// tipo que depende de una property para el resultado de un funcion
type Dependant<T extends { property: any }> = T["property"];

type Independant = {
  property: number;
};

const dependant: Dependant<Independant> = 1;

console.log(dependant);

// ejemplo 2
enum Number1 {
  "NUMBER1" = "number1",
  "NUMBER2" = "number2",
}

enum Number2 {
  "NUMBER3" = "number3",
}

const myNumber = { ...Number1, ...Number2 } as const;
const mixValues = Object.values(myNumber);

type mixValues = (typeof mixValues)[number];

type Enums = {
  [Key in mixValues]: any;
};
