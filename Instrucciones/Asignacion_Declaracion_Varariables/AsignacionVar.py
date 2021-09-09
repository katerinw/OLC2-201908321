from Abstract.Instruccion import  Instruccion
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo
from TS.Simbolo import Simbolo

class AsignacionVar(Instruccion):
    def __init__(self, identificador, valor, tipo, fila, columna):
        self.identificador = identificador
        self.valor = valor
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def interpretar(self, tree, table):
        value = self.valor.interpretar(tree, table) #Interpreta el valor
        if isinstance(value, Excepcion): 
            return value

        if self.tipo == None: #Verifica si la variable trae tipo
            self.tipo = self.valor.tipo

            if self.tipo != self.valor.tipo: #Verifica que sea el mismo tipo de variable
                return Excepcion("Semántico", "El tipo de dato en la variable \""+self.identificador+"\" es diferente", self.fila, self.columna)

        simboloVar = table.getTabla(str(self.identificador)) #Verifica si la varuable ya existe en algún entorno

        tablaSimbolo = table.getRealTabla(str(self.identificador))
        if tablaSimbolo == tree.getTSGlobal() and table != tree.getTSGlobal():  #Verofica que la variable que se encontro sea diferente 
            simboloVar = None


        if simboloVar != None: #Reasignar variable
            if simboloVar.globall: #Si la variable es global jsjs
                simbolo = Simbolo(str(self.identificador), self.tipo, value, False, True, self.fila, self.columna)

                result = table.actualizarTabla(simbolo)  #Actualiza la variable que esta dentro del entorno
                if isinstance(result, Excepcion):
                    return result

                resultGlobal = tree.getTSGlobal().actualizarTabla(simbolo) #Actualiza la variable global
                if isinstance(resultGlobal, Excepcion):
                    return resultGlobal

            elif simboloVar.local: #Si la variable es local jsjs
                simbolo = Simbolo(str(self.identificador), self.tipo, value, True, False, self.fila, self.columna)

                result = table.actualizarTabla(simbolo)

                if isinstance(result, Excepcion):
                    return result
                
            else: #Si se declara asi normal como abajo

                simbolo = Simbolo(str(self.identificador), self.tipo, value, False, False, self.fila, self.columna)
                result = table.actualizarTabla(simbolo)
                if isinstance(result, Excepcion):
                    return result

        elif simboloVar == None: #Declarar variable
            simbolo = Simbolo(str(self.identificador), self.tipo, value, False, False, self.fila, self.columna)

            result = table.setTabla(simbolo)
            if isinstance(result, Excepcion):
                return result
            
        return None

