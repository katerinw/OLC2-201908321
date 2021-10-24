from posixpath import basename
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class And(Instruccion):
    def __init__(self, opIzq, opDer, fila, columna):
        self.opIzq = opIzq
        self.opDer = opDer
        self.tipo = None
        self.trueLabel = []
        self.falseLabel = []
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        opIzq = self.opIzq.interpretar(tree, table, generator)
        if isinstance(opIzq, Excepcion):
            return opIzq

        if self.opIzq.tipo != Tipo.BANDERA:
            return Excepcion("Semántico", "Los tipos de datos para el signo \"&&\" no pueden ser operados", self.fila, self.columna)

        self.agregarLabel(opIzq, generator)

        if isinstance(opIzq.trueLabel, list):
            for L in opIzq.trueLabel:
                tree.updateConsola(generator.newLabel(str(L)))
        else:
            tree.updateConsola(generator.newLabel(str(opIzq.trueLabel)))

        opDer = self.opDer.interpretar(tree, table, generator)
        if isinstance(opDer, Excepcion):
            return opDer

        if self.opDer.tipo != Tipo.BANDERA:
            return Excepcion("Semántico", "Los tipos de datos para el signo \"&&\" no pueden ser operados", self.fila, self.columna)

        self.agregarLabel(opDer, generator)

        self.tipo = Tipo.BANDERA

        valor = opIzq.getValor() and opDer.getValor()
        newValue = Value(valor, self.tipo, False)

        self.transferirLabelsTrue(opDer.trueLabel)
        self.transferirLabelsFalse(opIzq.falseLabel)
        self.transferirLabelsFalse(opDer.falseLabel)

        newValue.trueLabel = self.trueLabel
        newValue.falseLabel = self.falseLabel

        return newValue

    def getNode(self):
        return super().getNode()

    def transferirLabelsTrue(self, labels):
        if isinstance(labels, list):
            for L in labels:
                self.trueLabel.append(str(L))
        else:
            self.trueLabel.append(str(labels)) 

    def transferirLabelsFalse(self, labels):
        if isinstance(labels, list):
            for L in labels:
                self.falseLabel.append(str(L))
        else:
            self.falseLabel.append(str(labels)) 

    def agregarLabel(self, op, generator):
        if op.trueLabel == None:
            op.trueLabel = generator.createLabel()

        if op.falseLabel == None:
            op.falseLabel = generator.createLabel()
