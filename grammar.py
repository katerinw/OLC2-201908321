''' Segundo semestre 2021 '''

import re
import sys

#LISTA DE ERRORES
errores = []


reservedWords = {
    'true': 'TRUE',
    'false': 'FALSE'
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
    r'[a-zA-Z_][a-zA-Z_0-9]'
    t_type = reservedWords.get(t.value.lower(),'ID')
    return t

def t_DECIMAL(t):
    r'\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Double value too large %d", t.value)
        t.value = 0
    return t

def t_ENTERO(t):
    r'\d+'
    try: 
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

def t_CADENA(t):
    r'\"((\\\")|[^\n\"])*\"'
    t.value = t.value[1:-1]
    return t

def t_CHAR(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|.)?\'""" #creo que hay que mejorarla pq no reconoce dos caracteres como \n \t
    t.value = t.value[1:-1]
    return t

