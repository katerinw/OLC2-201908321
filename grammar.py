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
    'println': 'PRINTLN',
    'log10' : 'LOG10',
    'log' : 'LOG',
    'sin' : 'SIN',
    'cos' : 'COS',
    'tan' : 'TAN',
    'sqrt' : 'SQRT',
    'function' : 'FUNCTION',
    'end' : 'END',
    'while' : 'WHILE',
    'for' : 'FOR',
    'local' : 'LOCAL',
    'global' : 'GLOBAL'

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
    'DOSPUNTOS',
    'COMA',
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
t_NOT = r'\!'
t_PARENTESISA = r'\('
t_PARENTESISC = r'\)' 
t_LLAVESA = r'\{'
t_LLAVESC = r'\}'
t_PUNTOCOMA = r';' 
t_DOSPUNTOS = r':' 
t_COMA = r','


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
    r'\#.*\n?'
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
t_ignore = " \t"

#Construyendo un analizador
import ply.lex as lex
lexer = lex.lex()

from TS.Excepcion import Excepcion
from Instrucciones.Funciones.Imprimir import Imprimir
from Expresiones.Primitivos import Primitivos
from TS.Tipo import Tipo
from Expresiones.OperacionAritmetica import OperacionAritmetica
from Expresiones.OperacionRelacional import OperacionRelacional
from Expresiones.OperacionLogica import OperacionLogica
from TS.Tipo import OperadorAritmetico, OperadorRelacional, OperadorLogico
from Instrucciones.Asignacion_Declaracion_Varariables.AsignacionVar import AsignacionVar
from Instrucciones.Asignacion_Declaracion_Varariables.DeclaracionVar import DeclaracionVar
from Expresiones.Identificador import Identificador
from Instrucciones.Funciones.Funcion import Funcion
from Instrucciones.Ciclos.While import While
from Instrucciones.Funciones.LlamadaFuncion import LlamadaFuncion



