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

    def addLabel(self, label):
        self.codigo.append(str(label) + ":")

    def addExpresion(self, target, izq, der, operador): #Agrega las expresiones al codigo
        self.codigo.append(target + ' = ' + izq + ' ' + operador + ' ' + der + ';')

    def addPrint(self, typePrint, value): #Añade un printf
        self.code.append('fmt.Printf(\"%' + typePrint + '\",' + value + ');')

    def addNewLine(self):
        self.codigo.append('fmt.Printf(\"%c\",10);')

    



