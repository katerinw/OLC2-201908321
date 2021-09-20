from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class Imprimir(Instruccion):
    def __init__(self, expresiones, saltoLinea, fila, columna):
        self.expresiones = expresiones
        self.saltoLinea = saltoLinea
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        valores = ""
        if self.expresiones != None:
            for expresion in self.expresiones:
                valor = expresion.interpretar(tree, table) #Retorna cualquier valor interpretado
                if isinstance(valor, Excepcion):
                    return valor
                valores += str(valor)
        elif self.expresiones == None and self.saltoLinea == True:
            valores = "\n"
                
        if(self.saltoLinea == True):
            tree.updateConsolaln(valores)
        else:
            tree.updateConsola(valores)
        return None