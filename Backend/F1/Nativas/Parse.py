from Abstract.Instruccion import Instruccion
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Parse(Instruccion):
    def __init__(self, tipo, expresion, fila, columna):
        self.tipo = tipo
        self.expresion = expresion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        expresion = self.expresion.interpretar(tree, table)
        if isinstance(expresion, Excepcion):
            return expresion
        
        if self.tipo == Tipo.ENTERO:
            #string a entero
            if self.expresion.tipo == Tipo.CADENA:
                try:
                    return int(str(expresion))
                except:
                    return Excepcion("Semántico", "No se puede parsear para Int64", self.fila, self.columna)

        if self.tipo == Tipo.DOBLE:
            #string a float
            if self.expresion.tipo == Tipo.CADENA:
                try:
                    return float(str(expresion))
                except:
                    return Excepcion("Semántico", "No se puede parsear para Float64", self.fila, self.columna)

        return Excepcion("Semántico", "El tipo de dato del parametro no es String", self.fila, self.columna)

    def getNode(self):
        nodo = NodeCst("nativas_instr")
        nodo.addChild("PARSE")
        nodo.addChild(str(self.tipoDato(self.tipo)))
        nodo.addChildNode(self.expresion.getNode())
        return nodo

    def tipoDato(self, tipo):
        if tipo == Tipo.BANDERA:
            return "Bool"
        elif tipo == Tipo.CADENA:
            return "String"
        elif tipo == Tipo.CARACTER:
            return "Char"
        elif tipo == Tipo.DOBLE:
            return "Float64"
        elif tipo == Tipo.ENTERO:
            return "Int64"
        elif tipo == Tipo.NULO:
            return "Nothing"