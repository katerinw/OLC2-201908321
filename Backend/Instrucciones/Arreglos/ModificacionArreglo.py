from os import execv
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from copy import copy

class ModificacionArreglo(Instruccion):
    def __init__(self, identificador, dimensiones, expresiones, fila, columna):
        self.identificador = identificador
        self.dimensiones = dimensiones
        self.expresiones = expresiones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        if isinstance(self.expresiones, list):
            value = self.interpretarArreglos(tree, table, self.expresiones)
            if isinstance(value, Excepcion):
                return value
            value = self.expresiones
        else:
            value = self.expresiones.interpretar(tree, table)

        simbolo = table.getTabla(str(self.identificador))
        if simbolo == None:
            return Excepcion("Semántico", "Arreglo \""+self.identificador+"\" no encontrado", self.fila, self.columna)

        if simbolo.getTipo() != Tipo.ARREGLO:
            return Excepcion("Semántico", "La varible \""+str(self.identificador)+"\" a la que intenta acceder no es un arreglo", self.fila, self.columna)

        valueResult = self.modify(tree, table, copy(self.dimensiones), simbolo.getValor(), value)
        if isinstance(valueResult, Excepcion):
            return valueResult
        
        return valueResult


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


    def modify(self, tree, table, dimensiones, arreglo, valor):
        if len(dimensiones) == 0:
            if isinstance(arreglo, list):
                return Excepcion("Semántico", "Acceso de mas en un arreglo", self.fila, self.columna)
            return valor
        
        if not(isinstance(arreglo, list)):
            return Excepcion("Semántico", "Acceso de mas en un arreglo", self.fila, self.columna)

        dimension = dimensiones.pop(0)
        
        num = dimension.interpretar(tree, table)
        if isinstance(num, Excepcion):
            return num
        
        if num == 0:
            return Excepcion("Semántico", "Indice en arreglo \""+self.identificador+"\" fuera de rango", self.fila, self.columna)

        
        if dimension.tipo != Tipo.ENTERO:
            return Excepcion("Semántico", "Expresion diferente a ENTERO en Arreglo", self.fila, self.columna)

        try:
            valor = self.modify(tree, table, copy(dimensiones), arreglo[num-1], valor)
        except:
            return Excepcion("Semántico", "Indice en arreglo \""+self.identificador+"\" fuera de rango", self.fila, self.columna)

        if isinstance(valor, Excepcion):
            return valor

        if valor != None:
            arreglo[num-1] = valor

        return None