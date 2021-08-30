from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorRelacional, Tipo

class OperacionRelacional(Instruccion):
    def __init__(self, operador, opIzq, opDer, fila, columna):
        self.operador = operador
        self.opIzq = opIzq
        self.opDer = opDer
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        opIzq = self.opIzq.interpretar(tree, table)
        if isinstance(opIzq, Excepcion):
            return opIzq
        
        if self.opDer != None:
            opDer = self.opDer.interpretar(tree, table)
            if isinstance(opDer, Excepcion):
                return opDer

        #igualacion
        if self.operador == OperadorRelacional.IGUALIGUAL:
            pass

        #diferente
        elif self.operador == OperadorRelacional.DIFERENTE:
            pass

        #menor que
        elif self.operador == OperadorRelacional.MENOR:
            pass

        #mayor que
        elif self.operador == OperadorRelacional.MAYOR:
            pass

        #menor igual
        elif self.operador == OperadorRelacional.MENORIGUAL:
            pass

        #mayor igual
        elif self.operador == OperadorRelacional.MAYORIGUAL:
            pass

    




    def getType(self, nodo, valor):
        if nodo.tipo == Tipo.ENTERO:
            return int(valor)
        elif nodo.tipo == Tipo.DOBLE:
            return float(valor)
        elif nodo.tipo == Tipo.CADENA:
            return str(valor)
        elif nodo.tipo == Tipo.CARACTER:
            return str(valor)
        elif nodo.tipo == Tipo.BANDERA:
            if str(valor).lower() == 'true':
                return True
            elif str(valor).lower() == 'false':
                return False
        return valor