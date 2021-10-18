''' Segundo semestre 2021 FASE 2 '''

import re
import sys
sys.setrecursionlimit(3000)

#LISTA DE ERRORES
errores = []


reservedWords = {
    'true': 'TRUE',
    'false': 'FALSE',
    'nothing' : 'NOTHING',
    'Int64': 'INT64',
    'Float64': 'FLOAT64',
    'String': 'STRING',
    'Bool': 'BOOL',
    'Char': 'CHAR',
    'struct': 'STRUCT',
    'print': 'PRINT',
    'println': 'PRINTLN',
    'function' : 'FUNCTION',
    'end' : 'END',
    'while' : 'WHILE',
    'for' : 'FOR',
    'in' : 'IN',
    'local' : 'LOCAL',
    'global' : 'GLOBAL',
    'return' : 'RETURN',
    'break' : 'BREAK',
    'continue' : 'CONTINUE',
    'string' : 'SSTRING',
    'parse' : 'PARSE',
    'pop' : 'POP',
    'push' : 'PUSH',
    'if' : 'IF',
    'else' : 'ELSE',
    'elseif' : 'ELSEIF',
    'mutable' : 'MUTABLE'
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
    'LLAVEA',
    'LLAVEC',
    'CORCHETEA',
    'CORCHETEC',
    'PUNTOCOMA',
    'DOSPUNTOS',
    'COMA',
    'PUNTO',
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
t_LLAVEA = r'\{'
t_LLAVEC = r'\}'
t_CORCHETEA = r'\['
t_CORCHETEC = r'\]'
t_PUNTOCOMA = r';' 
t_DOSPUNTOS = r':' 
t_COMA = r','
t_PUNTO = r'\.'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservedWords.get(t.value,'ID') #Cecha las palbras reservadas
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
t_ignore = " \t\r"

#Construyendo un analizador
import ply.lex as lex
lexer = lex.lex(reflags = re.VERBOSE)

#Importaciones
from Expresiones.Aritmeticas.Multiplicacion import Multiplicacion
from Expresiones.Primitivos.NegativeValue import NegativeValue
from Expresiones.Primitivos.BooleanValue import BooleanValue
from Expresiones.Relacionales.IgualIgual import IgualIgual
from Expresiones.Primitivos.DoubleValue import DoubleValue
from Expresiones.Primitivos.StringValue import StringValue
from Expresiones.Relacionales.MayorIgual import MayorIgual
from Expresiones.Relacionales.MenorIgual import MenorIgual
from Expresiones.Relacionales.Diferente import Diferente
from Expresiones.Primitivos.CharValue import CharValue
from Instrucciones.Funciones.Imprimir import Imprimir
from Expresiones.Aritmeticas.Division import Division
from Expresiones.Primitivos.IntValue import IntValue
from Expresiones.Relacionales.Mayor import Mayor
from Expresiones.Relacionales.Menor import Menor
from Expresiones.Aritmeticas.Resta import Resta
from Expresiones.Aritmeticas.Suma import Suma
from TS.Excepcion import Excepcion
from TS.Tipo import Tipo


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

#///////////////////////////////////////////////////////////FINAL INSTRUCCION
def p_fininstr(p):
    'fininstr : PUNTOCOMA'

#///////////////////////////////////////////////////////////INSTRUCCIONES
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

#///////////////////////////////////////////////////////////INSTRUCCION
def p_instruccion(p):
    '''instruccion : imprimir_instr fininstr
                   | asignacion_instr fininstr
                   | declaracion_var_instr fininstr
                   | modificar_arreglo fininstr
                   | funciones_instr fininstr
                   | while_instr fininstr
                   | llamada_funcion_instr fininstr
                   | break_instr fininstr
                   | continue_instr fininstr
                   | return_instr fininstr
                   | if_instr fininstr
                   | for_instr fininstr
                   | pop_instr fininstr
                   | push_instr fininstr
                   | structs_instr fininstr
                   | llamada_funcion_struct_instr fininstr
                   | modificacion_struct fininstr'''
    p[0] = p[1]

def p_instruccion_error(p):
    'instruccion : error fininstr'
    errores.append(Excepcion("Sintáctico", "Error sintáctico, " + str(p[1].value), p.lineno(1), find_column(input, p.slice[1])))
    p[0] = ""

#///////////////////////////////////////////////////////////EXPRESION
def p_expresion_parentesis(p):
    'expresion : PARENTESISA expresion PARENTESISC'
    p[0] = p[2]

def p_expresion_string(p):
    'expresion : CADENA'
    p[0] = StringValue(p[1], Tipo.CADENA, p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_character(p):
    'expresion : CARACTER'
    p[0] = CharValue(p[1], Tipo.CARACTER, p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_integer(p):
    'expresion : ENTERO'
    p[0] = IntValue(p[1], Tipo.ENTERO, p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_integer_negative(p):
    'expresion : MENOS ENTERO %prec UMINUS'
    p[0] = NegativeValue(p[2], Tipo.ENTERO, p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_double(p):
    'expresion : DOBLE'
    p[0] = DoubleValue(p[1], Tipo.DOBLE, p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_double_negative(p):
    'expresion : MENOS DOBLE %prec UMINUS'
    p[0] = NegativeValue(p[2], Tipo.DOBLE, p.lineno(1), find_column(input, p.slice[1]))

def p_expresion_nothing(p):
    'expresion : NOTHING'
    p[0] = ''

def p_expresion_identificador(p):
    'expresion : ID'
    p[0] = ''

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
        p[0] = Suma(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '-':
        p[0] = Resta(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '*':
        p[0] = Multiplicacion(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '/':
        p[0] = Division(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '^':
        p[0] = ''
    elif p[2] == '%':
        p[0] = ''

def p_expresion_binaria_relacional(p):
    '''expresion : expresion IGUALIGUAL expresion
                 | expresion DIFERENTE expresion
                 | expresion MENOR expresion
                 | expresion MAYOR expresion
                 | expresion MENORIGUAL expresion
                 | expresion MAYORIGUAL expresion'''
    
    if p[2] == '==':
        p[0] = IgualIgual(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '!=':
        p[0] = Diferente(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '<':
        p[0] = Menor(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '>':
        p[0] = Mayor(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '<=':
        p[0] = MenorIgual(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '>=':
        p[0] = MayorIgual(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))

def p_expresion_binaria_logica(p):
    '''expresion : expresion AND expresion
                 | expresion OR expresion'''

    if p[2] == '&&':
        p[0] = ''
    elif p[2] == '||':
        p[0] = ''

def p_expresion_unaria(p):
    'expresion : NOT expresion %prec UNOT'

    if p[1] == '!':
        p[0] = ''

def p_expresion_llamada_funcion(p):
    'expresion : llamada_funcion_instr'
    p[0] = p[1]

def p_expresion_llamada_funcion_struct(p):
    'expresion : llamada_funcion_struct_instr'
    p[0] = p[1]

def p_lista_expresiones(p):
    'expresion : CORCHETEA expresiones_coma CORCHETEC'
    p[0] = p[2]

def p_acceso_arreglo_expresion(p):
    'expresion : acceso_arreglo'
    p[0] = p[1]

def p_push_expresion(p):
    'expresion : push_instr'
    p[0] = p[1]

def p_pop_expresion(p):
    'expresion : pop_instr'
    p[0] = p[1]

def p_acceso_struct_expresion(p):
    'expresion : acceso_struct'
    p[0] = p[1]

#//////////////////////////////////////////NATIVAS
def p_parse_int64(p):
    'expresion : PARSE PARENTESISA INT64 COMA expresion PARENTESISC'
    p[0] = ''

def p_parse_float64(p):
    'expresion : PARSE PARENTESISA FLOAT64 COMA expresion PARENTESISC'
    p[0] = ''

def p_parse_string(p):
    'expresion : SSTRING PARENTESISA expresion PARENTESISC'
    p[0] = ''

def p_pop_instr(p):
    'pop_instr : POP NOT PARENTESISA expresion PARENTESISC'
    p[0] = ''

def p_push_instr(p):
    'push_instr : PUSH NOT PARENTESISA expresion COMA expresion PARENTESISC'
    p[0] = ''

#///////////////////////////////////////////////////////////EXPRESIONES COMA
def p_expresiones_coma_expresiones_coma_epxresion(p):
    'expresiones_coma : expresiones_coma COMA expresion'
    p[1].append(p[3])
    p[0] = p[1]

def p_expresiones_coma_expresion(p):
    'expresiones_coma : expresion'
    p[0] = [p[1]]

#///////////////////////////////////////////////////////////BOOLEAN
def p_bandera(p):
    '''bandera : TRUE
               | FALSE'''
    if p[1].lower() == 'true':
        p[1] = True
    elif p[1].lower() == 'false':
        p[1] == False

    p[0] = BooleanValue(p[1], Tipo.BANDERA, p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////TIPO DE DATOS
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
    p[0] = ''

def p_asignacion_var(p):
    'asignacion_instr : ID IGUAL expresion'
    if isinstance(p[3], list):
        p[0] = ''
    else:
        p[0] = '' 

#///////////////////////////////////////////////////////////MODIFICAR ARREGLO
def p_modificar_arreglo(p):
    'modificar_arreglo : ID lista_dimensiones IGUAL expresion'
    p[0] = ''

#///////////////////////////////////////////////////////////ACCESO ARREGLO
def p_acceso_arreglo(p):
    'acceso_arreglo : ID lista_dimensiones'
    p[0] = ''
 
def p_lista_dimensiones(p):
    'lista_dimensiones : lista_dimensiones CORCHETEA expresion CORCHETEC' 
    p[1].append(p[3])
    p[0] = p[1]

def p_lista_dimensione(p):
    'lista_dimensiones : CORCHETEA expresion CORCHETEC'
    p[0] = [p[2]] 

#///////////////////////////////////////////////////////////DECLARACION DE VARIABLES LOCALES Y GLOBALES
def p_declaracion_local(p):
    'declaracion_var_instr : LOCAL ID'
    p[0] = ''

def p_declaracion_global(p):
    'declaracion_var_instr : GLOBAL ID'
    p[0] = ''

def p_declaracion(p):
    'declaracion_var_instr : ID'
    p[0] = ''

#///////////////////////////////////////////////////////////DECLARACION Y ASIGNACION DE VARIABLES LOCALES Y GLOBALES
def p_declaracion_global_asignacion_var_tipo(p):
    'declaracion_var_instr : GLOBAL ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipo'
    p[0] = ''    

def p_declaracion_local_asignacion_var_tipo(p):
    'declaracion_var_instr : LOCAL ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipo'
    p[0] = ''    

def p_declaracion_global_asignacion_var(p):
    'declaracion_var_instr : GLOBAL ID IGUAL expresion'
    p[0] = ''    

def p_declaracion_local_asignacion_var(p):
    'declaracion_var_instr : LOCAL ID IGUAL expresion'
    p[0] = ''    

#///////////////////////////////////////////////////////////IMPRIMIR
def p_imprimir_vacio(p):
    'imprimir_instr : PRINT PARENTESISA PARENTESISC'
    p[0] = ''

def p_imprimirln_vacio(p):
    'imprimir_instr : PRINTLN PARENTESISA PARENTESISC'
    p[0] = ''

def p_imprimir_expresiones_coma(p):
    'imprimir_instr : PRINT PARENTESISA expresion PARENTESISC'
    p[0] = Imprimir(p[3], False, p.lineno(1), find_column(input, p.slice[1]))

def p_imprimirln_expresiones_coma(p):
    'imprimir_instr : PRINTLN PARENTESISA expresion PARENTESISC'
    p[0] = Imprimir(p[3], True, p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////FUNCIONES
def p_funciones(p):
    'funciones_instr : FUNCTION ID PARENTESISA PARENTESISC instrucciones END'
    p[0] = ''

def p_funciones_parametros(p):
    'funciones_instr : FUNCTION ID PARENTESISA parametros PARENTESISC instrucciones END'
    p[0] = ''

#///////////////////////////////////////////////////////////PARAMETROS DE FUNCION
def p_parametros_funcion(p):
    'parametros : parametros COMA parametro'
    p[1].append(p[3])
    p[0] = p[1] 

def p_parametros_parametro(p):
    'parametros : parametro'
    p[0] = [p[1]]

#///////////////////////////////////////////////////////////PARAMETRO DE FUNCION
def p_parametro_tipo(p):
    'parametro : ID DOSPUNTOS DOSPUNTOS tipo'
    p[0] = {'tipo' : p[4],'identificador' : p[1]}

def p_parametro(p):
    'parametro : ID'
    p[0] = {'tipo' : None,'identificador' : p[1]}

#///////////////////////////////////////////////////////////LLAMADA FUNCION
def p_llamada_funcion(p):
    'llamada_funcion_instr : ID PARENTESISA PARENTESISC'
    p[0] = ''

#///////////////////////////////////////////////////////////LLAMADA FUNCION / LLAMADA STRUCT
def p_llamada_funcion_parametros(p):
    'llamada_funcion_struct_instr : ID PARENTESISA parametros_llamada PARENTESISC'
    p[0] = ''
    
#///////////////////////////////////////////////////////////PARAMETOS LLAMADA FUNCION
def p_parametros_llamada_funcion(p):
    'parametros_llamada : parametros_llamada COMA expresion '
    p[1].append(p[3])
    p[0] = p[1]

def p_parametros_llamada_expresion(p):
    'parametros_llamada : expresion'
    p[0] = [p[1]]

#///////////////////////////////////////////////////////////WHILE
def p_While(p):
    'while_instr : WHILE expresion instrucciones END'
    p[0] = ''

#///////////////////////////////////////////////////////////FOR
def p_for_string(p): #Lo hace con strings y arreglos
    'for_instr : FOR declaracion_var_instr IN expresion instrucciones END'
    p[0] = ''

def p_for_rango(p): #Lo hace con rango
    'for_instr : FOR declaracion_var_instr IN expresion DOSPUNTOS expresion instrucciones END'
    p[0] = ''

#///////////////////////////////////////////////////////////SENTENCIAS DE TRANSFERENCIA
def p_sentencia_transferencia_return_expresion(p):
    'return_instr : RETURN expresion'
    p[0] = ''

def p_sentencia_transferencia_return(p):
    'return_instr : RETURN'
    p[0] = ''

def p_sentencia_transferencia_break(p):
    'break_instr : BREAK'
    p[0] = ''

def p_sentencia_transferencia_continue(p):
    'continue_instr : CONTINUE'
    p[0] = ''

#///////////////////////////////////////////////////////////SENTENCIAS DE CONTROL
def p_if(p):
    'if_instr : IF expresion instrucciones END'
    p[0] = ''

def p_if_elseif_else(p):
    'if_instr : IF expresion instrucciones elseifs_instr ELSE instrucciones END'
    p[0] = ''

def p_if_elseif(p):
    'if_instr : IF expresion instrucciones elseifs_instr END'
    p[0] = ''

def p_if_else(p):
    'if_instr : IF expresion instrucciones ELSE instrucciones END'
    p[0] = ''

def p_elseifs_elseifs_elseif(p):
    'elseifs_instr : elseifs_instr elseif_instr'
    if p[2] != "":
        p[1].append(p[2])
    p[0] = p[1] 

def p_elseifs_elseif(p):
    'elseifs_instr : elseif_instr'
    if p[1] == "":
        p[0] = []
    else:
        p[0] = [p[1]] 

def p_elseif(p):
    'elseif_instr : ELSEIF expresion instrucciones'
    p[0] = ''

#///////////////////////////////////////////////////////////STRUCTS
def p_struct(p):
    '''structs_instr : structs_inmutable
                     | structs_mutable'''
    p[0] = p[1]

def p_structs_inmutable(p):
    'structs_inmutable : STRUCT ID lista_atributos END'
    p[0] = ''

def p_structs_mutable(p):
    'structs_mutable : MUTABLE STRUCT ID lista_atributos END'
    p[0] = ''

#///////////////////////////////////////////////////////////ATRIBUTOS
def p_atributos_atributos(p):
    'lista_atributos : lista_atributos atributo fininstr'
    p[1].append(p[2])
    p[0] = p[1] 

def p_atributos(p):
    'lista_atributos : atributo fininstr'
    p[0] = [p[1]]

#///////////////////////////////////////////////////////////ATRIBUTO
def p_atributo_tipo(p):
    'atributo : ID DOSPUNTOS DOSPUNTOS tipo'
    p[0] = {'tipo' : p[4],'identificador' : p[1]}

def p_atributo(p):
    'atributo : ID'
    p[0] = {'tipo' : None,'identificador' : p[1]}

#///////////////////////////////////////////////////////////ACCESO STRUCT
def p_acceso_struct(p):
    'acceso_struct : ID PUNTO ID'
    p[0] = ''

#///////////////////////////////////////////////////////////MODIFICACION STRUCT
def p_modificacion_struct(p):
    'modificacion_struct : ID PUNTO ID IGUAL expresion'
    p[0] = ''


#Haciendo el parser


import ply.yacc as yacc
parser = yacc.yacc()

input = ''

def getErrores():
    return errores 
'''
def crearNativas(ast): #Creacion y declaracion de funciones nativas
    identificador = 'cos'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Cos$$Parametros123'}]
    instrucciones = []
    cos = Cos(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(cos)

    identificador = 'float'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': [], 'identificador': 'Float$$Parametros123'}]
    instrucciones = []
    float = Float(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(float)

    identificador = "length"
    parametros = [{'tipo': Tipo.ARREGLO, 'dimensiones': None, 'identificador': 'Length$$Parametros123'}] 
    instrucciones = []
    length = Length(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(length)

    identificador = 'log'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Log$$Parametros123'}, {'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Log$$Parametros456'}]
    instrucciones = []
    log = Log(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(log)

    identificador = 'log10'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Log10$$Parametros123'}]
    instrucciones = []
    log10 = Log10(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(log10)

    identificador = 'lowercase'
    parametros = [{'tipo': Tipo.CADENA, 'dimensiones': None, 'identificador': 'Lower$$Parametros123'}]
    instrucciones = []
    lowercase = Lower(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(lowercase)

    identificador = 'sin'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Sin$$Parametros123'}]
    instrucciones = []
    sin = Sin(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(sin)

    identificador = 'sqrt'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Sqrt$$Parametros123'}]
    instrucciones = []
    sqrt = Sqrt(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(sqrt)  

    identificador = 'tan'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': [], 'identificador': 'Tan$$Parametros123'}]
    instrucciones = []
    tan = Tan(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(tan)

    identificador = 'trunc'
    parametros = [{'tipo': Tipo.DOBLE, 'dimensiones': [], 'identificador': 'Trunc$$Parametros123'}]
    instrucciones = []
    trunc = Trunc(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(trunc)

    identificador = 'typeof'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': [], 'identificador': 'TypeOf$$Parametros123'}]
    instrucciones = []
    typeof = Typeof(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(typeof)
    
    identificador = 'uppercase'
    parametros = [{'tipo': Tipo.CADENA, 'dimensiones': [], 'identificador': 'Upper$$Parametros123'}]
    instrucciones = []
    uppercase = Upper(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(uppercase)
'''

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

from TS.TablaSimbolos import TablaSimbolos
from Generador.Generador import Generador
from TS.Arbol import Arbol

instrucciones = parse(entrada) #ARBOL AST
ast = Arbol(instrucciones)
TSGlobal = TablaSimbolos('global')
ast.setTSGlobal(TSGlobal)
generator = Generador()
#crearNativas(ast)

for error in errores: #Captura de errores lexicos y sintacticos 
    ast.getExcepciones().append(error)
    ast.updateConsolaln(error.toString())


for instruccion in ast.getInstrucciones():
    valor = instruccion.interpretar(ast, TSGlobal, generator)
    if isinstance(valor, Excepcion):
        ast.getExcepciones().append(valor)
        ast.updateConsolaln(valor.toString())

print(generator.getCode())
#print(ast.getConsola())

'''println(5+6+9+4+7+89+4+2+1+1+1+1+7);'''