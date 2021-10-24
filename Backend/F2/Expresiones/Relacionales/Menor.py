from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class Menor(Instruccion):
    def __init__(self, opIzq, opDer, fila, columna):
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = None
        self.trueLabel = None
        self.falseLabel = None
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table, generator):
        opIzq = self.opIzq.interpretar(tree, table, generator)
        if isinstance(opIzq, Excepcion):
            return opIzq

        opDer = self.opDer.interpretar(tree, table, generator)
        if isinstance(opDer, Excepcion):
            return opDer

        return self.esMenor(opIzq.getValor(), opDer.getValor(), tree, generator)

    def getNode(self):
        return super().getNode()

    def esMenor(self, opIzq, opDer, tree, generator):
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.returnValue(opIzq, opDer, tree, generator)

        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.returnValue(opIzq, opDer, tree, generator)

        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA

        elif (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO) or (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE): 
            self.tipo = Tipo.BANDERA
            return self.returnValue(opIzq, opDer, tree, generator)

        return Excepcion("Semántico", "Los tipos de datos para el signo \"<\" no pueden ser operados", self.fila, self.columna)


    def returnValue(self, opIzq, opDer, tree, generator):
        valor = opIzq < opDer
        newValue = Value(valor, self.tipo, False)
            
        if self.trueLabel == None:
            self.trueLabel = generator.createLabel()

        if self.falseLabel == None:
            self.falseLabel = generator.createLabel()

        tree.updateConsola(generator.newIf(str(opIzq), str(opDer), '<', self.trueLabel))
        tree.updateConsola(generator.newGoto(self.falseLabel))

        newValue.trueLabel = self.trueLabel
        newValue.falseLabel = self.falseLabel

        return newValue