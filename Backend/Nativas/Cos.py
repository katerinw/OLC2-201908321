from Instrucciones.Funciones.Funcion import Funcion
from TS.Tipo import Tipo
from TS.Excepcion import Excepcion
from math import cos

class Cos(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla('Cos$$Parametros123')

        if simbolo == None:
            return Excepcion("Semántico", "No se encontró el parametro de la función nativa \"COS\"", self.fila, self.columna)
        
        if simbolo.getTipo() != Tipo.ENTERO and simbolo.getTipo() != Tipo.DOBLE:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para Cos no es tipo Int64 o Float64", self.fila, self.columna)
        self.tipo = Tipo.ENTERO

        return cos(simbolo.getValor())
