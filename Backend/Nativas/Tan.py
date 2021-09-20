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
            return Excepcion("Semántico", "No se encontró el parametro de la función nativa \"TAN\"", self.fila, self.columna)


        if simbolo.getTipo() != Tipo.ENTERO and simbolo.getTipo() != Tipo.DOBLE:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para Tan no es tipo Int64 o Float64", self.fila, self.columna)


        self.tipo = simbolo.getTipo()
        return tan(simbolo.getValor())

        