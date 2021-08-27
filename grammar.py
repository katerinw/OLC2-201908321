''' Segundo semestre 2021 '''

import re
import sys

#LISTA DE ERRORES
errores = []


reservedWords = {
    'true': 'TRUE',
    'false': 'FALSE',
    'int64': 'INT64',
    'float64': 'FLOAT64',
    'bool': 'BOOL',
    'char': 'CHAR',
    'string': 'STRING',
    'print': 'PRINT',
    'println': 'PRINTLN'
}

#DECLARACION DE TOKENS
tokens = [
    'MAS',
    'MENOS',
    'ASTERISCO',
    'DIVISION',
    'POTENCIA',
    'PORCENTAJE',
    'MENOR',
    'MAYOR',
    'IGUAL',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUALIGUAL',
    'DIFERENTE',
    'OR',
    'AND',
    'NOT',
    'PARENTESISA',
    'PARENTESISC',
    'LLAVESA',
    'LLAVESC',
    'ID',
    'ENTERO',
    'DECIMAL',
    'CADENA',
    'CARACTER',
    'ignore_COMENTARIOMULTILINEA',
    'ignore_COMENTARIOUNILINEA',
] + list(reservedWords.values())

#ASIGNACION DE TOKENS 
t_MAS = r'\+'
t_MENOS = r'\-'
t_ASTERISCO = r'\*'
t_DIVISION = r'\\'
t_POTENCIA = r'\^'
t_PORCENTAJE = r'%'
t_MENOR = r'<'
t_MAS = r'>'
t_IGUAL = r'='
t_MAYORIGUAL = r'>='
t_MANORIGUAL = r'<='
t_IGUALIGUAL = r'=='
t_DIFERENTE = r'!='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_PARENTESISA = r'\('
t_PARENTESISC = r'\)' 
t_LLAVESA = r'\{'
t_LLAVESC = r'\}'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t_type = reservedWords.get(t.value.lower(),'ID') #Cecha las palbras reservadas
    return t

def t_DOUBLE(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t

def t_INTEGER(t):
    r'\d+'
    try: 
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_STRING(t):
    r'\"((\\\")|[^\n\"])*\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|.)?\'"""
    t.value = t.value[1:-1]
    return t

'''Se pone ignore para obligar al analizador a ignorarlo y 
ademas no se retorna nada para que no lo tome en cuenta'''

def t_ignore_COMENTARIOMULTILINEA(t):
    r'\#=(.|\n*|)*?=#'
    t.lexer.lineno += t.value.count('\n')

def t_ignore_COMENTARIOUNILINEA(t):
    r'\#.*\n'
    t.lexer.lineno +=1

#Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

#Error handling rule
#Almacenamiento de errores lexicos
'''def t_errors(t):
    errores'''

#Compute column.
#     input is the input text string
#     token is a token instance

def find_column(inp, token):
    line_start = inp.rfind('\n', 0, token.lexpos) + 1
    return (token.lexpos - line_start) + 1

#Caracteres ignorados
t_ignore = "\t"

#Construyendo un analizador
import ply.lex as lex
lexer = lex.lex()

from Abstract.Instruccion import Instruccion
from Instrucciones.Funciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos



#Definir precedencia
precedence = ()

#Definir la gramatica
start = 'inicio'

def p_inicio(p):
    'inicio : instrucciones'
    p[0] = p[1]

#//////////////////////////////////////////////////FINAL INSTRUCCION
def p_fininstr(p):
    'fininstr : PUNTOCOMA'


#//////////////////////////////////////////////////INSTRUCCIONES
def p_instrucciones_instrucciones_instruccion(p):
    'instrucciones : instrucciones instruccion'
    if p[2] != "":
        p[1].append(p[2])
    p[0] = p[1]

def p_instrucciones_instruccion(p):
    'instrucciones : instruccion'
    if p[1] == "":
        p[0] = ""
    else:
        p[0] = [p[1]]

#//////////////////////////////////////////////////INSTRUCCION
def p_instruccion(p):
    '''instruccion : imprimir_instr fininstr'''
    p[0] = p[1]


#//////////////////////////////////////////////////IMPRIMIR
def p_imprimir(p):
    'imprimir_instr : PRINT PARENTESISA expresion PARENTESISC'


#//////////////////////////////////////////////////Expresion
def p_expresion_cadena(p):
    'expresion : STRING'







    


