from TS.Excepcion import Excepcion
from Instrucciones.Funciones.Funcion import Funcion
from TS.Tipo import Tipo

class Length(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        pass