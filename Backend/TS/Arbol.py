class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = []
        self.structs = []
        self.excepciones = []
        self.consola = ""
        self.TSGlobal = None

    def getInstrucciones(self):
        return self.instrucciones

    def setInstrucciones(self, instrucciones):
        self.instrucciones = instrucciones

    def getExcepciones(self):
        return self.excepciones

    def setExcepciones(self, excepciones):
        self.excepciones = excepciones

    def getConsola(self):
        return self.consola

    def setConsola(self, consola):
        self.consola = consola

    def updateConsolaln(self, cadena):
        self.consola += str(cadena) + '\n'

    def updateConsola(self, cadena):
        self.consola += str(cadena)

    def getTSGlobal(self):
        return self.TSGlobal

    def setTSGlobal(self, TSGlobal):
        self.TSGlobal = TSGlobal

    def getFunciones(self):
        return self.funciones

    def getFuncion(self, identificador):
        for funcion in self.funciones:
            if funcion.identificador == identificador:
                return funcion
        return None

    def addFuncion(self, funcion):
        self.funciones.append(funcion)

    def getStructs(self):
        return self.structs

    def getStruct(self, identificador):
        for struct in self.structs:
            if struct.identificador == identificador:
                return struct
        return None

    def addStruct(self, struct):
        self.structs.append(struct)

    