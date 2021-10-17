from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Resta(Instruccion):
    def __init__(self, opIzq, opDer, fila, columna):
        self.opIzq = opIzq
        self.opDer = opDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table, generator):
        opIzq = self.opIzq.interpretar(tree, table, generator)
        opDer = self.opDer.interpretar(tree, table, generator)

        newTemp = generator.newTemp()

        return self.restar(opIzq, opDer, newTemp, generator)

    def getNode(self):
        return super().getNode()

    def restar(self, opIzq, opDer, newTemp, generator):
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "-")
            self.tipo = Tipo.ENTERO
            return newTemp
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "-")
            self.tipo = Tipo.DOBLE
            return newTemp
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "-")
            self.tipo = Tipo.DOBLE
            return newTemp
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            generator.addExpresion(newTemp, str(opIzq), str(opDer), "-")
            self.tipo = Tipo.DOBLE
            return newTemp

        return Excepcion("Semántico", "Los tipos de datos para el signo \"-\" no pueden ser operados", self.fila, self.columna)