from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
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