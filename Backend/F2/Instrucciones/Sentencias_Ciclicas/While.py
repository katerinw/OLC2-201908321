from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from TS.Excepcion import Excepcion
from TS.Value import Value
from TS.Tipo import Tipo

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.condicion = condicion
        self.instrucciones = instrucciones
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        newLabel = generator.createLabel()
        tree.updateConsola(generator.newLabel(newLabel))

        condicion = self.condicion.interpretar(tree, table, generator)
        if isinstance(condicion, Excepcion):
            return condicion

        if self.condicion.tipo != Tipo.BANDERA:
            return Excepcion("Semántico", "La condición de While no es tipo boolean", self.fila, self.columna)

        tree.updateConsola(generator.newLabel(condicion.trueLabel))
        nuevaTabla = TablaSimbolos('while', table)

        for instruccion in self.instrucciones:
            result = instruccion.interpretar(tree, nuevaTabla, generator)
            if isinstance(result, Excepcion):
                tree.getExcepciones().append(result)
                tree.updateConsolaln(result.toString())
                        
            if isinstance(result, Return): #Sentencia Return  
                return result
                        
            if isinstance(result, Break): #Sentencia Break
                return None

            if isinstance(result, Continue):
                break

        tree.updateConsola(generator.newGoto(newLabel))
        tree.updateConsola(generator.newLabel(condicion.falseLabel))

    def getNode(self):
        return super().getNode()