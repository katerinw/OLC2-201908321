from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Value import Value
from TS.Tipo import Tipo

class Identificador(Instruccion):
    def __init__(self, identificador, fila, columna):
        self.identificador = identificador
        self.trueLabel = None
        self.falseLabel = None
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        simbolo = table.getTabla(self.identificador)

        if simbolo == None:
            return Excepcion("Semántico", "La variable \""+self.identificador+"\" no existe", self.fila, self.columna)

        self.tipo = simbolo.getTipo()

        newTempPosicion = generator.createTemp()
        tree.updateConsola(generator.newExpresion(newTempPosicion, 'P', str(simbolo.posicion), '+'))

        newTemp = generator.createTemp()
        tree.updateConsola(generator.newGetStack(newTemp, str(newTempPosicion)))

        if simbolo.tipo != Tipo.BANDERA:
            return Value(simbolo.getValor().getValor(), newTemp, simbolo.getTipo(), True)
        else:
            value = Value(simbolo.getValor().getValor(), simbolo.getValor().getTemporal(), Tipo.BANDERA, False)
            self.agregarLabel()

            generator.addIf(newTemp, '1', '==', self.trueLabel)
            generator.addGoto(self.falseLabel)

            value.trueLabel = self.trueLabel
            value.falseLabel = self.falseLabel

            return value

#JAJAJA NO SE QUE HACER PQ AAAAM QUIERO TENER EL VALOR NO EL TEMPORAL JEJE

 
    def getNode(self):
        return super().getNode()

    def agregarLabel(self, generator):
        if self.trueLabel == None:
            self.trueLabel = generator.newLabel()

        if self.falseLabel == None:
            self.falseLabel = generator.newLabel()