from Instrucciones.Arreglos.AccesoArreglo import AccesoArreglo
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import Tipo

class LlamadaFuncionStruct(Instruccion):
    def __init__(self, identificador, parametros, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.fila = fila
        self.columna  = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table):
        funcion = tree.getFuncion(str(self.identificador))
        struct = tree.getStruct(str(self.identificador))

        if funcion != None: #Para las funciones
            nuevaTabla = TablaSimbolos('functioncall',tree.getTSGlobal()) #cambiar

            if len(funcion.parametros) != len(self.parametros):
                return Excepcion("Semántico", "Cantidad de parámetros incorrecta en función \""+self.identificador+"\"", self.fila, self.columna)

            contador = 0
            for expresion in self.parametros:
                resultExpresion = expresion.interpretar(tree, table) #cambio
                if isinstance(resultExpresion, Excepcion):
                    return resultExpresion

                #Para poder capturar el tipo de dato de la variable y asi no modificar el verdadero sino el momentaneo jeje
                if funcion.parametros[contador]['identificador'].lower() == 'truncate$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'typeof$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'sin$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'cos$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'tan$$parametros123':
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

        elif struct != None: #Para las structs
            nuevaTabla = TablaSimbolos(str(self.identificador), table)

            if len(struct.atributos) != len(self.parametros):
                return Excepcion("Semántico", "Cantidad de parámetros incorrecta para struct \""+self.identificador+"\"", self.fila, self.columna)

            contador = 0
            for expresion in self.parametros:
                resultExpresion = expresion.interpretar(tree, table)
                if isinstance(resultExpresion, Excepcion):
                    return resultExpresion

                if struct.atributos[contador]['tipo'] != expresion.tipo and struct.atributos[contador]['tipo'] != None: #Verifica que los parametros sean del mismo tipo
                    return Excepcion("Semántico", "Tipo de dato diferente en parámetros en la función \""+self.identificador+"\"", self.fila, self.columna)

                #Creacion de simbolo e ingresandolo a la tabla de simbolos
                if struct.atributos[contador]['tipo'] == None:
                    simbolo = Simbolo(struct.atributos[contador]['identificador'], expresion.tipo, resultExpresion, False, False, self.fila, self.columna)
                else:
                    simbolo = Simbolo(struct.atributos[contador]['identificador'], struct.atributos[contador]['tipo'], resultExpresion, False, False, self.fila, self.columna)
                
                resultTable = nuevaTabla.setTabla(simbolo)
                if isinstance(resultTable, Excepcion):
                    return resultTable
                
                contador += 1

            self.tipo = struct.tipo
            valor = struct.interpretar(tree, nuevaTabla)
            if isinstance(valor, Excepcion):
                return valor
            return nuevaTabla

        elif struct == None and funcion == None: #Por si no existe nada jsjs
            return Excepcion("Semántico", "Struct/Funcion \""+self.identificador+"\" no encontrado", self.fila, self.columna)

        #def makeDictionary(self, valor, struct, s)