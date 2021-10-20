from TS.Tipo import Tipo

class Value:
    def __init__(self, valor, tipo, isTemp):
        self.valor = valor
        self.tipo = tipo
        self.isTemp = isTemp
        self.trueLabel = None
        self.falseLabel = None

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = str(valor)

    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getIsTemp(self):
        return self.isTemp

    def getTrueLabel(self):
        return self.trueLabel

    def getFalseLabel(self):
        return self.falseLabel

    