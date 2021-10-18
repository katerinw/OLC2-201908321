from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class BooleanValue(Instruccion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        if self.tipo != Tipo.BANDERA:
            return Excepcion("Semántico", "El valor no es tipo BOOLEAN", self.fila, self.columna)

        return Value(str(self.valor), self.tipo, False)

    def getNode(self):
        return super().getNode()