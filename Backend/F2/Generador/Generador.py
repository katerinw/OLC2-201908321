from Generador.Nativas import *

class Generador:
    def __init__(self):
        self.generador = None
        self.temporal = 0
        self.label = 0
        self.codigo = []
        self.listaTemporales = []

    def newTemp(self): #Generar un nuevo temporal
        temporal = 't' + str(self.temporal)
        self.temporal += 1
        self.listaTemporales.append(temporal) #Se guarda para declararse
        return temporal

    def newLabel(self):
        label  = 'L' + str(self.label)
        self.label += 1
        return label

    def addCallFunc(self, nombre):
        self.codigo.append(nombre+"();")

    def addIf(self, opIzq, opDer, operador, label):
        self.codigo.append("if(" + opIzq + " " + operador + " " + opDer + ") {goto " + label + "};")

    def addGoto(self, label):
        self.codigo.append("goto " + label + ";")

    def addLabel(self, label):
        self.codigo.append(str(label) + ":")

    def addExpresion(self, target, izq, der, operador): #Agrega las expresiones al codigo
        self.codigo.append(target + ' = ' + izq + ' ' + operador + ' ' + der + ';')

    '''def addRelacional(self, expresion):
        newLabel = self.newLabel()
        self.addLabel(str(expresion.trueLabel))'''


    def addPrint(self, typePrint, value): #Añade un printf
        self.codigo.append('fmt.Printf(\"%' + typePrint + '\",' + value + ');')

    def addNewLine(self):
        self.codigo.append('fmt.Printf(\"%c\",10);')

    def getCode(self):
        tempCode = 'package main\n'
        tempCode += 'import ("fmt")\n'
        tempCode += 'var stack[30101999]float64\n'
        tempCode += 'var heap[30101999]float64\n'
        tempCode += 'var P, H float64\n'
        tempCode += 'var '
        if len(self.listaTemporales) > 0:
            tempCode += self.getUsedTemps()
        tempCode += ' float64; \n\n'
        tempCode += addTrue()
        tempCode += addFalse()
        tempCode += addMathError()
        tempCode += addBoundsError()
        tempCode += 'func main(){\n'
        tempCode += "\n".join(self.codigo)
        tempCode += '\n}\n'

        return tempCode 

    #Obtener los temporales usados
    def getUsedTemps(self):
        return ",".join(self.listaTemporales)

    