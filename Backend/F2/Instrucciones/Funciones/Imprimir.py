from Expresiones.Relacionales.Diferente import Diferente
from Expresiones.Aritmeticas.Division import Division
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo


class Imprimir(Instruccion):
    def __init__(self, expresiones, saltoLinea, fila, columna):
        self.expresiones = expresiones
        self.saltoLinea = saltoLinea
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        tempValor = self.expresiones.interpretar(tree, table, generator)
        if isinstance(tempValor, Excepcion):
            return tempValor

        if tempValor.tipo == Tipo.ENTERO:     
            generator.addPrint("d", "int(" + str(tempValor.getValor()) + ")")
        
        elif tempValor.tipo == Tipo.DOBLE:
            generator.addPrint("f", str(tempValor.getValor()))
        
        elif tempValor.tipo == Tipo.BANDERA:
            trueIns = generator.newCallFunc('print_true_armc')
            falseIns = generator.newCallFunc('print_false_armc')
            generator.addOpRelacional(tempValor, trueIns, falseIns)
        else:
            print("ERROR")

        generator.addNewLine()      

    def getNode(self):
        return super().getNode()
