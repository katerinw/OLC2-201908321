from Abstract.Instruccion import Instruccion

class Return(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        return self

    def getNode(self):
        return super().getNode()