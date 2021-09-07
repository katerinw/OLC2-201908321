from TS.Tipo import Tipo
from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.TablaSimbolos import TablaSimbolos

class While(Instruccion):
    def __init__(self, condicion, instrucciones, fila, columna):
        self.instrucciones = instrucciones
        self.condicion = condicion
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        while True:
            condicion = self.condicion.interpretar(tree, table)
            if isinstance(condicion, Excepcion):
                return condicion

            if self.condicion.tipo == Tipo.BANDERA:
                if condicion == True: #Verifica en cada ciclo que la condicion sea verdadera
                    nuevaTabla = TablaSimbolos(table)
                    for instruccion in self.instrucciones:
                        result = instruccion.interpretar(tree, nuevaTabla)
                        if isinstance(result, Excepcion):
                            tree.getExcepciones().append(result)
                            tree.updateConsolaln(result.toString())

                elif condicion == False:
                    break
            else:
                return Excepcion("Semántico", "La condición de While no es tipo boolean", self.fila, self.columna)


        