class Add:
    def __init__(self, num, num2):
        self.numeroUno = num
        self.numeroDos = num2
        
    def imprime(self):
        print(self.numeroUno)
        
class ImprimirDosNumeros(Add):
    def __init__(self, num, num2):
        super().__init__(num, num2)
        
    def imprime(self):
        super().imprime()
        print(self.numeroDos)
        
imp = ImprimirDosNumeros(2, 3)
imp.imprime()