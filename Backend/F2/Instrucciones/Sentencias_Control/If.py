from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo

class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.ElseIf = ElseIf
        self.fila = fila
        self.columna = columna


    def interpretar(self, tree, table, generator, etiqueta=None):
        ifOriginal = False
        if etiqueta == None:
            newLabel = generator.createLabel()
            etiqueta = newLabel
            ifOriginal = True

        condicion = self.condicion.interpretar(tree, table, generator)
        if isinstance(condicion, Excepcion):
            return condicion

        if self.condicion.tipo != Tipo.BANDERA:
            return Excepcion("Semántico", "Tipo de dato no bool en sentencia de control If", self.fila, self.columna)

        tree.updateConsola(generator.newLabel(condicion.trueLabel))
        for instruccion in self.instruccionesIf:
            resultIf = instruccion.interpretar(tree, table, generator)
            if isinstance(resultIf, Excepcion):
                return resultIf
            if isinstance(resultIf, Continue):
                return resultIf
            if isinstance(resultIf, Return):
                return resultIf
            if isinstance(resultIf, Break):
                return resultIf

        tree.updateConsola(generator.newGoto(etiqueta))
        tree.updateConsola(generator.newLabel(condicion.falseLabel))

        if self.ElseIf:
            for elseIf in self.ElseIf:
                resultElseIf = elseIf.interpretar(tree, table, generator, etiqueta)
                if isinstance(resultElseIf, Excepcion):
                    return resultElseIf
                if isinstance(resultElseIf, Continue):
                    return resultElseIf
                if isinstance(resultElseIf, Return):
                    return resultElseIf
                if isinstance(resultElseIf, Break):
                    return resultElseIf 

        if self.instruccionesElse:
            for elsee in self.instruccionesElse:
                resultElse = elsee.interpretar(tree, table, generator)
                if isinstance(resultElse, Excepcion):
                    return resultElse
                if isinstance(resultElse, Continue):
                    return resultElse
                if isinstance(resultElse, Return):
                    return resultElse
                if isinstance(resultElse, Break):
                    return resultElse
            tree.updateConsola(generator.newGoto(etiqueta))

        if ifOriginal:
            tree.updateConsola(generator.newLabel(etiqueta))

         



        


        
        
        



    def getNode(self):
        return super().getNode()