#Definir precedencia
precedence = (
    ('left', 'OR'),
    ('left', 'AND'),
    ('right', 'UNOT'),
    ('left', 'IGUALIGUAL', 'DIFERENTE', 'MENOR', 'MENORIGUAL', 'MAYOR', 'MAYORIGUAL', ),
    ('left', 'MAS', 'MENOS'),
    ('left', 'ASTERISCO', 'DIVISION', 'PORCENTAJE'),
    ('nonassoc', 'POTENCIA'),  
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
        p[0] = []
    else: 
        p[0] = [p[1]]

#//////////////////////////////////////////////////INSTRUCCION
def p_instruccion(p):
    '''instruccion : imprimir_instr fininstr
                   | asignacion_instr fininstr
                   | declaracion_var_instr fininstr
                   | funciones_instr fininstr
                   | while_instr fininstr
                   | llamada_funcion_instr fininstr'''
    p[0] = p[1]

def p_instruccion_error(p):
    'instruccion : error fininstr'
    errores.append(Excepcion("Sintáctico", "Error sintáctico, " + str(p[1].value), p.lineno(1), find_column(input, p.slice[1])))
    p[0] = ""

#//////////////////////////////////////////////////EXPRESION
def p_expresion_parentesis(p):
    'expresion : PARENTESISA expresion PARENTESISC'
    p[0] = p[2]

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

def p_expresion_identificador(p):
    'expresion : ID'
    p[0] = Identificador(p[1], p.lineno(1), find_column(input, p.slice[1]))

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

def p_expresion_binaria_relacional(p):
    '''expresion : expresion IGUALIGUAL expresion
                 | expresion DIFERENTE expresion
                 | expresion MENOR expresion
                 | expresion MAYOR expresion
                 | expresion MENORIGUAL expresion
                 | expresion MAYORIGUAL expresion'''
    
    if p[2] == '==':
        p[0] = OperacionRelacional(OperadorRelacional.IGUALIGUAL, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '!=':
        p[0] = OperacionRelacional(OperadorRelacional.DIFERENTE, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '<':
        p[0] = OperacionRelacional(OperadorRelacional.MENOR, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '>':
        p[0] = OperacionRelacional(OperadorRelacional.MAYOR, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '<=':
        p[0] = OperacionRelacional(OperadorRelacional.MENORIGUAL, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '>=':
        p[0] = OperacionRelacional(OperadorRelacional.MAYORIGUAL, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))

def p_expresion_binaria_logica(p):
    '''expresion : expresion AND expresion
                 | expresion OR expresion'''

    if p[2] == '&&':
        p[0] = OperacionLogica(OperadorLogico.AND, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '||':
        p[0] = OperacionLogica(OperadorLogico.OR, p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))

def p_expresion_unaria(p):
    '''expresion : NOT expresion %prec UNOT
                 | MENOS expresion %prec UMINUS'''

    if p[1] == '!':
        p[0] = OperacionLogica(OperadorLogico.NOT, p[2], None, p.lineno(1), find_column(input, p.slice[1]))
    elif p[1] == '-':
        p[0] = OperacionAritmetica(OperadorAritmetico.UMENOS, p[2], None, p.lineno(1), find_column(input, p.slice[1]))


#//////////////////////////////////////////////////BOOLEAN
def p_bandera(p):
    '''bandera : TRUE
               | FALSE'''
    p[0] = Primitivos(Tipo.BANDERA, p[1], p.lineno(1), find_column(input, p.slice[1]))

#//////////////////////////////////////////////////TIPO DE DATOS
def p_tipo_datos(p):
    '''tipo : INT64
            | FLOAT64
            | STRING
            | CHAR
            | BOOL'''
    if p[1].lower() == 'int64':
        p[0] = Tipo.ENTERO
    elif p[1].lower() == 'float64':
        p[0] = Tipo.DOBLE
    elif p[1].lower() == 'string':
        p[0] = Tipo.CADENA
    elif p[1].lower() == 'char':
        p[0] = Tipo.CARACTER
    elif p[1].lower() == 'bool':
        p[0] = Tipo.BANDERA

#///////////////////////////////////////////////////////////ASIGNACION DE VARIABLES
def p_asignacion_var_tipo(p):
    'asignacion_instr : ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipo'
    p[0] = AsignacionVar(p[1], p[3], p[6], p.lineno(1), find_column(input, p.slice[1]))

def p_asignacion_var(p):
    'asignacion_instr : ID IGUAL expresion'
    p[0] = AsignacionVar(p[1], p[3], None, p.lineno(1), find_column(input, p.slice[1]))    

#///////////////////////////////////////////////////////////DECLARACION DE VARIABLES LOCALES Y GLOBALES
def p_declaracion_local(p):
    'declaracion_var_instr : LOCAL ID'
    p[0] = DeclaracionVar(p[2], None, None, True, False, p.lineno(1), find_column(input, p.slice[1]))

def p_declaracion_global(p):
    'declaracion_var_instr : GLOBAL ID'
    p[0] = DeclaracionVar(p[2], None, None, False, True, p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////DECLARACION Y ASIGNACION DE VARIABLES LOCALES Y GLOBALES
def p_declaracion_global_asignacion_var_tipo(p):
    'declaracion_var_instr : GLOBAL ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipo'
    p[0] = DeclaracionVar(p[2], p[4], p[7], False, True, p.lineno(1), find_column(input, p.slice[1]))    

def p_declaracion_local_asignacion_var_tipo(p):
    'declaracion_var_instr : LOCAL ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipo'
    p[0] = DeclaracionVar(p[2], p[4], p[7], True, False, p.lineno(1), find_column(input, p.slice[1]))    

def p_declaracion_global_asignacion_var(p):
    'declaracion_var_instr : GLOBAL ID IGUAL expresion'
    p[0] = DeclaracionVar(p[2], p[4], None, False, True, p.lineno(1), find_column(input, p.slice[1]))    

def p_declaracion_local_asignacion_var(p):
    'declaracion_var_instr : LOCAL ID IGUAL expresion'
    p[0] = DeclaracionVar(p[2], p[4], None, True, False, p.lineno(1), find_column(input, p.slice[1]))    

#//////////////////////////////////////////////////IMPRIMIR
def p_imprimir(p):
    'imprimir_instr : PRINT PARENTESISA expresion PARENTESISC'
    p[0] = Imprimir(p[3], False, p.lineno(1), find_column(input, p.slice[1]))

def p_imprimirln(p):
    'imprimir_instr : PRINTLN PARENTESISA expresion PARENTESISC'
    p[0] = Imprimir(p[3], True, p.lineno(1), find_column(input, p.slice[1]))

#//////////////////////////////////////////////////FUNCIONES
def p_funciones(p):
    'funciones_instr : FUNCTION ID PARENTESISA PARENTESISC instrucciones END'
    p[0] = Funcion(p[2], None, p[5], p.lineno(1), find_column(input, p.slice[1]))

def p_funciones_parametros(p):
    'funciones_instr : FUNCTION ID PARENTESISA parametros PARENTESISC instrucciones END'
    p[0] = Funcion(p[1], p[4], p[6], p.lineno(1), find_column(input, p.slice[1]))

#//////////////////////////////////////////////////PARAMETROS DE FUNCION
def p_parametros_funcion(p):
    'parametros : parametros COMA parametro'
    p[1].append(p[3])
    p[0] = p[1] 

def p_parametros_parametro(p):
    'parametros : parametro'
    p[0] = [p[1]]

#//////////////////////////////////////////////////PARAMETRO DE FUNCION
def p_parametro_tipo(p):
    'parametro : ID DOSPUNTOS DOSPUNTOS tipo'
    p[0] = {'tipo' : p[4], 'dimensiones' : None, 'identificador' : p[1]}

def p_parametro(p):
    'parametro : ID'
    p[0] = {'tipo' : None, 'dimensiones' : None, 'identificador' : p[1]}

#//////////////////////////////////////////////////LLAMADA FUNCION
def p_llamada_funcion(p):
    'llamada_funcion_instr : ID PARENTESISA PARENTESISC'
    p[0] = LlamadaFuncion(p[1], [], p.lineno(1), find_column(input, p.slice[1]))

#//////////////////////////////////////////////////WHILE
def p_While(p):
    'while_instr : WHILE expresion instrucciones END'
    p[0] = While(p[2], p[3], p.lineno(1), find_column(input, p.slice[1]))

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
    ast.updateConsolaln(error.toString())
    

for instruccion in ast.getInstrucciones():
    if isinstance(instruccion, Funcion):
        ast.addFuncion(instruccion)
    else:
        valor = instruccion.interpretar(ast, TSGlobal)
        if isinstance(valor, Excepcion):
            ast.getExcepciones().append(valor)
            ast.updateConsolaln(valor.toString())

print(ast.getConsola())


'''i = 0::Int64;
while i <= 10
    println(i);
    
end;
    '''

'''x = (3*5)::Int64;
str = "Saludo";

function ejemplo()
    global str = "Ejemplo";
    x = 0;
    i = 1;
    while i < 5
        local x = 0::Int64;
        x = i *2;
        println(x);
        i = i + 1;
    end;
    println(x);
end;

ejemplo();

println(x);
println(str);
    '''

    


