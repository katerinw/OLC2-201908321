from Instrucciones.Funciones.Funcion import Funcion
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from math import log10

class Log10(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla('Log10$$Parametros123')
        
        if simbolo == None:
            return Excepcion("Semántico", "No se encontro el parametro de la funcion nativa \"Log10\"", self.fila, self.columna)

        if simbolo.getTipo() != Tipo.ENTERO:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para \"Log10\" no es tipo Int64", self.fila, self.columna)

        self.tipo = simbolo.getTipo()

        return log10(simbolo.getValor())

    def getNode(self):
        nodo = NodeCst("nativas_instr")

        nodo.addChild(str(self.identificador))
        parametrosNodo = NodeCst("parametros")
        for parametro in self.parametros:
            parametroNodo = NodeCst("parametro")
            parametroNodo.addChild(str(self.tipoDato(parametro['tipo'])))
            idNodo = NodeCst("expresion")
            idNodo.addChild(str(parametro['identificador']))
            parametroNodo.addChildNode(idNodo)
            parametrosNodo.addChildNode(parametroNodo)
        nodo.addChildNode(parametrosNodo)

        instruccionesNodo = NodeCst("instrucciones")
        for instruccion in self.instrucciones:
            instruccionesNodo.addChildNode(instruccion.getNode())
        nodo.addChildNode(instruccionesNodo)

        return nodo
