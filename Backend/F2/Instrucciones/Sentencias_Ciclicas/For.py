from Abstract.Instruccion import Instruccion

class For(Instruccion):
    def __init__(self, identificador, expresionIzq, expresionDer, instrucciones, fila, columna):
        self.identificador = identificador
        self.expresionIzq = expresionIzq
        self.expresionDer = expresionDer
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table, generator):
        return super().interpretar(tree, table, generator)

    def getNode(self):
        return super().getNode()
        