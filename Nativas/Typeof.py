from Instrucciones.Funciones.Funcion import Funcion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo


class Typeof(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla('TypeOf$$Parametros123')

        if simbolo == None:
            return Excepcion("Semántico", "No se encontro el parametro de la funcion nativa \"TypeOf\"", self.fila, self.columna)

        self.tipo = Tipo.CADENA

        return self.TipoDe(simbolo.getTipo())

    def TipoDe(self, type):
        if type == Tipo.ENTERO:
            return "Int64"
        elif type == Tipo.DOBLE:
            return "Float64"
        elif type == Tipo.BANDERA:
            return "Bool"
        elif type == Tipo.CARACTER:
            return "Char"
        elif type == Tipo.CADENA:
            return "String"
        elif type == Tipo.NULO:
            return "Nothing"