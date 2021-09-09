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
        
        if simboloVar != None:  #Verifica si la variable ya fue declarada
            if simboloVar.local and self.globall: #Verifica que no haya una variable local antes de declarar una global
                return Excepcion("Semántico", "No se puede declarar una variable global donde ya existe una variable local", self.fila, self.columna)
            
        value = "" # declara value vacia
        if self.valor != None: #Verifica que si venga un valor
            value = self.valor.interpretar(tree, table)
            if isinstance(value, Excepcion):
                return value

            if self.tipo == None: #Verifica si la variable trae tipo o no
                self.tipo = self.valor.tipo #Le pone el tipo de la variable al tipo
            
            if self.valor.tipo != self.tipo: #Verifica que la variable sea del mismo tipo
                return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna) 
        
        if self.local:  #Se encarga de las variables locales jeje
            if self.valor != None:  #Si trae valor para ponerle valor jsjs     
                simbolo = Simbolo(str(self.identificador), self.valor.tipo, value, True, False, self.fila, self.columna)
            else: #Si no trae valor jsjsj
                simbolo = Simbolo(str(self.identificador), simboloVar.tipo, simboloVar.valor, True, False, self.fila, self.columna)
             
        elif self.globall:  #Se encarga de las variables globales
            if self.valor != None: #Si la variable trae valor
                simbolo = Simbolo(str(self.identificador), self.valor.tipo, value, False, True, self.fila, self.columna)

                if simboloVar == None: #Verifica si la variable no estaba declarada anteriormente de modo global
                    simboloGlobal = Simbolo(str(self.identificador), self.valor.tipo, value, False, False, self.fila, self.columna)
                    resultGlobal = tree.getTSGlobal().setTable(simboloGlobal)  #Ingresa el simbolo al entorno global
                    if isinstance(resultGlobal, Excepcion):
                        return resultGlobal
                else:  #Verifica si la variable ya estaba declarada anteriormente de modo global
                    resultGlobal = tree.getTSGlobal().actualizarTabla(simbolo) #Actualiza el simbolo al entorno global
                    if isinstance(resultGlobal, Excepcion):
                        return resultGlobal
            else: #Si la variable no trae valor
                simbolo = Simbolo(str(self.identificador), None, None, False, True, self.fila, self.columna)
                
                if simboloVar == None: #Verifica si la variable no estaba declarada anteriormente de modo global
                    simboloGlobal = Simbolo(str(self.identificador), None, None, False, False, self.fila, self.columna)
                    resultGlobal = tree.getTSGlobal().setTable(simboloGlobal)  #Ingresa el simbolo al entorno global
                    if isinstance(resultGlobal, Excepcion):
                        return resultGlobal
                else:  #Verifica si la variable ya estaba declarada anteriormente de modo global
                    simbolo = Simbolo(str(self.identificador), simboloVar.tipo, simboloVar.valor, False, True, self.fila, self.columna)

        result = table.setTabla(simbolo)  #pos namas estamos mandando el identificador a la tablita jeje
        if isinstance(result, Excepcion):
            return result

        return None