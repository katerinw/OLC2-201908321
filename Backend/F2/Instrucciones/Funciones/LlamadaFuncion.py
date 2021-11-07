#from Instrucciones.Arreglos.AccesoArreglo import AccesoArreglo
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
#from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Value import Value
from TS.Tipo import Tipo


class LlamadaFuncion(Instruccion):
    def __init__(self, identificador, parametros, fila, columna):
        self.identificador = identificador
        self.parametros = parametros
        self.fila = fila
        self.columna = columna
        self.tipo = Tipo.NULO

    def interpretar(self, tree, table, generator):
        funcion = tree.getFuncion(str(self.identificador))
        struct = 'tree.getStruct(str(self.identificador))'

        if funcion != None: #Para las funciones
            nuevaTabla = TablaSimbolos('functioncall',tree.getTSGlobal()) #cambiar

            if len(funcion.parametros) != len(self.parametros):
                return Excepcion("Semántico", "Cantidad de parámetros incorrecta en función \""+self.identificador+"\"", self.fila, self.columna)

            tamTabla = nuevaTabla.size
            newTemp = generator.createTemp()                                #Temp cambio simulado de ambito
            tree.updateConsola(generator.newSimulateNextStack(newTemp, str(tamTabla))) #Cambio simulado de ambito           

            contador = 0
            for expresion in self.parametros:
                newTempIndice = generator.createTemp()                                #Temp cambio simulado de ambito
                tree.updateConsola(generator.newExpresion(newTempIndice, newTemp, str(contador+1), '+')) #Cambio simulado de ambito           


                resultExpresion = expresion.interpretar(tree, nuevaTabla, generator) #cambio
                if isinstance(resultExpresion, Excepcion):
                    return resultExpresion

                #Para poder capturar el tipo de dato de la variable y asi no modificar el verdadero sino el momentaneo jeje
                if funcion.parametros[contador]['identificador'].lower() == 'truncate$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'typeof$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'sin$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'cos$$parametros123' or funcion.parametros[contador]['identificador'].lower() == 'tan$$parametros123':
                    funcion.parametros[contador]['tipo'] = expresion.tipo

                if funcion.parametros[contador]['tipo'] != expresion.tipo and funcion.parametros[contador]['tipo'] != None: #Verifica que los parametros sean del mismo tipo
                    return Excepcion("Semántico", "Tipo de dato diferente en parámetros en la función \""+self.identificador+"\"", self.fila, self.columna)

                
                value = self.correctValue(resultExpresion)
                tree.updateConsola(generator.newSetStack(newTempIndice, str(value)))
                contador += 1


            tree.updateConsola(generator.newNextStack(str(tamTabla)))  #Cambia de ambito
            tree.updateConsola(generator.newCallFunc(self.identificador)) #Llama a la funcion

            newTempIndiceReturn = generator.createTemp()
            tree.updateConsola(generator.newExpresion(newTempIndiceReturn, 'P', '0', '+'))
            
            newTempValorReturn = generator.createTemp()    #Tiene el valor de return 
            tree.updateConsola(generator.newGetStack(newTempValorReturn, newTempIndiceReturn))

            tree.updateConsola(generator.newBackStack(str(tamTabla)))  #Regresa en el ambito

            self.tipo = funcion.tipo

            valor = Value('', newTempValorReturn, self.tipo, True) #Retornando temporal
            return valor

        elif struct != None: #Para las structs
            pass

        elif struct == None and funcion == None: #Por si no existe nada jsjs
            return Excepcion("Semántico", "Struct/Funcion \""+self.identificador+"\" no encontrado", self.fila, self.columna)


    def getNode(self):
        return super().getNode()

    def correctValue(self, valor):
        if valor.isTemp:
            return valor.getTemporal()
        else:
            return valor.getValor()