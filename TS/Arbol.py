class Arbol:
    def __init__(self, instrucciones):
        self.instrucciones = instrucciones
        self.funciones = []
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

    