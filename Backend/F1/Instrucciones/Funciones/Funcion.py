from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo


class Funcion(Instruccion):
    def __init__(self, identificador, parametros, instrucciones, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.instrucciones = instrucciones
        self.tipo = Tipo.NULO
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTabla = TablaSimbolos('function', table)
        for instruccion in self.instrucciones:
            value = instruccion.interpretar(tree, nuevaTabla) #Devuelve el nodo del resultado de la funcion si es un return
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
                self.tipo = value.tipo
                return value.result

        self.tipo = Tipo.NULO
        return "Nothing"

    def getNode(self):
        nodo = NodeCst("funciones_instr")
        nodo.addChild(str(self.identificador))

        if self.parametros != None:
            parametrosNodo = NodeCst("parametros")
            for param in self.parametros:
                parametroNodo = NodeCst("parametro")
                parametroNodo.addChild(str(self.tipoDato(param['tipo'])))
                idNodo = NodeCst("expresion")
                idNodo.addChild(str(param['identificador']))
                parametroNodo.addChildNode(idNodo)
                parametrosNodo.addChildNode(parametroNodo)
            nodo.addChildNode(parametrosNodo)

        instruccionesNodo = NodeCst("instrucciones")
        for instruccion in self.instrucciones:
            instruccionesNodo.addChildNode(instruccion.getNode())
        nodo.addChildNode(instruccionesNodo)

        return nodo

    def tipoDato(self, tipo):
        if tipo == Tipo.BANDERA:
            return "Bool"
        elif tipo == Tipo.CADENA:
            return "String"
        elif tipo == Tipo.CARACTER:
            return "Char"
        elif tipo == Tipo.DOBLE:
            return "Float64"
        elif tipo == Tipo.ENTERO:
            return "Int64"
        elif tipo == Tipo.NULO:
            return "Nothing"
