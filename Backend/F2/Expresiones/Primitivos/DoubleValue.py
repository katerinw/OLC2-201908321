from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class DoubleValue(Instruccion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        if self.tipo != Tipo.DOBLE:
            return Excepcion("Semántico", "El valor no es tipo DOUBLE", self.fila, self.columna)

        return Value(self.valor, "", self.tipo, False)

    def getNode(self):
        return super().getNode()