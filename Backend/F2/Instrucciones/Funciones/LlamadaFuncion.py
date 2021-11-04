#from Instrucciones.Arreglos.AccesoArreglo import AccesoArreglo
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
#from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import Tipo

class LlamadaFuncion(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table, generator):
        funcion = tree.getFuncion(str(self.identificador))
        
        nuevaTabla = TablaSimbolos('functioncall',tree.getTSGlobal()) #cambiar

        value = funcion.interpretar(tree, nuevaTabla, generator)
        if isinstance(value, Excepcion):
            return value

        self.tipo = funcion.tipo
        return value

    def getNode(self):
        return super().getNode()