''' Segundo semestre 2021 '''

import re
import sys

#LISTA DE ERRORES
errores = []


reservedWords = {
    'true': 'TRUE',
    'false': 'FALSE',
    'nothing' : 'NOTHING',
    'int64': 'INT64',
    'float64': 'FLOAT64',
    'string': 'STRING',
    'bool': 'BOOL',
    'char': 'CHAR',
    'struct': 'STRUCT',
    'print': 'PRINT',
    'println': 'PRINTLN'
}

#DECLARACION DE TOKENS
tokens = [
    'MAS',
    'MENOS',
    'ASTERISCO',
    'DIAGONAL',
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
    'PUNTOCOMA',
    'ID',
    'ENTERO',
    'DOBLE',
    'CADENA',
    'CARACTER',
    'ignore_COMENTARIOMULTILINEA',
    'ignore_COMENTARIOUNILINEA',
] + list(reservedWords.values())

#ASIGNACION DE TOKENS 
t_MAS = r'\+'
t_MENOS = r'\-'
t_ASTERISCO = r'\*'
t_DIAGONAL = r'\\'
t_DIVISION = r'/'
t_POTENCIA = r'\^'
t_PORCENTAJE = r'%'
t_MENOR = r'<'
t_MAYOR = r'>'
t_IGUAL = r'='
t_MAYORIGUAL = r'>='
t_MENORIGUAL = r'<='
t_IGUALIGUAL = r'=='
t_DIFERENTE = r'!='
t_OR = r'\|\|'
t_AND = r'&&'
t_NOT = r'!'
t_PARENTESISA = r'\('
t_PARENTESISC = r'\)' 
t_LLAVESA = r'\{'
t_LLAVESC = r'\}'
t_PUNTOCOMA = r';' 


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservedWords.get(t.value.lower(),'ID') #Cecha las palbras reservadas
    return t

def t_DOBLE(t):
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

def t_CARACTER(t):
    r"""\'(\\'|\\\\|\\n|\\t|\\r|\\"|.)?\'"""
    t.value = t.value[1:-1]
    return t

'''Se pone ignore para obligar al analizador a ignorarlo y 
ademas no se retorna nada para que no lo tome en cuenta'''

def t_ignore_COMENTARIOMULTILINEA(t):
    r'\#=(.|\n*|)*?=\#'
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
def t_error(t):
    errores.append(Excepcion("Léxico","Error léxico." + t.value[0] , t.lexer.lineno, find_column(input, t)))
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1) 

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

from TS.Excepcion import Excepcion
from Instrucciones.Funciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import Tipo
from Expresiones.OperacionAritmetica import OperacionAritmetica
from TS.Tipo import OperadorAritmetico


#Definir precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'IGUALIGUAL', 'DIFERENTE', 'MENOR', 'MENORIGUAL', 'MAYOR', 'MAYORIGUAL', ),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'PORCENTAJE'),
    ('nonassoc', 'POTENCIA'),
    ('left', 'MASMAS', 'MENOSMENOS'),
    ('right', 'UMINUS'),    
)

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

def p_instruccion_error(p):
    'instruccion : error fininstr'
    errores.append(Excepcion("Sintáctico", "Error sintáctico, " + str(p[1].value), p.lineno(1), find_column(input, p.slice[1])))
    p[0] = ""

#//////////////////////////////////////////////////IMPRIMIR
def p_imprimir(p):
    'imprimir_instr : PRINT PARENTESISA expresion PARENTESISC'
    p[0] = Imprimir(p[3], False, p.lineno(1), find_column(input, p.slice[1]))

def p_imprimirln(p):
    'imprimir_instr : PRINTLN PARENTESISA expresion PARENTESISC'
    p[0] = Imprimir(p[3], True, p.lineno(1), find_column(input, p.slice[1]))

#//////////////////////////////////////////////////EXPRESION
def p_expresion_string(p):
    'expresion : CADENA'
    p[0] = Primitivos(Tipo.CADENA, str(p[1]).replace('\\n', '\n').replace('\\\\', '\\').replace('\\t','\t').replace('\\r', '\r').replace('\\v', '\v').replace('\\\"', '\"').replace('\\\'', '\''), p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_character(p):
    'expresion : CARACTER'
    p[0] = Primitivos(Tipo.CARACTER, p[1], p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_integer(p):
    'expresion : ENTERO'
    p[0] = Primitivos(Tipo.ENTERO, p[1], p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_double(p):
    'expresion : DOBLE'
    p[0] = Primitivos(Tipo.DOBLE, p[1], p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_nothing(p):
    'expresion : NOTHING'
    p[0] = Primitivos(Tipo.NULO, p[1], p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_boolean(p):
    'expresion : bandera'
    p[0] = p[1]

def p_expresion_binaria_aritmetica(p):
    '''expresion : expresion MAS expresion
                 | expresion MENOS expresion
                 | expresion ASTERISCO expresion
                 | expresion DIVISION expresion
                 | expresion POTENCIA expresion
                 | expresion PORCENTAJE expresion'''
    
    if p[2] == '+':
        p[0] = OperacionAritmetica(OperadorAritmetico.MAS, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '-':
        p[0] = OperacionAritmetica(OperadorAritmetico.MENOS, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '*':
        p[0] = OperacionAritmetica(OperadorAritmetico.ASTERISCO, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '/':
        p[0] = OperacionAritmetica(OperadorAritmetico.DIVISION, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '^':
        p[0] = OperacionAritmetica(OperadorAritmetico.POTENCIA, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '%':
        p[0] = OperacionAritmetica(OperadorAritmetico.PORCENTAJE, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))


#//////////////////////////////////////////////////BOOLEAN
def p_bandera(p):
    '''bandera : TRUE
               | FALSE'''
    p[0] = Primitivos(Tipo.BANDERA, p[1], p.lineno(1), find_column(input, p.slice[1]))

#Haciendo el parser
import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores 

def parse(inp):
    global errores 
    global lexer 
    global parser 
    errores = []
    lexer = lex.lex()
    parser = yacc.yacc()
    global input 
    input = inp
    return parser.parse(inp)

#Se va para la interfaz
file = open("./entrada.txt", "r", encoding="utf-8-sig")
entrada = file.read()

from TS.Arbol import Arbol
from TS.TablaSimbolos import TablaSimbolos

instrucciones = parse(entrada) #ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos()
ast.setTSGlobal(TSGlobal)

for error in errores: #Captura de errores lexicos y sintacticos 
    ast.getExcepciones().append(error)
    ast.updateConsola(error.toString())
    

for instruccion in ast.getInstrucciones():
    valor = instruccion.interpretar(ast, TSGlobal)
    if isinstance(valor, Excepcion):
        ast.getExcepciones().append(valor)
        ast.updateConsola(valor.toString())

print(ast.getConsola())





    


