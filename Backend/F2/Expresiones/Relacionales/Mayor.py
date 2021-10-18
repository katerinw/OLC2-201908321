from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class Mayor(Instruccion):
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

        return self.esMayor(opIzq.getValor(), opDer.getValor(), generator)

    def getNode(self):
        return super().getNode()

    def esMayor(self, opIzq, opDer, generator):
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.returnValue(opIzq, opDer, generator)

        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.returnValue(opIzq, opDer, generator)

        elif (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO) or (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE): 
            self.tipo = Tipo.BANDERA
            return self.returnValue(opIzq, opDer, generator)

        return Excepcion("Semántico", "Los tipos de datos para el signo \">\" no pueden ser operados", self.fila, self.columna)


    def returnValue(self, opIzq, opDer, generator):
        newValue = Value("", self.tipo, False)
            
        if self.trueLabel == None:
            self.trueLabel = generator.newLabel()

        if self.falseLabel == None:
            self.falseLabel = generator.newLabel()

        generator.addIf(str(opIzq), str(opDer), '>', self.trueLabel)
        generator.addGoto(self.falseLabel)

        newValue.trueLabel = self.trueLabel
        newValue.falseLabel = self.falseLabel

        return newValue