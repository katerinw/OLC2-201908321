from Instrucciones.Funciones.Funcion import Funcion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from math import tan

class Tan(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla('Tan$$Parametros123')

        if simbolo == None:
            pass

        if simbolo.getTipo() != Tipo.ENTERO:
            pass

        self.tipo = simbolo.getTipo()
        return tan(simbolo.getValor())

        