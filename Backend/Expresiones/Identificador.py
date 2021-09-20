from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo

class Identificador(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        simbolo = table.getTabla(self.identificador)

        if simbolo == None:
            return Excepcion("Semántico", "La variable \""+self.identificador+"\" no existe", self.fila, self.columna)
        
        self.tipo = simbolo.getTipo()

        return simbolo.getValor()


        