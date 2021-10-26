from Expresiones.Relacionales.Diferente import Diferente
from Expresiones.Primitivos.Temporal import Temporal
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

        newTemp = generator.createTemp()

        return self.dividir(opIzq, opDer, newTemp, tree, table, generator)

    def getNode(self):
        return super().getNode()

    def dividir(self, opIzq, opDer, newTemp, tree, table, generator):
        #INT
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.DOBLE
            return self.returnValue(opIzq, opDer, newTemp, tree, table, generator)
            
        #DOUBLE
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.DOBLE
            return self.returnValue(opIzq, opDer, newTemp, tree, table, generator)

        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE or self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.DOBLE
            return self.returnValue(opIzq, opDer, newTemp, tree, table, generator)

        return Excepcion("Semántico", "Los tipos de datos para el signo \"/\" no pueden ser operados", self.fila, self.columna)


    def returnValue(self, opIzq, opDer, newTemp, tree, table, generator):
        valIzq = self.correctValue(opIzq)
        valDer = self.correctValue(opDer)

        trueIns = generator.newExpresion(newTemp, "float64("+str(valIzq)+")", "float64("+str(valDer)+")", "/")
        falseIns = generator.newCallFunc('print_math_error_armc')  

        cero = IntValue(0, Tipo.ENTERO, self.fila, self.columna)
        val = Temporal(opDer, self.fila, self.columna)
        diferente = Diferente(val, cero, self.fila, self.columna).interpretar(tree, table, generator)
        if isinstance(diferente, Excepcion):
            return diferente

        valor = 'NULL'
        if opDer.getValor() != 0:
            valor = opIzq.getValor()/opDer.getValor()

        tree.updateConsola(generator.newOpRelacional(diferente, trueIns, falseIns))
        newValue = Value(valor, newTemp, self.tipo, True)
        return newValue

    def correctValue(self, valor):
        if valor.isTemp:
            return valor.getTemporal()
        else:
            return valor.getValor()
 