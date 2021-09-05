from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion

class DeclaracionVar(Instruccion):
    def __init__(self, identificador, local, globall, fila, columna):
        self.identificador = identificador
        self.local = local
        self.globall = globall
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return super().interpretar(tree, table)