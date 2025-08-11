from super.Producto import Producto

class Adorno(Producto):
    def __init__(self, ref, nombre, pvp, descrip) -> None:
        super().__init__(ref, nombre, pvp, descrip)
    