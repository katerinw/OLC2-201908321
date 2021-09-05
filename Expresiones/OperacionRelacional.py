from Abstract.Instruccion import Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import OperadorRelacional, Tipo

class OperacionRelacional(Instruccion):
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

        #igualacion
        if self.operador == OperadorRelacional.IGUALIGUAL:
            return self.igualacion(opIzq, opDer)

        #diferente
        elif self.operador == OperadorRelacional.DIFERENTE:
            return self.diferencia(opIzq, opDer)

        #menor que
        elif self.operador == OperadorRelacional.MENOR:
            return self.menor(opIzq, opDer)

        #mayor que
        elif self.operador == OperadorRelacional.MAYOR:
            return self.mayor(opIzq, opDer)

        #menor igual
        elif self.operador == OperadorRelacional.MENORIGUAL:
            return self.menorIgual(opIzq, opDer)

        #mayor igual
        elif self.operador == OperadorRelacional.MAYORIGUAL:
            return self.mayorIgual(opIzq, opDer)
        
        return Excepcion("Semántico", "Tipo de operación relacional no Especificado.", self.fila, self.columna)


    def igualacion(self, opIzq, opDer):
        #boolean
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) == self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) == self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) == self.getType(self.opDer, opDer)
        elif (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE) or (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO):
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) == self.getType(self.opDer, opDer)
        return Excepcion("Semántico", "Los tipos de datos para el signo \"==\" no son los correctos", self.fila, self.columna)
    

    def diferencia(self, opIzq, opDer):
        #boolean
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) != self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) != self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) != self.getType(self.opDer, opDer)
        elif (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE) or (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO):
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) != self.getType(self.opDer, opDer)
        return Excepcion("Semántico", "Los tipos de datos para el signo \"!=\" no son los correctos", self.fila, self.columna)


    def mayor(self, opIzq, opDer):
        #boolean
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) > self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) > self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) > self.getType(self.opDer, opDer)
        elif (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE) or (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO):
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) > self.getType(self.opDer, opDer)
        return Excepcion("Semántico", "Los tipos de datos para el signo \">\" no son los correctos", self.fila, self.columna)


    def menor(self, opIzq, opDer):
        #boolean
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) < self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) < self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) < self.getType(self.opDer, opDer)
        elif (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE) or (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO):
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) < self.getType(self.opDer, opDer)
        return Excepcion("Semántico", "Los tipos de datos para el signo \"<\" no son los correctos", self.fila, self.columna)


    def mayorIgual(self, opIzq, opDer):
        #boolean
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) >= self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) >= self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) >= self.getType(self.opDer, opDer)
        elif (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE) or (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO):
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) >= self.getType(self.opDer, opDer)
        return Excepcion("Semántico", "Los tipos de datos para el signo \">=\" no son los correctos", self.fila, self.columna)


    def menorIgual(self, opIzq, opDer):
        #boolean
        if self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.ENTERO:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) <= self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.DOBLE:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) <= self.getType(self.opDer, opDer)
        elif self.opIzq.tipo == Tipo.CADENA and self.opDer.tipo == Tipo.CADENA:
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) <= self.getType(self.opDer, opDer)
        elif (self.opIzq.tipo == Tipo.ENTERO and self.opDer.tipo == Tipo.DOBLE) or (self.opIzq.tipo == Tipo.DOBLE and self.opDer.tipo == Tipo.ENTERO):
            self.tipo = Tipo.BANDERA
            return self.getType(self.opIzq, opIzq) <= self.getType(self.opDer, opDer)
        return Excepcion("Semántico", "Los tipos de datos para el signo \"<=\" no son los correctos", self.fila, self.columna)


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