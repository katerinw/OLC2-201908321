from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorAritmetico, Tipo

class OperacionAritmetica(Instruccion):
    def __init__(self, operador, opIzq, opDer, fila, columna):
        self.operador = operador
        self.opIzq = opIzq
        self.opDer = opDer
        self.fila = fila
        self.columna = columna
        self.tipo = None

    def interpretar(self, tree, table):
        opIzq = self.opIzq.interpretar(tree, table)
        if isinstance(opIzq, Excepcion):
            return opIzq
        
        if self.opDer != None:
            opDer = self.opDer.interpretar(tree, table)
            if isinstance(opDer, Excepcion):
                return opDer

        #suma
        if self.operador == OperadorAritmetico.MAS:
            return self.suma(opIzq, opDer)

        #resta
        elif self.operador == OperadorAritmetico.MENOS:
            return self.resta(opIzq, opDer)

        #multiplicacion
        elif self.operador == OperadorAritmetico.ASTERISCO:
            return self.multiplicacion(opIzq, opDer)

        #division
        elif self.operador == OperadorAritmetico.DIVISION:
            if opDer != 0:
                return self.division(opIzq, opDer)
            else:
                return Excepcion("Semántico", "No se puede dividir entre cero", self.fila, self.columna) 
        
        #potencia
        elif self.operador == OperadorAritmetico.POTENCIA:
            return self.potencia(opIzq, opDer)
        
        #modulo
        elif self.operador == OperadorAritmetico.PORCENTAJE:
            if opDer != 0:
                return self.modulo(opIzq, opDer)
            else:
                return Excepcion("Semántico", "No se puede hacer mmodulo de cero", self.fila, self.columna) 

        return Excepcion("Semántico", "Tipo de Operacion no Especificado.", self.fila, self.columna)


    def suma(self, opIzq, opDer):
        #entero
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.ENTERO
            return int(self.getType(self.opIzq, opIzq) + self.getType(self.opDer, opDer))

        #decimal
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) + self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) + self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) + self.getType(self.opDer, opDer))

        return Excepcion("Semántico", "Los tipos de datos para el signo \"+\" no pueden ser operados", self.fila, self.columna)
    

    def resta(self, opIzq, opDer):
         #entero
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.ENTERO
            return int(self.getType(self.opIzq, opIzq) - self.getType(self.opDer, opDer))

        #decimal
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) - self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) - self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) - self.getType(self.opDer, opDer))

        return Excepcion("Semántico", "Los tipos de datos para el signo \"-\" no pueden ser operados", self.fila, self.columna)


    def multiplicacion(self, opIzq, opDer):
        #entero
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.ENTERO
            return int(self.getType(self.opIzq, opIzq) * self.getType(self.opDer, opDer))

        #decimal
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) * self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) * self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) * self.getType(self.opDer, opDer))

        #string
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo ==Tipo.CADENA
            return str(self.getType(self.opIzq, opIzq) + self.getType(self.opDer, opDer))

        return Excepcion("Semántico", "Los tipos de datos para el signo \"*\" no pueden ser operados", self.fila, self.columna)


    def division(self, opIzq, opDer):
        #decimal
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) / self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) / self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) / self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) / self.getType(self.opDer, opDer))
    
        return Excepcion("Semántico", "Los tipos de datos para el signo \"\\\" no pueden ser operados", self.fila, self.columna)


    def potencia(self, opIzq, opDer):
        #entero
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.ENTERO
            return int(self.getType(self.opIzq, opIzq) ** self.getType(self.opDer, opDer))

        #decimal
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) ** self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) ** self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) ** self.getType(self.opDer, opDer))

        #cadena
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.CADENA
            return str(self.getType(self.opIzq, opIzq) * self.getType(self.opDer, opDer))

        return Excepcion("Semántico", "Los tipos de datos para el signo \"^\" no pueden ser operados", self.fila, self.columna)


    def modulo(self, opIzq, opDer):
        #entero
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.ENTERO
            return int(self.getType(self.opIzq, opIzq) % self.getType(self.opDer, opDer))

        #decimal
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) % self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) % self.getType(self.opDer, opDer))
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo == Tipo.DOBLE
            return float(self.getType(self.opIzq, opIzq) % self.getType(self.opDer, opDer))

        return Excepcion("Semántico", "Los tipos de datos para el signo \"%\" no pueden ser operados", self.fila, self.columna)


    def getType(self, nodo, valor):
        if nodo.tipo == Tipo.ENTERO:
            return int(valor)
        elif nodo.tipo == Tipo.DOBLE:
            return float(valor)
        elif nodo.tipo == Tipo.CADENA:
            return str(valor)
        elif nodo.tipo == Tipo.CARACTER:
            return str(valor)
        elif nodo.tipo == Tipo.BANDERA:
            if str(valor).lower() == 'true':
                return True
            elif str(valor).lower() == 'false':
                return False
        return valor