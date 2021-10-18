from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class CharValue(Instruccion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        if self.tipo != Tipo.CARACTER:
            return Excepcion("Semántico", "El valor no es tipo CHAR", self.fila, self.columna)

        return Value(str(self.valor), self.tipo, False)

    def getNode(self):
        return super().getNode()