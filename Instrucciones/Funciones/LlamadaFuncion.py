from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo

class LlamadaFuncion(Instruccion):
    def __init__(self, identificador, parametros, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.fila = fila
        self.columna  = columna

    def interpretar(self, tree, table):
        funcion = tree.getFuncion(self.identificador)
        if funcion == None:
            return Excepcion("Semántico", "Función \""+self.identificador+"\" no encontrada", self.fila, self.columna)

        nuevaTabla = TablaSimbolos(tree.getTSGlobal()) #cambiar

        if len(funcion.parametros) != len(self.parametros):
            return Excepcion("Semántico", "Cantidad de parámetros incorrecta en función \""+self.identificador+"\"", self.fila, self.columna)

        contador = 0
        for expresion in self.parametros:
            resultExpresion = expresion.interpretar(tree, table) #cambio
            if isinstance(resultExpresion, Excepcion):
                return resultExpresion
            
            #Para poder capturar el tipo de dato de la variable y asi no modificar el verdadero sino el momentaneo jeje
            if funcion.parametros[contador]['identificador'].lower() == 'truncate$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'typeof$$parametros123':
                funcion.parametros[contador]['tipo'] = expresion.tipo

            if funcion.parametros[contador]['tipo'] != expresion.tipo and funcion.parametros[contador]['tipo'] != None: #Verifica que los parametros sean del mismo tipo
                return Excepcion("Semántico", "Tipo de dato diferente en parámetros en la función \""+self.identificador+"\"", self.fila, self.columna)

            #Creacion de simbolo e ingresandolo a la tabla de simbolos
            if funcion.parametros[contador]['tipo'] == None:
                simbolo = Simbolo(funcion.parametros[contador]['identificador'], expresion.tipo, resultExpresion, False, False, self.fila, self.columna)
            else:
                simbolo = Simbolo(funcion.parametros[contador]['identificador'], funcion.parametros[contador]['tipo'], resultExpresion, False, False, self.fila, self.columna)
            
            resultTable = nuevaTabla.setTabla(simbolo)
            if isinstance(resultTable, Excepcion):
                return resultTable

            contador += 1

        value = funcion.interpretar(tree, nuevaTabla)
        if isinstance(value, Excepcion):
            return value
        
        self.tipo = funcion.tipo
        return value
        