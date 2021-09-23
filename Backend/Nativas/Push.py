from Abstract.Instruccion import Instruccion
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from copy import copy

class Push(Instruccion):
    def __init__(self, arreglo, valor, fila, columna):
        self.arreglo = arreglo
        self.valor = valor
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        arreglo = self.arreglo.interpretar(tree, table)
        if isinstance(arreglo, Excepcion):
            return arreglo

        if self.arreglo.tipo != Tipo.ARREGLO and isinstance(arreglo, list):
            return Excepcion("Semántico", "La variable para la función nativa Push! no es tipo Arreglo", self.fila, self.columna)
        
        if isinstance(self.valor, list):
            valor = copy(self.valor)
            self.copiarArreglo(valor, self.valor)
            val = self.interpretarArreglos(tree, table, valor)
            if isinstance(val, Excepcion):
                return val
                    
        else:
            valor = self.valor.interpretar(tree, table)
            if isinstance(valor, Excepcion):
                return valor

        self.tipo = Tipo.ARREGLO
        arreglo.append(valor)
        return arreglo

    def interpretarArreglos(self, tree, table, arreglo):
        i = 0
        while i < len(arreglo):
            if isinstance(arreglo[i], list):
                self.interpretarArreglos(tree, table, arreglo[i])
            else:
                valor = arreglo[i].interpretar(tree, table)
                if isinstance(valor, Excepcion):
                    return valor
                arreglo[i] = valor
            i += 1
        return None


    def copiarArreglo(self, valor, arreglo):
        i = 0
        while i < len(arreglo):
            if isinstance(arreglo[i], list):
                valor[i] = copy(arreglo[i])
            else:
                valor[i] = copy(arreglo[i])
            i += 1
        return None        


    def getNode(self):
        nodo = NodeCst("nativas_instr")
        nodo.addChild("PUSH!")
        nodo.addChildNode(self.arreglo.getNode())
        if isinstance(self.valor, list):
            self.listaNode(self.valor, nodo)
        else:
            nodo.addChildNode(self.valor.getNode())

    def listaNode(self, value, nodo):
        for val in value:
            if isinstance(val, list):
                self.listaNode(val, nodo)
            else:
                nodo.addChildNode(val.getNode())
        return None
