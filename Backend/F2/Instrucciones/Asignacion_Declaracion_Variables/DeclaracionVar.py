from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Value import Value
from TS.Tipo import Tipo

class DeclaracionVar(Instruccion):
    def __init__(self, identificador, valor, tipo, local, globall, fila, columna):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.local = local
        self.globall = globall
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        #AUN DEBES VALIDAR SI SOLO DECLARAN LA VARIABLE LOCAL PERO NO LE ASIGNAN VALOR Y LA USAN COMO CONTADOR
        simboloVar = table.getTabla(str(self.identificador))
        if simboloVar != None:
            tablaSimboloVar = table.getRealTabla(str(self.identificador))
            if simboloVar.local == True and self.globall == True:
                return Excepcion("Semántico", "No se puede declarar una variable global donde ya existe una variable local", self.fila, self.columna) 
            elif simboloVar.local == True and self.local == True and tablaSimboloVar == table:
                return Excepcion("Semántico", "No se puede declarar una variable local donde ya existe una variable local", self.fila, self.columna) 


        if self.valor != None: #Si viene un valor
            value = self.valor.interpretar(tree, table, generator)
            if isinstance(value, Excepcion):
                return value
            
            if self.tipo == None: #Verifica si el tipo de la var no viene
                self.tipo = self.valor.tipo #Le asigna el tipo a la var

            if self.tipo != self.valor.tipo: #Verifica que las variables sean del mismo tipo 
                return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna) 

        tamTable = table.size
        newTemp = generator.createTemp()

        if self.local: #Se encarga de las variable locales
            if simboloVar != None:
                simbolo = Simbolo(str(self.identificador), self.tipo, value, tamTable, True, False, self.fila, self.columna)
            else:
                simbolo = Simbolo(str(self.identificador), self.tipo, value, tamTable, True, False, self.fila, self.columna)
        
        
        elif self.globall: #Se encarga de las variables globales
            if simboloVar == None: #Verifica si la variable no estaba declarada anteriormente de modo global        
                return Excepcion("Semántico", "La variable \""+self.identificador+"\" no existe en el entorno global", self.fila, self.columna) 
            elif simboloVar != None:#Verifica si la variable ya estaba declarada anteriormente de modo global
                simbolo = Simbolo(str(self.identificador), self.tipo, value, simboloVar.posicion, False, True, self.fila, self.columna)
                resultGlobal = tree.getTSGlobal().actualizarTabla(simbolo) #Actualiza el simbolo al entorno global
                if isinstance(resultGlobal, Excepcion):
                    return resultGlobal
            
        result = table.setTabla(simbolo)  #pos namas estamos mandando el identificador a la tablita jeje
        if isinstance(result, Excepcion):
            return result

        #Creacion de C3D
        if self.tipo == Tipo.BANDERA:
            self.addBoolean(newTemp, simbolo.posicion, tree, generator)
        elif self.tipo == Tipo.CADENA:
            self.addCadena(value, newTemp, simbolo.posicion, tree, generator)
        else:
            valor = self.correctValue(value)
            tree.updateConsola(generator.newExpresion(newTemp, 'P', str(simbolo.posicion), '+'))
            tree.updateConsola(generator.newSetStack(newTemp, str(valor)))

        return None
        


    def getNode(self):
        return super().getNode()


    def addCadena(self, value, newTemp, tamTable, tree, generator):
        newTempH = generator.createTemp()
        tree.updateConsola(generator.newAsigTemp(newTempH, 'H'))
        for char in value.getValor():
            tree.updateConsola(generator.newSetHeap('H', str(ord(char))))
            tree.updateConsola(generator.newNextHeap())
        tree.updateConsola(generator.newSetHeap('H', str(-1)))
        tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
        tree.updateConsola(generator.newSetStack(newTemp, newTempH))

    def addBoolean(self, newTemp, tamTable, tree, generator):
        newLabel = generator.createLabel()
        tree.updateConsola(generator.newLabel(newLabel.trueLabel))
        tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
        tree.updateConsola(generator.newSetStack(newTemp, '1'))
        tree.updateConsola(generator.newGoto(newLabel))
        tree.updateConsola(generator.newLabel(newLabel.falseLabel))
        tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
        tree.updateConsola(generator.newSetStack(newTemp, '0'))
        tree.updateConsola(generator.newLabel(newLabel))

    def correctValue(self, valor):
        if valor.isTemp:
            return valor.getTemporal()
        else:
            return valor.getValor()