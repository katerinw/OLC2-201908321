from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos

class LlamadaFuncion(Instruccion):
    def __init__(self, identificador, parametros, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.fila = fila
        self.columna  = columna

    def interpretar(self, tree, table):
        funcion = tree.getFuncion(self.identificador)
        if funcion == None:
            return Excepcion("Semántico", "Función \""+self.identificador+"\" no encontrada", self.fila, self.columna)

        nuevaTabla = TablaSimbolos(tree.getTSGlobal())

        value = funcion.interpretar(tree, nuevaTabla)
        if isinstance(value, Excepcion):
            return value
        
        self.tipo = funcion.tipo
        return value
        