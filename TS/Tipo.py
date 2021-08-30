from enum import Enum
from typing import ClassVar

class Tipo(Enum):
    ENTERO = 1
    DOBLE = 2 
    BANDERA = 3
    CARACTER = 4 
    CADENA = 5 
    NULO = 6
    ARREGLO = 7

class OperadorAritmetico(Enum):
    MAS = 1
    MENOS = 2
    ASTERISCO = 3
    DIVISION = 4
    POTENCIA = 5
    PORCENTAJE = 6
    UMENOS = 7

class OperadorRelacional(Enum):
    MENOR = 1
    MAYOR = 2 
    MENORIGUAL = 3
    MAYORIGUAL = 4
    IGUALIGUAL = 5
    DIFERENTE = 6

class OperadorLogico(Enum):
    NOT = 1
    AND = 2
    OR = 3

