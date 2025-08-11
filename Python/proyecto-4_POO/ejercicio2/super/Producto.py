class Producto:
    def __init__(self, ref, nombre, pvp, descrip) -> None:
        self.ref = ref
        self.nombre = nombre
        self.pvp = pvp
        self.descrip = descrip
    
    
    def __str__(self) -> str:
        return f"REFERENCIA:\t{self.ref}\nNOMBRE:\t{self.nombre}\nPVP:\t{self.pvp}\nDESCRIPCION:\t{self.descrip}"