from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class Modulo(Instruccion):
    def __init__(self, opIzq, opDer, fila, columna):
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = None
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        opIzq = self.opIzq.interpretar(tree, table, generator)
        if isinstance(opIzq, Excepcion):
            return opIzq

        opDer = self.opDer.interpretar(tree, table, generator)
        if isinstance(opDer, Excepcion):
            return opDer
        
        generator.modulo = True
        newTemp = generator.createTemp()
        return self.modulo(opIzq, opDer, newTemp, tree, generator)

    def getNode(self):
        return super().getNode()

    def modulo(self, opIzq, opDer, newTemp, tree, generator):
        #INT
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.ENTERO
            return self.c3dModulo(opIzq, opDer, newTemp, tree, generator)

        #DOUBLE
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.DOBLE
            return self.c3dModulo(opIzq, opDer, newTemp, tree, generator)

        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE or self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.DOBLE
            return self.c3dModulo(opIzq, opDer, newTemp, tree, generator)

        return Excepcion("Semántico", "Los tipos de datos para el signo \"%\" no pueden ser operados", self.fila, self.columna)


    def c3dModulo(self, opIzq, opDer, newTemp, tree, generator):
        dividendo = self.correctValue(opIzq)
        divisor = self.correctValue(opDer)
        modulo = generator.newModulo(dividendo, divisor)

        tree.updateConsola(generator.newAsigTemp(newTemp, modulo))

        valor = Value('', newTemp, self.tipo, True)
        return valor

    def correctValue(self, valor):
        if valor.isTemp:
            return valor.getTemporal()
        else:
            return valor.getValor()