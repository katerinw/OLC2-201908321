from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo

class DeclaracionVar(Instruccion):
    def __init__(self, identificador, valor, tipo, local, globall, fila, columna):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.local = local
        self.globall = globall
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
#AUN DEBES VALIDAR SI SOLO DECLARAN LA VARIABLE LOCAL PERO NO LE ASIGNAN VALOR Y LA USAN COMO CONTADOR
        simboloVar = table.getTabla(str(self.identificador))
        
        if simboloVar != None:
            if simboloVar.local and self.globall:
                return Excepcion("Semántico", "No se puede declarar una variable global donde ya existe una variable local", self.fila, self.columna)
            
        value = ""
        if self.valor != None:
            value = self.valor.interpretar(tree, table)
            if isinstance(value, Excepcion):
                return value
        
        if self.local:  #Se encarga de las variables locales jeje
            if self.valor != None:
                if self.tipo == None:
                    self.tipo = self.valor.tipo
                
                if self.valor.tipo != self.tipo:
                    return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna)

                simbolo = Simbolo(str(self.identificador), self.valor.tipo, value, True, False, self.fila, self.columna)
            else:
                simbolo = Simbolo(str(self.identificador), simboloVar.tipo, simboloVar.valor, True, False, self.fila, self.columna)
             

        elif self.globall:  #Se encarga de las variables globales
            if self.valor != None:
                if self.tipo == None:
                    self.tipo = self.valor.tipo
                
                if self.valor.tipo != self.tipo:
                    return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna)
                
                simbolo = Simbolo(str(self.identificador), self.valor.tipo, value, False, True, self.fila, self.columna)
                if simboloVar == None:
                    simboloGlobal = Simbolo(str(self.identificador), self.valor.tipo, value, False, False, self.fila, self.columna)
                    resultGlobal = tree.getTSGlobal().setTable(simboloGlobal)
                    if isinstance(resultGlobal, Excepcion):
                        return resultGlobal
                else:
                    resultGlobal = tree.getTSGlobal().actualizarTabla(simbolo)
                    if isinstance(resultGlobal, Excepcion):
                        return resultGlobal
            else:
                if simboloVar == None:
                    simboloGlobal = Simbolo(str(self.identificador), None, None, False, False, self.fila, self.columna)
                    resultGlobal = tree.getTSGlobal().setTable(simboloGlobal)
                    if isinstance(resultGlobal, Excepcion):
                        return resultGlobal

                    simbolo = Simbolo(str(self.identificador), None, None, False, True, self.fila, self.columna)

                else:
                    simbolo = Simbolo(str(self.identificador), simboloVar.tipo, simboloVar.valor, False, True, self.fila, self.columna)

        result = table.setTabla(simbolo)  #pos namas estamos mandando el identificador a la tablita jeje

        if isinstance(result, Excepcion):
            return result

        return None