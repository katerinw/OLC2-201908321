from Abstract.Instruccion import Instruccion

class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.ElseIf = ElseIf
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        return super().interpretar(tree, table, generator)

    def getNode(self):
        return super().getNode()