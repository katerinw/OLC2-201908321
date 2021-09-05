from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from TS.TablaSimbolos import TablaSimbolos

class Funcion(Instruccion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = Tipo.NULO
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos(table)
        for instruccion in self.instrucciones:
            value = instruccion.interpretar(tree, nuevaTabla) #Devuelve el nodo del resultado de la funcion si es un return
            if isinstance(value, Excepcion):
                tree.getExcepciones().append(value)
                tree.updateConsolaln(value.toString())

        return None