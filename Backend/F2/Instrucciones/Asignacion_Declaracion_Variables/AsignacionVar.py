from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Simbolo import Simbolo
from TS.Tipo import Tipo

class AsignacionVar(Instruccion):
    def __init__(self, identificador, valor, tipo, fila, columna):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table, generator):
        value = self.valor.interpretar(tree, table, generator)
        if isinstance(value, Excepcion):
            return value

        if self.tipo == None:
            self.tipo = self.valor.tipo
        
        if self.tipo != self.valor.tipo:
            return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna)

        simboloVar = table.getTabla(str(self.identificador))
        
        if simboloVar != None:
            if simboloVar.globall: #Si la variable es global
                simbolo = Simbolo(str(self.identificador), self.tipo, value, None, None, False, True, self.fila, self.columna)
                result = table.actualizarTabla(simbolo) #Actualiza la variable del entorno global
                if isinstance(result, Excepcion):
                    return result
                resultGlobal = tree.getTSGlobal().actualizarTabla(simbolo) #Actualiza la variable global
                if isinstance(resultGlobal, Excepcion):
                    return result
            
            elif simboloVar.local: #Si la variable es local
                simbolo = Simbolo(str(self.identificador), self.tipo, value, None, None, True, False, self.fila, self.columna)
                result = table.actualizarTabla(simbolo) #Actualiza la variable local mas cercana
                if isinstance(result, Excepcion):
                    return result
            
            else: #Si se declara normalita
                simbolo = Simbolo(str(self.identificador), self.tipo, value, None, None, False, False, self.fila, self.columna)
                result = table.actualizarTabla(simbolo)
                if isinstance(result, Excepcion):
                    return result

            #Creacion de C3D
            if self.tipo == Tipo.BANDERA:
                self.addBoolean(simboloVar.posicionTemp, None, tree, generator)
            elif self.tipo == Tipo.CADENA:
                self.addCadena(value, simboloVar.posicionTemp, None, tree, generator)

            else:
                tree.updateConsola(generator.newSetStack(simboloVar.posicionTemp, str(value.getValor())))
        
        elif simboloVar == None:
            tamTable = table.size
            newTemp = generator.createTemp()
            simbolo = Simbolo(str(self.identificador), self.tipo, value, tamTable, newTemp, False, False, self.fila, self.columna)
            result = table.setTabla(simbolo)

            #Creacion de C3D
            if self.tipo == Tipo.BANDERA:
                self.addBoolean(newTemp, tamTable, tree, generator)
            elif self.tipo == Tipo.CADENA:
                self.addCadena(value, newTemp, tamTable, tree, generator)
            else:
                tree.updateConsola(generator.newExpresion(newTemp, 'P', str(tamTable), '+'))
                tree.updateConsola(generator.newSetStack(newTemp, str(value.getValor())))

#IBAS A HACER REASIGNACION DESPUES DE LAB DE ARQUI
        
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
