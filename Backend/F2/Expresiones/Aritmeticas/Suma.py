from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from Value import Value

class Suma(Instruccion):
    def __init__(self, opIzq, opDer, fila, columna):
        self.opIzq = opIzq
        self.opDer = opDer
        self.fila = fila
        self.columna = columna
        self.generador = None
        self.tipo = None

    def interpretar(self, tree, table):
        self.opIzq.generador = self.generador
        self.opDer.generador = self.generador

        opIzq = self.opIzq.interpretar(tree, table)
        opDer = self.opDer.interpretar(tree, table)

        newTemp = self.generador.newTemp()

        return self.sumar(opIzq, opDer, newTemp)

    def getNode(self):
        return super().getNode()

    def sumar(self, opIzq, opDer, newTemp):
        if opIzq.tipo == Tipo.ENTERO and opDer.tipo == Tipo.ENTERO:
            self.generador.addExpresion(newTemp, opIzq.getValue(), opDer.getValue(), "+")
            self.tipo = Tipo.ENTERO
            return Value(newTemp, self.tipo, True)
        elif opIzq.tipo == Tipo.ENTERO and opDer.tipo == Tipo.DOBLE:
            self.generador.addExpresion(newTemp, opIzq.getValue(), opDer.getValue(), "+")
            self.tipo = Tipo.DOBLE
            return Value(newTemp, self.tipo, True)
        elif opIzq.tipo == Tipo.DOBLE and opDer.tipo == Tipo.DOBLE:
            self.generador.addExpresion(newTemp, opIzq.getValue(), opDer.getValue(), "+")
            self.tipo = Tipo.DOBLE
            return Value(newTemp, self.tipo, True)
        elif opIzq.tipo == Tipo.DOBLE and opDer.tipo == Tipo.ENTERO:
            self.generador.addExpresion(newTemp, opIzq.getValue(), opDer.getValue(), "+")
            self.tipo = Tipo.DOBLE
            return Value(newTemp, self.tipo, True)
        
        return Value("0", Tipo.ENTERO, False)
        #return Excepcion("Semántico", "Los tipos de datos para el signo \"+\" no pueden ser operados", self.fila, self.columna)


    