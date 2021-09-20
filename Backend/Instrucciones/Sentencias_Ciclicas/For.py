from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import Tipo
from copy import copy

class For(Instruccion):
    def __init__(self, identificador, expresionIzq, expresionDer, instrucciones, fila, columna):
        self.identificador = identificador
        self.expresionIzq = expresionIzq
        self.expresionDer = expresionDer
        self.instrucciones = instrucciones
        self.fila = fila 
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTablaIntermedia = TablaSimbolos('fordeclaration', table)
        Identificador = self.identificador.interpretar(tree, nuevaTablaIntermedia) #Solo se encarga 
        if isinstance(Identificador, Excepcion): #de meter la variable en la tabla, pq
            return Identificador #retorna None jeje

        Identificador = self.identificador.identificador #Asigane el nombre del id


        if isinstance(self.expresionIzq, list):
            expIzq = copy(self.expresionIzq)
            self.copiarArreglo(expIzq, self.expresionIzq)
            val = self.interpretarArreglos(tree, table, expIzq)
            if isinstance(val, Excepcion):
                return val
            expresionIzqTipo = Tipo.ARREGLO
        else:
            expIzq = self.expresionIzq.interpretar(tree, table)
            if isinstance(expIzq, Excepcion):
                return expIzq
            expresionIzqTipo = self.expresionIzq.tipo


        if self.expresionDer != None:
            expDer = self.expresionDer.interpretar(tree, table)
            if isinstance(expDer, Excepcion):
                return expDer 
            
            if self.expresionIzq.tipo == Tipo.ENTERO and self.expresionDer.tipo == Tipo.ENTERO:
                if expIzq>expDer:
                    return Excepcion("Semántico", "El rango izquierdo no puede ser mayor al derecho", self.fila, self.columna)
            else:
                return Excepcion("Semántico", "Los parametros de rango no son tipo Entero", self.fila, self.columna)


        if expresionIzqTipo == Tipo.CADENA or expresionIzqTipo == Tipo.ARREGLO or expresionIzqTipo == Tipo.CARACTER:  #Para cadenas
            for iterador in expIzq:
                simbolo = Simbolo(str(Identificador), self.tipoDato(iterador), iterador, True, False, self.fila, self.columna)
                nuevaTablaIntermedia.actualizarTabla(simbolo)
                nuevaTabla = TablaSimbolos('for', nuevaTablaIntermedia)
                for instruccion in self.instrucciones:
                    result = instruccion.interpretar(tree, nuevaTabla)

                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsolaln(result.toString())
                        
                    if isinstance(result, Return): #Sentencia Return  
                        return result.expresion
                        
                    if isinstance(result, Break): #Sentencia Break
                        return None

                    if isinstance(result, Continue):
                        break

        elif expresionIzqTipo == Tipo.ENTERO and self.expresionDer.tipo == Tipo.ENTERO: #Para rangos en numeros
            for iterador in range(expIzq,expDer+1):
                simbolo = Simbolo(str(Identificador), Tipo.ENTERO, iterador, True, False, self.fila, self.columna)
                nuevaTablaIntermedia.actualizarTabla(simbolo)
                nuevaTabla = TablaSimbolos('for',nuevaTablaIntermedia)
                for instruccion in self.instrucciones:
                    result = instruccion.interpretar(tree, nuevaTabla)

                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsolaln(result.toString())
                        
                    if isinstance(result, Return): #Sentencia Return  
                        return result
                        
                    if isinstance(result, Break): #Sentencia Break
                        return None

                    if isinstance(result, Continue):
                        break
        
        return None


    def interpretarArreglos(self, tree, table, arreglo):
        i = 0
        while i < len(arreglo):
            if isinstance(arreglo[i], list):
                self.interpretarArreglos(tree, table, arreglo[i])
            else:
                valor = arreglo[i].interpretar(tree, table)
                if isinstance(valor, Excepcion):
                    return valor
                arreglo[i] = valor
            i += 1
        return None


    def copiarArreglo(self, valor, arreglo):
        i = 0
        while i < len(arreglo):
            if isinstance(arreglo[i], list):
                valor[i] = copy(arreglo[i])
            else:
                valor[i] = copy(arreglo[i])
            i += 1
        return None 

    def tipoDato(self, value):
        if isinstance(value, int):
            return Tipo.ENTERO
        elif isinstance(value, float):
            return Tipo.DOBLE
        elif isinstance(value, str):
            return Tipo.CADENA
        elif isinstance(value, bool):
            return Tipo.BANDERA
        elif isinstance(value, list):
            return Tipo.ARREGLO
