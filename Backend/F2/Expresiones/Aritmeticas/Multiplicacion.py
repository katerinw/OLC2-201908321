from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class Multiplicacion(Instruccion):
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

        newTemp = generator.createTemp()

        return self.multiplicar(opIzq, opDer, newTemp, tree, generator)

    def getNode(self):
        return super().getNode()

    def multiplicar(self, opIzq, opDer, newTemp, tree, generator):
        valIzq = self.correctValue(opIzq)
        valDer = self.correctValue(opDer)
        #INT
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            tree.updateConsola(generator.newExpresion(newTemp, str(valIzq), str(valDer), "*"))
            self.tipo = Tipo.ENTERO
            valor = opIzq.getValor()*opDer.getValor()
            newValue = Value(valor, newTemp, self.tipo, True)
            return newValue

        #DOUBLE
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            tree.updateConsola(generator.newExpresion(newTemp, str(valIzq), str(valDer), "*"))
            self.tipo = Tipo.DOBLE
            valor = opIzq.getValor()*opDer.getValor()
            newValue = Value(valor, newTemp, self.tipo, True)
            return newValue

        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO or self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            tree.updateConsola(generator.newExpresion(newTemp, str(valIzq), str(valDer), "*"))
            self.tipo = Tipo.DOBLE
            valor = opIzq.getValor()*opDer.getValor()
            newValue = Value(valor, newTemp, self.tipo, True)
            return newValue

        #STRING
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.CADENA

        return Excepcion("Semántico", "Los tipos de datos para el signo \"*\" no pueden ser operados", self.fila, self.columna)

    def correctValue(self, valor):
        if valor.isTemp:
            return valor.getTemporal()
        else:
            return valor.getValor()