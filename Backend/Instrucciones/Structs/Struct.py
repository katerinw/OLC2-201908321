from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Struct(Instruccion):
    def __init__(self, identificador, atributos, mutable, fila, columna):
        self.identificador = identificador
        self.atributos = atributos
        self.mutable = mutable
        self.tipo = Tipo.STRUCT
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        return self