from typing import _SpecialForm
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
        if isinstance(self.expresiones, list): 
            for expresion in self.expresiones:
                self.print(expresion, tree, table, generator)

        else:
            tree.updateConsola(generator.newPrint("c", '00'))

        if self.saltoLinea:
            tree.updateConsola(generator.newNewLine())   

        return None   

    def getNode(self):
        return super().getNode()

    def print(self, expresion, tree, table, generator):
        tempValor = expresion.interpretar(tree, table, generator)
        if isinstance(tempValor, Excepcion):
            return tempValor

        if tempValor.tipo == Tipo.ENTERO:     
            tree.updateConsola(generator.newPrint("d", "int(" + str(tempValor.getValor()) + ")"))
            
        elif tempValor.tipo == Tipo.DOBLE:
            tree.updateConsola(generator.newPrint("f", str(tempValor.getValor())))
            
        elif tempValor.tipo == Tipo.BANDERA:
            trueIns = generator.newCallFunc('print_true_armc')
            falseIns = generator.newCallFunc('print_false_armc')
            tree.updateConsola(generator.newOpRelacional(tempValor, trueIns, falseIns))
        elif tempValor.tipo == Tipo.CADENA:
            tree.updateConsola(generator.newPrint("c", str(tempValor.getValor())))
            
        else:
            print("ERROR")
