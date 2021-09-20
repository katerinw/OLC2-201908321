from Instrucciones.Funciones.Funcion import Funcion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from math import log

class Log(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simboloBase = table.getTabla('Log$$Parametros123')
    
        simbolo = table.getTabla('Log$$Parametros456')

        if simbolo == None or simboloBase == None:
            return Excepcion("Semántico", "No se encontro el parametro de la funcion nativa \"Log\"", self.fila, self.columna)

        if simboloBase.getTipo() != Tipo.ENTERO or simbolo.getTipo() != Tipo.ENTERO:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para \"Log\" no es tipo Int64", self.fila, self.columna)

        self.tipo = simboloBase.getTipo()
        return log(simbolo.getValor(), simboloBase.getValor())
        
