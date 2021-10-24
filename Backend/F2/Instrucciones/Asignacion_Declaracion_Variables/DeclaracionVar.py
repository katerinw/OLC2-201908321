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

        if self.local: #Se encarga de las variable locales
            tamTable = table.size
            newTemp = generator.createTemp()
            if simboloVar != None:
                simbolo = Simbolo(str(self.identificador), self.tipo, value, tamTable, newTemp, True, False, self.fila, self.columna)
            else:
                simbolo = Simbolo(str(self.identificador), self.tipo, value, tamTable, newTemp, True, False, self.fila, self.columna)
        
        
        elif self.globall: #Se encarga de las variables globales
            if simboloVar == None: #Verifica si la variable no estaba declarada anteriormente de modo global        
                return Excepcion("Semántico", "La variable \""+self.identificador+"\" no existe en el entorno global", self.fila, self.columna) 
            elif simboloVar != None:#Verifica si la variable ya estaba declarada anteriormente de modo global
                simbolo = Simbolo(str(self.identificador), self.tipo, value, simboloVar.posicion, simboloVar.posicionTemp, False, True, self.fila, self.columna)
                resultGlobal = tree.getTSGlobal().actualizarTabla(simbolo) #Actualiza el simbolo al entorno global
                if isinstance(resultGlobal, Excepcion):
                    return resultGlobal
            
        result = table.setTabla(simbolo)  #pos namas estamos mandando el identificador a la tablita jeje
        if isinstance(result, Excepcion):
            return result

        #Creacion de C3D
        if self.tipo == Tipo.BANDERA:
            self.addBoolean(simbolo.posicionTemp, simbolo.posicion, tree, generator)
        elif self.tipo == Tipo.CADENA:
            self.addCadena(value, simbolo.posicionTemp, simbolo.posicion, tree, generator)
        else:
            tree.updateConsola(generator.newExpresion(simbolo.posicionTemp, 'P', str(simbolo.posicion), '+'))
            tree.updateConsola(generator.newSetStack(simbolo.posicionTemp, str(value.getValor())))

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
        if tamTable != None:
            tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
        tree.updateConsola(generator.newSetStack(newTemp, newTempH))

    def addBoolean(self, newTemp, tamTable, tree, generator):
        newLabel = generator.createLabel()
        tree.updateConsola(generator.newLabel(newLabel.trueLabel))
        if tamTable != None:
            tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
        tree.updateConsola(generator.newSetStack(newTemp, '1'))
        tree.updateConsola(generator.newGoto(newLabel))
        tree.updateConsola(generator.newLabel(newLabel.falseLabel))
        if tamTable != None:
            tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
        tree.updateConsola(generator.newSetStack(newTemp, '0'))
        tree.updateConsola(generator.newLabel(newLabel))