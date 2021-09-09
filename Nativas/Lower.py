from re import T
from Instrucciones.Funciones.Funcion import Funcion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Lower(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla('Lower$$Parametros123')

        if simbolo == None:
            return Excepcion("Semántico", "No se encontro el parametro de la funcion nativa \"Lowercase\"", self.fila, self.columna)

        if simbolo.getTipo() != Tipo.CADENA:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para Lowercase no es tipo Int64", self.fila, self.columna)

        self.tipo = Tipo.CADENA
        return simbolo.getValor().lower()