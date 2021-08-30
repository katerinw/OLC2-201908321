from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Imprimir(Instruccion):
    def __init__(self, expresion, saltoLinea, fila, columna):
        self.expresion = expresion
        self.saltoLinea = saltoLinea
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        valor = self.expresion.interpretar(tree, table) #Retorna cualquier valor interpretado

        if isinstance(valor, Excepcion):
            return valor

        if self.expresion.tipo == Tipo.ARREGLO:
            return Excepcion("Semántico", "No se puede imprimirun arreglo completo", self.fila, self.columna)

        if(self.saltoLinea == True):
            tree.updateConsolaln(valor)
        else:
            tree.updateConsola(valor)
        return None