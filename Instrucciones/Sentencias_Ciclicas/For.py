from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import Tipo

class For(Instruccion):
    def __init__(self, identificador, expresionIzq, expresionDer, instrucciones, fila, columna):
        self.identificador = identificador
        self.expresionIzq = expresionIzq
        self.expresionDer = expresionDer
        self.instrucciones = instrucciones
        self.fila = fila 
        self.columna = columna

    def interpretar(self, tree, table):
        nuevaTablaIntermedia = TablaSimbolos(table)
        Identificador = self.identificador.interpretar(tree, nuevaTablaIntermedia) #Solo se encarga 
        if isinstance(Identificador, Excepcion): #de meter la variable en la tabla, pq
            return Identificador #retorna None jeje

        Identificador = self.identificador.identificador #Asigane el nombre del id

        expIzq = self.expresionIzq.interpretar(tree, table)
        if isinstance(expIzq, Excepcion):
            return expIzq

        if self.expresionDer != None:
            expDer = self.expresionDer.interpretar(tree, table)
            if isinstance(expDer, Excepcion):
                return expDer 
            if expIzq>expDer:
                return Excepcion("Semántico", "El rango izquierdo no puede ser mayor al derecho", self.fila, self.columna)

        if self.expresionIzq.tipo == Tipo.CADENA:  #Para cadenas
            for iterador in expIzq:
                simbolo = Simbolo(str(Identificador), Tipo.CARACTER, iterador, True, False, self.fila, self.columna)
                nuevaTablaIntermedia.actualizarTabla(simbolo)
                nuevaTabla = TablaSimbolos(nuevaTablaIntermedia)
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

        elif self.expresionIzq.tipo == Tipo.ENTERO and self.expresionDer.tipo == Tipo.ENTERO: #Para rangos en numeros
            for iterador in range(expIzq,expDer+1):
                simbolo = Simbolo(str(Identificador), Tipo.ENTERO, iterador, True, False, self.fila, self.columna)
                nuevaTablaIntermedia.actualizarTabla(simbolo)
                nuevaTabla = TablaSimbolos(nuevaTablaIntermedia)
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
        

        return None
                