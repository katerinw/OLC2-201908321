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
        tree.updateConsola("func Print_String_armc(){\n")

        newTempIndiceParametro = generator.createTemp() 
        tree.updateConsola(generator.newExpresion(newTempIndiceParametro, 'P', '1', '+')) #Tiene el indice del parametro depositado
        
        newTempValorIndiceHeap = generator.createTemp()
        tree.updateConsola(generator.newGetStack(newTempValorIndiceHeap, newTempIndiceParametro)) #Accede al valor del parametro

        newLabel = generator.createLabel()
        tree.updateConsola(generator.newLabel(newLabel))

        newTempValorHeap = generator.createTemp()
        tree.updateConsola(generator.newGetHeap(newTempValorHeap, newTempValorIndiceHeap))

        valor = Value(None, newTempValorHeap, Tipo.ENTERO, True)

        #Sacando opIzq y opDer
        operadorDerecho = NegativeValue(1, Tipo.ENTERO, self.fila, self.columna)
        operadorIzquierdo = Temporal(valor, self.fila, self.columna)
        diferente = Diferente(operadorIzquierdo, operadorDerecho, self.fila, self.columna).interpretar(tree, table, generator)

        tree.updateConsola(generator.newLabel(diferente.trueLabel))
        tree.updateConsola(generator.newPrint('c', 'int('+newTempValorHeap+')'))
        tree.updateConsola(generator.newExpresion(newTempValorIndiceHeap, newTempValorIndiceHeap, '1', '+'))
        tree.updateConsola(generator.newGoto(newLabel))

        tree.updateConsola(generator.newLabel(diferente.falseLabel))

        tree.updateConsola(generator.newReturn())
        tree.updateConsola("}")
        

    def getNode(self):
        return super().getNode()