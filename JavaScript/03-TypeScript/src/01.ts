// typescript => javascript con esteroides

class Persona {
  name: string;

  constructor(name: string){
    this.name = name;
  }

  getName(): string {
    return this.name;
  }

  setName(name: string): void {
    this.name = name;
  }
};

interface IPersona {
  name: string;
  getName(): string;
  setName(name: string): void;
}

const xPerson: Persona = new Persona("johan manuel");

const IPerson: IPerson = xPerson


