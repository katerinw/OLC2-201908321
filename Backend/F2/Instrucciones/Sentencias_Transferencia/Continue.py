from Abstract.Instruccion import Instruccion

class Continue(Instruccion):
    def __init__(self, fila, columna):
        super().__init__(fila, columna)
    
    def interpretar(self, tree, table, generator):
        return super().interpretar(tree, table, generator)

    def getNode(self):
        return super().getNode()