from Instrucciones.Funciones.Funcion import Funcion
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from math import sin

class Sin(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        tipo = Tipo.NULO

    def interpretar(self, tree, table):
        simbolo = table.getTabla('Sin$$Parametros123')

        if simbolo == None:
            return Excepcion("Semántico", "No se encontró el parametro de la función nativa \"Sin\"", self.fila, self.columna)

        if simbolo.getTipo() != Tipo.ENTERO and simbolo.getTipo() != Tipo.DOBLE:
            return Excepcion("Semántico", "La variable \""+ self.identificador +"\" para \"Sin\" no es tipo Int64 o Float64", self.fila, self.columna)

        self.tipo = simbolo.getTipo()
        return sin(simbolo.getValor())


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
        