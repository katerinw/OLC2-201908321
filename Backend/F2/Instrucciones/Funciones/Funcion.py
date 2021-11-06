from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
#from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Value import Value
from TS.Tipo import Tipo

class Funcion(Instruccion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
        self.size = 0
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table, generator):
        nuevaTabla = TablaSimbolos('function', table)

        tamanoTabla = nuevaTabla.size  #Guardando el valor del tamano de todos los entornos
        nuevaTabla.changeOwnSize(1)    #Sumandole 1 del return 
        nuevaTabla.size = nuevaTabla.ownSize  #Asignandole cero a la nueva tabla pq asi la funcion empieza de cero  
        
        tree.updateConsolaln("\nfunc " + self.identificador + "(){")

        for parametro in self.parametros:
            tamTabla = nuevaTabla.size #Tamano de tabla jeje
            #Creacion de simbolo e ingresandolo a la tabla de simbolos
            value = self.returnValueType(parametro['tipo']) #Solo poniendo un valor aleatorio para ver si cumple con los requisitos
            simbolo = Simbolo(parametro['identificador'], parametro['tipo'], value, tamTabla, False, False, self.fila, self.columna)
            resultTable = nuevaTabla.setTabla(simbolo)
            if isinstance(resultTable, Excepcion):
                return resultTable

        
        for instruccion in self.instrucciones:
            value = instruccion.interpretar(tree, nuevaTabla, generator) #Devuelve el nodo del resultado de la funcion si es un return
            if isinstance(value, Excepcion):
                tree.getExcepciones().append(value)
                tree.updateConsolaln(value.toString())
            if isinstance(value, Continue):
                err = Excepcion("Semántico", "Sentencia CONTUNUE fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                tree.updateConsolaln(err.toString())
            if isinstance(value, Break):
                err = Excepcion("Semántico", "Sentencia BREAK fuera de ciclo", instruccion.fila, instruccion.columna)
                tree.getExcepciones().append(err)
                tree.updateConsolaln(err.toString())
            if isinstance(value, Return):
                self.tipo = Tipo.ENTERO
                nuevaTabla.changeOwnSize(1) #Aumenta el tamano del entorno con el return
                #self.tipo = value.tipo
                #return value.result
        
        self.tipo = Tipo.NULO
        tree.updateConsolaln("}")

        nuevaTabla.size = tamanoTabla #Regresando el valor de la tabla a su valor actual
        
        return "Nothing"

    def getNode(self):
        return super().getNode()

    def returnValueType(self, tipo):
        if tipo == Tipo.ENTERO:
            return Value(1, '', tipo, False)
        elif tipo == Tipo.DOBLE:
            return Value(1.0, '', tipo, False)
        elif tipo == Tipo.BANDERA:
            return Value(True, '', tipo, False)
        elif tipo == Tipo.CARACTER:
            return Value('', '', tipo, False)
        elif tipo == Tipo.CADENA:
            return Value('', '', tipo, False)
