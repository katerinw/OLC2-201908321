from Abstract.Instruccion import Instruccion
from TS.Tipo import Tipo

class Imprimir(Instruccion):
    def __init__(self, expresiones, saltoLinea, fila, columna):
        self.expresiones = expresiones
        self.saltoLinea = saltoLinea
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        tempValue = self.expresiones.interpretar(tree, table, generator)

        if self.expresiones.tipo == Tipo.ENTERO:
            generator.addPrint("d", "(int)" + str(tempValue))
        elif self.expresiones.tipo == Tipo.DOBLE:
            generator.addPrint("f", "(double)" + str(tempValue))
        else:
            print("ERROR")

        generator.addNewLine()      

    def getNode(self):
        return super().getNode()
