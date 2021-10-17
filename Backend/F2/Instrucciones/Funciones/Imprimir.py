from Abstract.Instruccion import Instruccion
from TS.Tipo import Tipo

class Imprimir(Instruccion):
    def __init__(self, expresiones, saltoLinea, fila, columna):
        self.expresiones = expresiones
        self.saltoLinea = saltoLinea
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        self.expresiones.generador = self.generador
        tempValue = self.expresiones.interpretar(tree, table)

        if tempValue.tipo == Tipo.ENTERO:
            self.generador.addPrint("d", "(int)" + str(tempValue.getValue()))
        elif tempValue.tipo == Tipo.DOBLE:
            self.generador.addPrint("f", "(double)" + str(tempValue.getValue()))
        else:
            print("ERROR")

        self.generador.addNewLine()      

    def getNode(self):
        return super().getNode()
