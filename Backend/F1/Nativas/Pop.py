from Abstract.Instruccion import Instruccion
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Pop(Instruccion):
    def __init__(self, expresion, fila, columna):
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        expresion = self.expresion.interpretar(tree, table)
        if isinstance(expresion, Excepcion):
            return expresion
        
        if self.expresion.tipo != Tipo.ARREGLO and isinstance(expresion, list):
            return Excepcion("Semántico", "La variable para la función nativa Pop! no es tipo Arreglo", self.fila, self.columna)

        valor = expresion.pop()
        self.tipo = self.tipoDato(valor)

        return valor


    def tipoDato(self, value):
        if isinstance(value, int):
            return Tipo.ENTERO
        elif isinstance(value, float):
            return Tipo.DOBLE
        elif isinstance(value, str):
            if len(value) == 1:
                return Tipo.CARACTER
            else:
                return Tipo.CADENA
        elif isinstance(value, bool):
            return Tipo.BANDERA
        elif isinstance(value, list):
            return Tipo.ARREGLO

    def getNode(self):
        nodo = NodeCst("nativas_instr")
        nodo.addChild("POP!")
        nodo.addChildNode(self.expresion.getNode())
        return nodo
