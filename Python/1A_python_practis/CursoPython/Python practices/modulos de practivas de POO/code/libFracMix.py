from libFraccion import Fraccion

class FracMix(Fraccion):

    def __init__(self,ent,num=0,den=1):
        self.ent=ent
        super().__init__(num,den)    
        self.simplifica()
        super().simplifica()

    def __str__(self):
        return str(self.ent) + super().__str__()

    def simplifica(self):
        if self.num > self.den:
            aux=self.num//self.den
            self.ent=self.ent+aux
            self.num-=(aux*self.den)
    
    def __add__(self, obj):
        ent=self.ent+obj.ent
        f = super().__add__(obj)
        r = FracMix(ent,f.num,f.den)
        return r

