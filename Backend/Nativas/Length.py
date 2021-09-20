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
        simbolo = table.getTabla('Length$$Parametros123')

        if simbolo == None:
            return Excepcion("Semántico", "No se encontro el parametro de la funcion nativa \"Length\"", self.fila, self.columna)

        if simbolo.getTipo() != Tipo.ARREGLO:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para Length no es un Arreglo", self.fila, self.columna)

        self.tipo = Tipo.ENTERO
        return len(simbolo.getValor())