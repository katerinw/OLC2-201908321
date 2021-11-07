''' Segundo semestre 2021 FASE 2 '''

from os import write
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
from Instrucciones.Asignacion_Declaracion_Variables.DeclaracionVar import DeclaracionVar
from Instrucciones.Asignacion_Declaracion_Variables.AsignacionVar import AsignacionVar
from Instrucciones.Sentencias_Transferencia.Continue import Continue
from Instrucciones.Funciones.LlamadaFuncion import LlamadaFuncion
from Expresiones.Aritmeticas.Multiplicacion import Multiplicacion
from Instrucciones.Sentencias_Transferencia.Return import Return
from Expresiones.Primitivos.NegativeValue import NegativeValue
from Expresiones.Primitivos.Identificador import Identificador
from Instrucciones.Sentencias_Transferencia.Break import Break
from Expresiones.Primitivos.BooleanValue import BooleanValue
from Expresiones.Primitivos.NothingValue import NothingValue
from Expresiones.Relacionales.IgualIgual import IgualIgual
from Expresiones.Primitivos.DoubleValue import DoubleValue
from Expresiones.Primitivos.StringValue import StringValue
from Expresiones.Relacionales.MayorIgual import MayorIgual
from Expresiones.Relacionales.MenorIgual import MenorIgual
from Instrucciones.Sentencias_Ciclicas.While import While
from Expresiones.Relacionales.Diferente import Diferente
from Expresiones.Primitivos.CharValue import CharValue
from Expresiones.Aritmeticas.Potencia import Potencia
from Instrucciones.Funciones.Imprimir import Imprimir
from Expresiones.Aritmeticas.Division import Division
from Instrucciones.Sentencias_Ciclicas.For import For
from Expresiones.Primitivos.IntValue import IntValue
from Instrucciones.Funciones.Funcion import Funcion
from Instrucciones.Sentencias_Control.If import If
from Expresiones.Aritmeticas.Modulo import Modulo
from Expresiones.Relacionales.Mayor import Mayor
from Expresiones.Relacionales.Menor import Menor
from Expresiones.Aritmeticas.Resta import Resta
from Expresiones.Aritmeticas.Suma import Suma
from Nativas.FuncPotencia import FuncPotencia
from Nativas.PrintString import PrintString
from Expresiones.Logicas.And import And
from Expresiones.Logicas.Not import Not
from Expresiones.Logicas.Or import Or
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
    '''instruccion : llamada_funcion_struct_instr fininstr 
                   | declaracion_var_instr fininstr
                   | llamada_funcion_instr fininstr
                   | modificacion_struct fininstr
                   | modificar_arreglo fininstr
                   | asignacion_instr fininstr
                   | funciones_instr fininstr
                   | continue_instr fininstr
                   | imprimir_instr fininstr
                   | structs_instr fininstr
                   | return_instr fininstr
                   | while_instr fininstr
                   | break_instr fininstr
                   | push_instr fininstr
                   | for_instr fininstr
                   | pop_instr fininstr
                   | if_instr fininstr'''
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
    p[0] = NothingValue('NULL', Tipo.NULO, p.lineno(1), find_column(input, p.slice[1]))

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
        p[0] = Suma(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '-':
        p[0] = Resta(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '*':
        p[0] = Multiplicacion(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '/':
        p[0] = Division(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '^':
        p[0] = Potencia(p[1], p[3],p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '%':
        p[0] = Modulo(p[1], p[3],p.lineno(2), find_column(input, p.slice[2]))

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
        p[0] = And(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))
    elif p[2] == '||':
        p[0] = Or(p[1], p[3], p.lineno(2), find_column(input, p.slice[2]))

def p_expresion_unaria(p):
    'expresion : NOT expresion %prec UNOT'
    p[0] = Not(p[2], p.lineno(1), find_column(input, p.slice[1]))

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
    p[0] = AsignacionVar(p[1], p[3], p[6], p.lineno(1), find_column(input, p.slice[1]))

def p_asignacion_var(p):
    'asignacion_instr : ID IGUAL expresion'
    if isinstance(p[3], list):
        p[0] = ''
    else:
        p[0] = AsignacionVar(p[1], p[3], None, p.lineno(1), find_column(input, p.slice[1])) 

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
    value = NothingValue('NULL', Tipo.NULO, p.lineno(1), find_column(input, p.slice[1]))
    p[0] = DeclaracionVar(p[2], value, Tipo.NULO, True, False, p.lineno(1), find_column(input, p.slice[1]))

def p_declaracion_global(p):
    'declaracion_var_instr : GLOBAL ID'
    value = NothingValue('NULL', Tipo.NULO, p.lineno(1), find_column(input, p.slice[1]))
    p[0] = DeclaracionVar(p[2], value, Tipo.NULO, False, True, p.lineno(1), find_column(input, p.slice[1]))

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

#///////////////////////////////////////////////////////////IMPRIMIR
def p_imprimir_vacio(p):
    'imprimir_instr : PRINT PARENTESISA PARENTESISC'
    p[0] = Imprimir(None, False, p.lineno(1), find_column(input, p.slice[1]))

def p_imprimirln_vacio(p):
    'imprimir_instr : PRINTLN PARENTESISA PARENTESISC'
    p[0] = Imprimir(None, True, p.lineno(1), find_column(input, p.slice[1]))

def p_imprimir_expresiones_coma(p):
    'imprimir_instr : PRINT PARENTESISA expresiones_coma PARENTESISC'
    p[0] = Imprimir(p[3], False, p.lineno(1), find_column(input, p.slice[1]))

def p_imprimirln_expresiones_coma(p):
    'imprimir_instr : PRINTLN PARENTESISA expresiones_coma PARENTESISC'
    p[0] = Imprimir(p[3], True, p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////FUNCIONES
def p_funciones(p):
    'funciones_instr : FUNCTION ID PARENTESISA PARENTESISC instrucciones END'
    p[0] = Funcion(p[2], [], p[5], p.lineno(1), find_column(input, p.slice[1]))

def p_funciones_parametros(p):
    'funciones_instr : FUNCTION ID PARENTESISA parametros PARENTESISC instrucciones END'
    p[0] = Funcion(p[2], p[4], p[6], p.lineno(1), find_column(input, p.slice[1]))

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
    p[0] = LlamadaFuncion(p[1], [], p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////LLAMADA FUNCION / LLAMADA STRUCT
def p_llamada_funcion_parametros(p):
    'llamada_funcion_struct_instr : ID PARENTESISA parametros_llamada PARENTESISC'
    p[0] = LlamadaFuncion(p[1], p[3], p.lineno(1), find_column(input, p.slice[1]))
    
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
    p[0] = While(p[2], p[3], p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////FOR
def p_for_string(p): #Lo hace con strings y arreglos
    'for_instr : FOR ID IN expresion instrucciones END'
    p[0] = For(p[2], p[4], None, p[5] ,p.lineno(1), find_column(input, p.slice[1]))

def p_for_rango(p): #Lo hace con rango
    'for_instr : FOR ID IN expresion DOSPUNTOS expresion instrucciones END'
    p[0] = For(p[2], p[4], p[6], p[7], p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////SENTENCIAS DE TRANSFERENCIA
def p_sentencia_transferencia_return_expresion(p):
    'return_instr : RETURN expresion'
    p[0] = Return(p[2], p.lineno(1), find_column(input, p.slice[1]))

def p_sentencia_transferencia_return(p):
    'return_instr : RETURN'
    p[0] = Return(None, p.lineno(1), find_column(input, p.slice[1]))

def p_sentencia_transferencia_break(p):
    'break_instr : BREAK'
    p[0] = Break(p.lineno(1), find_column(input, p.slice[1]))

def p_sentencia_transferencia_continue(p):
    'continue_instr : CONTINUE'
    p[0] = Continue(p.lineno(1), find_column(input, p.slice[1]))

#///////////////////////////////////////////////////////////SENTENCIAS DE CONTROL
def p_if(p):
    'if_instr : IF expresion instrucciones END'
    p[0] = If(p[2], p[3], None, None, p.lineno(1), find_column(input, p.slice[1]))

def p_if_elseif_else(p):
    'if_instr : IF expresion instrucciones elseifs_instr ELSE instrucciones END'
    p[0] = If(p[2], p[3], p[6], p[4], p.lineno(1), find_column(input, p.slice[1]))

def p_if_elseif(p):
    'if_instr : IF expresion instrucciones elseifs_instr END'
    p[0] = If(p[2], p[3], None, p[4], p.lineno(1), find_column(input, p.slice[1]))

def p_if_else(p):
    'if_instr : IF expresion instrucciones ELSE instrucciones END'
    p[0] = If(p[2], p[3], p[5], None, p.lineno(1), find_column(input, p.slice[1]))

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
    p[0] = If(p[2], p[3], None, None, p.lineno(1), find_column(input, p.slice[1]))

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

def crearNativas(ast): #Creacion y declaracion de funciones nativas
    identificador = 'Print_String_armc'
    parametros = [{'tipo': Tipo.CADENA, 'dimensiones': None, 'identificador': 'Print_String_armc'}]
    instrucciones = []
    printstring = PrintString(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(printstring)

    identificador = 'Potencia_armc'
    parametros = [{'tipo': Tipo.ENTERO, 'dimensiones': None, 'identificador': 'Potencia_armc'}]
    instrucciones = []
    potencia = FuncPotencia(identificador, parametros, instrucciones, -1, -1)
    ast.addFuncion(potencia)

    

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
label = 0
temporal = 0
indices = {'temporal' : 0, 'label' : 0}
generator = Generador(indices)
generatorFunction = Generador(indices)
crearNativas(ast)

for func in ast.getFunciones():
    valor = func.interpretar(ast, TSGlobal, generatorFunction)
    if isinstance(valor, Excepcion):
        ast.getExcepciones().append(valor)
        ast.setConsola('')
    else:
        generatorFunction.addInstruction(ast.getConsola())
        ast.setConsola('')


for error in errores: #Captura de errores lexicos y sintacticos 
    ast.getExcepciones().append(error)
    ast.updateConsolaln(error.toString())


for instruccion in ast.getInstrucciones():
    if isinstance(instruccion, Funcion):
        ast.addFuncion(instruccion)
        valor = instruccion.interpretar(ast, TSGlobal, generatorFunction)
    else:
        valor = instruccion.interpretar(ast, TSGlobal, generator)
    if isinstance(valor, Excepcion):
        ast.getExcepciones().append(valor)
        ast.setConsola('')
    else:
        if isinstance(instruccion, Funcion):
            generatorFunction.addInstruction(ast.getConsola())
            ast.setConsola('')
        else:
            generator.addInstruction(ast.getConsola())
            ast.setConsola('')


file = open("./Salida.txt", "w")
file.write(generator.getCode(generatorFunction))
file.close()

#print(generator.getCode(generatorFunction))
#print(ast.getConsola())


'''
for i in 1:4
	println(i);
end;

x = 0::Int64;
x = x + 1;
'''