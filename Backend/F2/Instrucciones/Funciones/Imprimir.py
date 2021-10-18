from Abstract.Instruccion import Instruccion
from TS.Tipo import Tipo

class Imprimir(Instruccion):
    def __init__(self, expresiones, saltoLinea, fila, columna):
        self.expresiones = expresiones
        self.saltoLinea = saltoLinea
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        tempValor = self.expresiones.interpretar(tree, table, generator)

        if tempValor.tipo == Tipo.ENTERO:
            generator.addPrint("d", "(int)" + str(tempValor.getValor()))
        elif tempValor.tipo == Tipo.DOBLE:
            generator.addPrint("f", "(double)" + str(tempValor.getValor()))
        elif tempValor.tipo == Tipo.BANDERA:
            newLabel = generator.newLabel()
            generator.addLabel(str(tempValor.trueLabel))
            generator.addGoto(str(newLabel))
            generator.addLabel(str(tempValor.falseLabel))
            generator.addLabel(str(newLabel))
        else:
            print("ERROR")

        generator.addNewLine()      

    def getNode(self):
        return super().getNode()
