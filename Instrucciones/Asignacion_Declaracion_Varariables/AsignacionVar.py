from Abstract.Instruccion import  Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from TS.Simbolo import Simbolo

class AsignacionVar(Instruccion):
    def __init__(self, identificador, valor, tipo, fila, columna):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.valor.interpretar(tree, table)
        if isinstance(value, Excepcion):
            return value

        if self.tipo == None:
            self.tipo = self.valor.tipo

        if self.tipo != self.valor.tipo:
            return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna)

        simbolo = Simbolo(str(self.identificador), self.valor.tipo, value, None, None, self.fila, self.columna)

        result = table.setTabla(simbolo)
        if isinstance(result, Excepcion):
            return result

        if result == True:
            result = table.actualizarTabla(simbolo)
        
        return None

        
        