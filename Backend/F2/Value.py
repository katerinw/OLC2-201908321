from TS.Tipo import Tipo

class Value:
    def __init__(self, valor, tipo, isTemp):
        self.valor = valor
        self.tipo = tipo
        self.isTemp = isTemp

    def getValue(self):
        return str(self.valor)