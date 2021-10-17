from Abstract.Instruccion import Instruccion
from TS.Tipo import Tipo
from Value import Value

class IntVal(Instruccion):
    def __init__(self, valor, tipo, fila, columna):
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna
        self.generador = None

    def interpretar(self, tree, table):
        if self.tipo != Tipo.ENTERO and self.tipo != Tipo.DOBLE:
            print("ERROR")
            return Value("0", Tipo.ENTERO, False)

        return Value(str(self.valor), self.tipo, True)

    def getNode(self):
        return super().getNode()