from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import Tipo

class Declaracion_Arreglos(Instruccion):
    def __init__(self, identificador, dimensiones, fila, columna):
        self.identificador = identificador 
        self.dimensiones = dimensiones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        print("hola")