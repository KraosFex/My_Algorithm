from abc import ABCMeta, abstractmethod

# definiendo intefaz
class Mando(ABCMeta): 
    @abstractmethod
    def siguiente_canal():
        pass
    
    @abstractmethod
    def anterior_canal():
        pass
    
    @abstractmethod
    def subir_volumen():
        pass
    
    @abstractmethod
    def bajar_volumen():
        pass
    
# implementando interfaz
class MandoSamsung(Mando):
    def __init__():
        pass 
    
    def siguiente_canal():
        print("Canal +")

    def anterior_canal():
        print("Canal -")

    def subir_volumen():
        print("Volumen +")
    
    def bajar_volumen():
        print("Valumen -")

## Instanciando clase de mando
mando1021 = MandoSamsung
mando1021.bajar_volumen()

