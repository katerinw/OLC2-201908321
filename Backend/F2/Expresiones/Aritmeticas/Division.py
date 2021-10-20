from Expresiones.Relacionales.Diferente import Diferente
from Expresiones.Primitivos.IntValue import IntValue
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class Division(Instruccion):
    def __init__(self, opIzq, opDer, fila, columna):
        self.opIzq = opIzq
        self.opDer = opDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table, generator):
        opIzq = self.opIzq.interpretar(tree, table, generator)
        if isinstance(opIzq, Excepcion):
            return opIzq

        opDer = self.opDer.interpretar(tree, table, generator)
        if isinstance(opDer, Excepcion):
            return opDer

        newTemp = generator.newTemp()

        return self.dividir(opIzq.getValor(), opDer.getValor(), newTemp, tree, table, generator)

    def getNode(self):
        return super().getNode()

    def dividir(self, opIzq, opDer, newTemp, tree, table, generator):
        #INT
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.ENTERO
            return self.returnValue(opIzq, opDer, newTemp, tree, table, generator)
            
        #DOUBLE
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.DOBLE
            return self.returnValue(opIzq, opDer, newTemp, tree, table, generator)

        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE or self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.DOBLE
            return self.returnValue(opIzq, opDer, newTemp, tree, table, generator)

        return Excepcion("Semántico", "Los tipos de datos para el signo \"/\" no pueden ser operados", self.fila, self.columna)


    def returnValue(self, opIzq, newTemp, tree, table, opDer, generator):
        trueIns = generator.newExpresion(newTemp, str(opIzq), str(opDer), "/")
        falseIns = generator.newCallFunc('print_math_error_armc')  

        cero = IntValue(0, Tipo.ENTERO, self.fila, self.columna)
        diferente = Diferente(self.opDer, cero, self.fila, self.columna)
        diferente.interpretar(tree, table, generator)
        
        generator.addOpRelacional(diferente, trueIns, falseIns)
        newValue = Value(newTemp, self.tipo, True)
        return newValue