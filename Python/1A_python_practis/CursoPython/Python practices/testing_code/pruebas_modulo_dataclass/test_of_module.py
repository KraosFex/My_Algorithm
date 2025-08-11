from dataclasses import dataclass

@dataclass
class Persona:
    """Este es el primer data class que creo
    """
    nombre: str
    apellido: str
    edad: int
    active: bool = False

def clientes_activos(clientes: list[Persona]):
    return (clientes for cliente in clientes if cliente.active == True)

def imprime_cliente_valido(clientes: Iterator[Persona]):
    for cliente in clientes:
        print(cliente)

persona1 = Persona(nombre="Jose", apellido="malave",edad=52, active=True)
persona2 = Persona(nombre="luis", apellido="casanai",edad=34, active=False)
persona3 = Persona(nombre="marino", apellido="ervalo",edad=41, active=True)
        
lista_de_clientes: list[Persona] = [persona1, persona2, persona3]

imprime_cliente_valido(clientes_activos(lista_de_clientes))
