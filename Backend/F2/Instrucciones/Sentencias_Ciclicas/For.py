from Instrucciones.Asignacion_Declaracion_Variables.DeclaracionVar import DeclaracionVar
from Instrucciones.Asignacion_Declaracion_Variables.AsignacionVar import AsignacionVar
from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Expresiones.Primitivos.Identificador import Identificador
from Expresiones.Relacionales.MenorIgual import MenorIgual
from Expresiones.Primitivos.IntValue import IntValue
from Expresiones.Aritmeticas.Suma import Suma
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo


class For(Instruccion):
    def __init__(self, identificador, expresionIzq, expresionDer, instrucciones, fila, columna):
        self.identificador = identificador
        self.expresionIzq = expresionIzq
        self.expresionDer = expresionDer
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna
    
    def interpretar(self, tree, table, generator):
        nuevaTablaIntermedia = TablaSimbolos('fordeclaration', table)

        if isinstance(self.expresionIzq, list):
            pass
        else:
            expIzq = self.expresionIzq.interpretar(tree, nuevaTablaIntermedia, generator)
            if isinstance(expIzq, Excepcion):
                return expIzq
            expresionIzqTipo = self.expresionIzq.tipo

        result = DeclaracionVar(self.identificador, self.expresionIzq, expresionIzqTipo, True, False, self.fila, self.columna).interpretar(tree, nuevaTablaIntermedia, generator)
        if isinstance(result, Excepcion):
            return result

        if self.expresionDer != None:
            expDer = self.expresionDer.interpretar(tree, nuevaTablaIntermedia, generator)
            if isinstance(expDer, Excepcion):
                return expDer 
            
            if self.expresionIzq.tipo == Tipo.ENTERO and self.expresionDer.tipo == Tipo.ENTERO:
                if expIzq.getValor()>expDer.getValor():
                    return Excepcion("Semántico", "El rango izquierdo no puede ser mayor al derecho", self.fila, self.columna)
            else:
                return Excepcion("Semántico", "Los parametros de rango no son tipo Entero", self.fila, self.columna)


        newLabel = generator.createLabel()
        tree.updateConsola(generator.newLabel(newLabel))

        if expresionIzqTipo == Tipo.CADENA or expresionIzqTipo == Tipo.ARREGLO or expresionIzqTipo == Tipo.CARACTER:  #Para cadenas
            pass
        elif expresionIzqTipo == Tipo.ENTERO and self.expresionDer.tipo == Tipo.ENTERO: #Para rangos en numeros
            identificador = Identificador(self.identificador, self.fila, self.columna)
            resultCondicion = MenorIgual(identificador, self.expresionDer, self.fila, self.columna).interpretar(tree, nuevaTablaIntermedia, generator)
            if isinstance(resultCondicion, Excepcion):
                return resultCondicion

            tree.updateConsola(generator.newLabel(resultCondicion.trueLabel))
            nuevaTabla = TablaSimbolos('for', nuevaTablaIntermedia)
            for instruccion in self.instrucciones:
                resultIns = instruccion.interpretar(tree, nuevaTabla, generator)
                if isinstance(resultIns, Excepcion):
                    tree.getExcepciones().append(resultIns)
                    tree.updateConsolaln(resultIns.toString())

                if isinstance(resultIns, Return): #Sentencia Return  
                    return resultIns
                            
                if isinstance(resultIns, Break): #Sentencia Break
                    return None

                if isinstance(resultIns, Continue):
                    break
                    
                uno = IntValue(1, Tipo.ENTERO, self.fila, self.columna)
                suma = Suma(identificador, uno, self.fila, self.columna)

                asignacion = AsignacionVar(self.identificador, suma, Tipo.ENTERO, self.fila, self.columna).interpretar(tree, nuevaTabla, generator)
                if isinstance(asignacion, Excepcion):
                    return asignacion

            tree.updateConsola(generator.newGoto(newLabel))
            tree.updateConsola(generator.newLabel(resultCondicion.falseLabel))

            

    def getNode(self):
        return super().getNode()
        