from Expresiones.Primitivos.NegativeValue import NegativeValue
from Expresiones.Relacionales.Diferente import Diferente
from Expresiones.Primitivos.Temporal import Temporal
from Instrucciones.Funciones.Funcion import Funcion
#from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class PrintString(Funcion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table, generator):
        #print("ES LLAMADA FUNCION")
        tree.updateConsola("func Print_String_armc(){\n")


        newTempUno = generator.createTemp()
        tree.updateConsola(generator.newExpresion(newTempUno, 'P', '1', '+'))
        
        newTempDos = generator.createTemp()
        tree.updateConsola(generator.newGetStack(newTempDos, newTempUno))

        newTempTres = generator.createTemp()

        newLabel = generator.createLabel()
        tree.updateConsola(generator.newLabel(newLabel))

        tree.updateConsola(generator.newGetHeap(newTempTres, newTempDos))

        valor = Value(None, newTempTres, Tipo.ENTERO, True)

        #Sacando opIzq y opDer
        operadorDerecho = NegativeValue(1, Tipo.ENTERO, self.fila, self.columna)
        operadorIzquierdo = Temporal(valor, self.fila, self.columna)
        diferente = Diferente(operadorIzquierdo, operadorDerecho, self.fila, self.columna)
        diferente.interpretar(tree, table, generator)

        tree.updateConsola(generator.newLabel(diferente.trueLabel))
        tree.updateConsola(generator.newPrint('c', 'int('+newTempTres+')'))
        tree.updateConsola(generator.newExpresion(newTempDos, newTempDos, '1', '+'))
        tree.updateConsola(generator.newGoto(newLabel))

        tree.updateConsola(generator.newLabel(diferente.falseLabel))




        tree.updateConsola("}")
        

    def getNode(self):
        return super().getNode()