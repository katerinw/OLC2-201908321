from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class CharValue(Instruccion):
    def __init__(self, valor, tipo, isTemp, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.isTemp = isTemp
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        if self.tipo != Tipo.CARACTER:
            return Excepcion("Semántico", "El valor no es tipo CHAR", self.fila, self.columna)

        return self.valor

    def getNode(self):
        return super().getNode()