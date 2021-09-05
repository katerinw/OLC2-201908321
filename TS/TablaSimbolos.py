from TS.Excepcion import Excepcion

class TablaSimbolos:
    def __init__(self, anterior = None):
        self.tabla = {} #Da un diccionario vacio
        self.anterior = anterior

    def setTabla(self, simbolo): #Agrega una variable al entorno
        if simbolo.identificador in self.tabla:
            return True
            #return Excepcion("Semántico", "Variable \"" + simbolo.identificador + "\" ya existe", simbolo.fila, simbolo.columna)
        else: 
            self.tabla[simbolo.identificador] = simbolo
            return None

    def getTabla(self, identificador):
        tablaActual = self
        while tablaActual != None:
            if identificador in tablaActual.tabla:
                return tablaActual.tabla[identificador] #Devuelve un nodo simbolo
            else:
                tablaActual = tablaActual.anterior
        return None

    def actualizarTabla(self, simbolo):
        tablaActual = self
        while tablaActual != None:
            if simbolo.identificador in tablaActual.tabla:
                tablaActual.tabla[simbolo.identificador].setValor(simbolo.getValor())
                tablaActual.tabla[simbolo.identificador].setTipo(simbolo.getTipo())
                return "variable actualizada" #Si regresa esto es que si la actualizo
            else:
                tablaActual = tablaActual.anterior
        return None #Si regresa esto es que no la actualizo
