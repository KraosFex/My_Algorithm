from abc import ABCMeta

class FloatABC(metaclass=ABCMeta):
    pass

@FloatABC.register
class Mi_class:
    pass

x = Mi_class



