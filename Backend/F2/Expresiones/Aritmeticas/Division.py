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

        return self.dividir(opIzq.getValor(), opDer.getValor(), newTemp, generator)

    def getNode(self):
        return super().getNode()

    def dividir(self, opIzq, opDer, newTemp, generator):
        #INT
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "/")
            self.tipo = Tipo.ENTERO
            newValue = Value(newTemp, self.tipo, True)
            return newValue

        #DOUBLE
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "/")
            self.tipo = Tipo.DOBLE
            newValue = Value(newTemp, self.tipo, True)
            return newValue

        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE or self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "/")
            self.tipo = Tipo.DOBLE
            newValue = Value(newTemp, self.tipo, True)
            return newValue

        return Excepcion("Semántico", "Los tipos de datos para el signo \"/\" no pueden ser operados", self.fila, self.columna)

