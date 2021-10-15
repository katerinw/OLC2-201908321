from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Sentencias_Transferencia.Return import Return
from Instrucciones.Sentencias_Transferencia.Break import Break
from Abstract.Instruccion import Instruccion
from TS.TablaSimbolos import TablaSimbolos
from Abstract.NodeCst import NodeCst
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from copy import copy

class If(Instruccion):
    def __init__(self, condicion, instruccionesIf, instruccionesElse, ElseIf, fila, columna):
        self.condicion = condicion 
        self.instruccionesIf = instruccionesIf
        self.instruccionesElse = instruccionesElse
        self.ElseIf = ElseIf
        self.fila = fila
        self.columna = columna
        self.estado = False

    def interpretar(self, tree, table):
        self.estado = False
        condicion = self.condicion.interpretar(tree, table)
        if isinstance(condicion, Excepcion):
            return condicion

        if self.condicion.tipo != Tipo.BANDERA:
            return Excepcion("Semántico", "Tipo de dato no bool en sentencia de control If", self.fila, self.columna)

        if condicion == True: #verifica si es verdadera la condicion
            #nuevaTabla = TablaSimbolos('if', table) #Nuevo entorno
            for instruccion in self.instruccionesIf:
                result = copy(instruccion).interpretar(tree, table)
                if isinstance(result, Excepcion):
                    tree.getExcepciones().append(result)
                    tree.updateConsola(result.toString())
                if isinstance(result, Continue):
                    return result
                if isinstance(result, Return):
                    return result
                if isinstance(result, Break):
                    return result
            return True
        else: 
            if self.ElseIf != None:
                for elseif in self.ElseIf:
                    result = copy(elseif).interpretar(tree, table)

                    if isinstance(result, Excepcion):
                        return result
                    if isinstance(result, Continue):
                        return result
                    if isinstance(result, Return):
                        return result
                    if isinstance(result, Break):
                        return result
                    
                    if result == True:
                        self.estado = result
                        return None

            if self.instruccionesElse != None and self.estado == False:
                #nuevaTabla = TablaSimbolos('else', table)
                for instruccion in self.instruccionesElse:
                    result = copy(instruccion).interpretar(tree, table)
                    if isinstance(result, Excepcion):
                        tree.getExcepciones().append(result)
                        tree.updateConsola(result.toString())
                    if isinstance(result, Continue):
                        return result
                    if isinstance(result, Return):
                        return result
                    if isinstance(result, Break):
                        return result         
                
    def getNode(self):
        nodo = NodeCst("if_instr")
        nodo.addChild("IF")
        nodo.addChildNode(self.condicion.getNode())

        instruccionesIfNodo = NodeCst("if_instr")
        for instruccion in self.instruccionesIf:
            instruccionesIfNodo.addChildNode(instruccion.getNode())
        nodo.addChildNode(instruccionesIfNodo)

        if self.instruccionesElse != None:
            instruccionesElseNodo = NodeCst("else_instr")
            for instruccion in self.instruccionesElse:
                instruccionesElseNodo.addChildNode(instruccion.getNode())
            nodo.addChildNode(instruccionesElseNodo)

        if self.ElseIf != None:
            instruccionesElseIfNodo = NodeCst("elseif_instr")
            for instruccion in self.ElseIf:
                instruccionesElseIfNodo.addChildNode(instruccion.getNode())
            nodo.addChildNode(instruccionesElseIfNodo)
        
        return nodo