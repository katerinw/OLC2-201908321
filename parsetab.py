
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'inicioleftORleftANDrightUNOTleftIGUALIGUALDIFERENTEMENORMENORIGUALMAYORMAYORIGUALleftMASMENOSleftASTERISCODIVISIONPORCENTAJEnonassocPOTENCIArightUMINUSAND ASTERISCO BOOL CADENA CARACTER CHAR COMA COS DIAGONAL DIFERENTE DIVISION DOBLE DOSPUNTOS END ENTERO FALSE FLOAT64 FOR FUNCTION GLOBAL ID IGUAL IGUALIGUAL INT64 LLAVESA LLAVESC LOCAL LOG LOG10 MAS MAYOR MAYORIGUAL MENOR MENORIGUAL MENOS NOT NOTHING OR PARENTESISA PARENTESISC PORCENTAJE POTENCIA PRINT PRINTLN PUNTOCOMA SIN SQRT STRING STRUCT TAN TRUE WHILE ignore_COMENTARIOMULTILINEA ignore_COMENTARIOUNILINEAinicio : instruccionesfininstr : PUNTOCOMAinstrucciones : instrucciones instruccioninstrucciones : instruccioninstruccion : imprimir_instr fininstr\n                   | asignacion_instr fininstr\n                   | declaracion_var_instr fininstr\n                   | funciones_instr fininstr\n                   | while_instr fininstr\n                   | llamada_funcion_instr fininstrinstruccion : error fininstrexpresion : PARENTESISA expresion PARENTESISCexpresion : CADENAexpresion : CARACTERexpresion : ENTEROexpresion : DOBLEexpresion : NOTHINGexpresion : IDexpresion : banderaexpresion : expresion MAS expresion\n                 | expresion MENOS expresion\n                 | expresion ASTERISCO expresion\n                 | expresion DIVISION expresion\n                 | expresion POTENCIA expresion\n                 | expresion PORCENTAJE expresionexpresion : expresion IGUALIGUAL expresion\n                 | expresion DIFERENTE expresion\n                 | expresion MENOR expresion\n                 | expresion MAYOR expresion\n                 | expresion MENORIGUAL expresion\n                 | expresion MAYORIGUAL expresionexpresion : expresion AND expresion\n                 | expresion OR expresionexpresion : NOT expresion %prec UNOT\n                 | MENOS expresion %prec UMINUSbandera : TRUE\n               | FALSEtipo : INT64\n            | FLOAT64\n            | STRING\n            | CHAR\n            | BOOLasignacion_instr : ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipoasignacion_instr : ID IGUAL expresiondeclaracion_var_instr : LOCAL IDdeclaracion_var_instr : GLOBAL IDimprimir_instr : PRINT PARENTESISA expresion PARENTESISCimprimir_instr : PRINTLN PARENTESISA expresion PARENTESISCfunciones_instr : FUNCTION ID PARENTESISA PARENTESISC instrucciones ENDfunciones_instr : FUNCTION ID PARENTESISA parametros PARENTESISC instrucciones ENDparametros : parametros COMA parametroparametros : parametroparametro : ID DOSPUNTOS DOSPUNTOS tipoparametro : IDllamada_funcion_instr : ID PARENTESISA PARENTESISCwhile_instr : WHILE expresion instrucciones END'
    
_lr_action_items = {'error':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[10,10,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,10,-13,-14,-15,-16,-17,-18,-19,-36,-37,10,-35,-34,10,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,10,10,10,]),'PRINT':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[11,11,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,11,-13,-14,-15,-16,-17,-18,-19,-36,-37,11,-35,-34,11,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,11,11,11,]),'PRINTLN':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[12,12,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,12,-13,-14,-15,-16,-17,-18,-19,-36,-37,12,-35,-34,12,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,12,12,12,]),'ID':([0,2,3,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,34,35,36,37,38,39,40,41,42,43,44,45,46,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,97,106,],[13,13,-4,31,32,33,41,-3,-5,-2,-6,-7,-8,-9,-10,-11,41,41,41,13,41,-13,-14,-15,-16,-17,-18,-19,41,41,-36,-37,73,13,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-35,-34,13,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,13,13,73,13,]),'LOCAL':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[14,14,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,14,-13,-14,-15,-16,-17,-18,-19,-36,-37,14,-35,-34,14,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,14,14,14,]),'GLOBAL':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[15,15,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,15,-13,-14,-15,-16,-17,-18,-19,-36,-37,15,-35,-34,15,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,15,15,15,]),'FUNCTION':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[16,16,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,16,-13,-14,-15,-16,-17,-18,-19,-36,-37,16,-35,-34,16,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,16,16,16,]),'WHILE':([0,2,3,18,19,20,21,22,23,24,25,26,34,36,37,38,39,40,41,42,45,46,52,68,69,74,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,95,96,106,],[17,17,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,17,-13,-14,-15,-16,-17,-18,-19,-36,-37,17,-35,-34,17,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,17,17,17,]),'$end':([1,2,3,18,19,20,21,22,23,24,25,26,],[0,-1,-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,]),'END':([3,18,19,20,21,22,23,24,25,26,52,95,106,],[-4,-3,-5,-2,-6,-7,-8,-9,-10,-11,77,105,109,]),'PUNTOCOMA':([4,5,6,7,8,9,10,31,32,36,37,38,39,40,41,42,45,46,49,50,68,69,70,71,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,98,99,100,101,102,103,105,109,],[20,20,20,20,20,20,20,-45,-46,-13,-14,-15,-16,-17,-18,-19,-36,-37,-44,-55,-35,-34,-47,-48,-56,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,-43,-38,-39,-40,-41,-42,-49,-50,]),'PARENTESISA':([11,12,13,17,27,28,29,33,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[27,28,30,35,35,35,35,51,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'IGUAL':([13,],[29,]),'CADENA':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,]),'CARACTER':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,]),'ENTERO':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,38,]),'DOBLE':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,]),'NOTHING':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,]),'NOT':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,]),'MENOS':([17,27,28,29,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[43,43,43,43,54,43,-13,-14,-15,-16,-17,-18,-19,43,43,-36,-37,54,54,54,43,43,43,43,43,43,43,43,43,43,43,43,43,43,54,-35,54,-20,-21,-22,-23,-24,-25,54,54,54,54,54,54,54,54,-12,]),'TRUE':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,]),'FALSE':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,]),'PARENTESISC':([30,36,37,38,39,40,41,42,45,46,47,48,51,67,68,69,73,75,76,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,99,100,101,102,103,107,108,],[50,-13,-14,-15,-16,-17,-18,-19,-36,-37,70,71,74,92,-35,-34,-54,96,-52,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,-38,-39,-40,-41,-42,-51,-53,]),'MAS':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[53,-13,-14,-15,-16,-17,-18,-19,-36,-37,53,53,53,53,-35,53,-20,-21,-22,-23,-24,-25,53,53,53,53,53,53,53,53,-12,]),'ASTERISCO':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[55,-13,-14,-15,-16,-17,-18,-19,-36,-37,55,55,55,55,-35,55,55,55,-22,-23,-24,-25,55,55,55,55,55,55,55,55,-12,]),'DIVISION':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[56,-13,-14,-15,-16,-17,-18,-19,-36,-37,56,56,56,56,-35,56,56,56,-22,-23,-24,-25,56,56,56,56,56,56,56,56,-12,]),'POTENCIA':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[57,-13,-14,-15,-16,-17,-18,-19,-36,-37,57,57,57,57,-35,57,57,57,57,57,None,57,57,57,57,57,57,57,57,57,-12,]),'PORCENTAJE':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[58,-13,-14,-15,-16,-17,-18,-19,-36,-37,58,58,58,58,-35,58,58,58,-22,-23,-24,-25,58,58,58,58,58,58,58,58,-12,]),'IGUALIGUAL':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[59,-13,-14,-15,-16,-17,-18,-19,-36,-37,59,59,59,59,-35,59,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,59,59,-12,]),'DIFERENTE':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[60,-13,-14,-15,-16,-17,-18,-19,-36,-37,60,60,60,60,-35,60,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,60,60,-12,]),'MENOR':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[61,-13,-14,-15,-16,-17,-18,-19,-36,-37,61,61,61,61,-35,61,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,61,61,-12,]),'MAYOR':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[62,-13,-14,-15,-16,-17,-18,-19,-36,-37,62,62,62,62,-35,62,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,62,62,-12,]),'MENORIGUAL':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[63,-13,-14,-15,-16,-17,-18,-19,-36,-37,63,63,63,63,-35,63,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,63,63,-12,]),'MAYORIGUAL':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[64,-13,-14,-15,-16,-17,-18,-19,-36,-37,64,64,64,64,-35,64,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,64,64,-12,]),'AND':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[65,-13,-14,-15,-16,-17,-18,-19,-36,-37,65,65,65,65,-35,-34,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,65,-12,]),'OR':([34,36,37,38,39,40,41,42,45,46,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,],[66,-13,-14,-15,-16,-17,-18,-19,-36,-37,66,66,66,66,-35,-34,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,]),'DOSPUNTOS':([36,37,38,39,40,41,42,45,46,49,68,69,72,73,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,94,],[-13,-14,-15,-16,-17,-18,-19,-36,-37,72,-35,-34,93,94,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-33,-12,104,]),'COMA':([73,75,76,99,100,101,102,103,107,108,],[-54,97,-52,-38,-39,-40,-41,-42,-51,-53,]),'INT64':([93,104,],[99,99,]),'FLOAT64':([93,104,],[100,100,]),'STRING':([93,104,],[101,101,]),'CHAR':([93,104,],[102,102,]),'BOOL':([93,104,],[103,103,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'inicio':([0,],[1,]),'instrucciones':([0,34,74,96,],[2,52,95,106,]),'instruccion':([0,2,34,52,74,95,96,106,],[3,18,3,18,3,18,3,18,]),'imprimir_instr':([0,2,34,52,74,95,96,106,],[4,4,4,4,4,4,4,4,]),'asignacion_instr':([0,2,34,52,74,95,96,106,],[5,5,5,5,5,5,5,5,]),'declaracion_var_instr':([0,2,34,52,74,95,96,106,],[6,6,6,6,6,6,6,6,]),'funciones_instr':([0,2,34,52,74,95,96,106,],[7,7,7,7,7,7,7,7,]),'while_instr':([0,2,34,52,74,95,96,106,],[8,8,8,8,8,8,8,8,]),'llamada_funcion_instr':([0,2,34,52,74,95,96,106,],[9,9,9,9,9,9,9,9,]),'fininstr':([4,5,6,7,8,9,10,],[19,21,22,23,24,25,26,]),'expresion':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[34,47,48,49,67,68,69,78,79,80,81,82,83,84,85,86,87,88,89,90,91,]),'bandera':([17,27,28,29,35,43,44,53,54,55,56,57,58,59,60,61,62,63,64,65,66,],[42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,]),'parametros':([51,],[75,]),'parametro':([51,97,],[76,107,]),'tipo':([93,104,],[98,108,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> inicio","S'",1,None,None,None),
  ('inicio -> instrucciones','inicio',1,'p_inicio','grammar.py',203),
  ('fininstr -> PUNTOCOMA','fininstr',1,'p_fininstr','grammar.py',208),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_instrucciones_instrucciones_instruccion','grammar.py',212),
  ('instrucciones -> instruccion','instrucciones',1,'p_instrucciones_instruccion','grammar.py',218),
  ('instruccion -> imprimir_instr fininstr','instruccion',2,'p_instruccion','grammar.py',226),
  ('instruccion -> asignacion_instr fininstr','instruccion',2,'p_instruccion','grammar.py',227),
  ('instruccion -> declaracion_var_instr fininstr','instruccion',2,'p_instruccion','grammar.py',228),
  ('instruccion -> funciones_instr fininstr','instruccion',2,'p_instruccion','grammar.py',229),
  ('instruccion -> while_instr fininstr','instruccion',2,'p_instruccion','grammar.py',230),
  ('instruccion -> llamada_funcion_instr fininstr','instruccion',2,'p_instruccion','grammar.py',231),
  ('instruccion -> error fininstr','instruccion',2,'p_instruccion_error','grammar.py',235),
  ('expresion -> PARENTESISA expresion PARENTESISC','expresion',3,'p_expresion_parentesis','grammar.py',241),
  ('expresion -> CADENA','expresion',1,'p_expresion_string','grammar.py',245),
  ('expresion -> CARACTER','expresion',1,'p_expresion_character','grammar.py',249),
  ('expresion -> ENTERO','expresion',1,'p_expresion_integer','grammar.py',253),
  ('expresion -> DOBLE','expresion',1,'p_expresion_double','grammar.py',257),
  ('expresion -> NOTHING','expresion',1,'p_expresion_nothing','grammar.py',261),
  ('expresion -> ID','expresion',1,'p_expresion_identificador','grammar.py',265),
  ('expresion -> bandera','expresion',1,'p_expresion_boolean','grammar.py',269),
  ('expresion -> expresion MAS expresion','expresion',3,'p_expresion_binaria_aritmetica','grammar.py',273),
  ('expresion -> expresion MENOS expresion','expresion',3,'p_expresion_binaria_aritmetica','grammar.py',274),
  ('expresion -> expresion ASTERISCO expresion','expresion',3,'p_expresion_binaria_aritmetica','grammar.py',275),
  ('expresion -> expresion DIVISION expresion','expresion',3,'p_expresion_binaria_aritmetica','grammar.py',276),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_binaria_aritmetica','grammar.py',277),
  ('expresion -> expresion PORCENTAJE expresion','expresion',3,'p_expresion_binaria_aritmetica','grammar.py',278),
  ('expresion -> expresion IGUALIGUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',294),
  ('expresion -> expresion DIFERENTE expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',295),
  ('expresion -> expresion MENOR expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',296),
  ('expresion -> expresion MAYOR expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',297),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',298),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_binaria_relacional','grammar.py',299),
  ('expresion -> expresion AND expresion','expresion',3,'p_expresion_binaria_logica','grammar.py',315),
  ('expresion -> expresion OR expresion','expresion',3,'p_expresion_binaria_logica','grammar.py',316),
  ('expresion -> NOT expresion','expresion',2,'p_expresion_unaria','grammar.py',324),
  ('expresion -> MENOS expresion','expresion',2,'p_expresion_unaria','grammar.py',325),
  ('bandera -> TRUE','bandera',1,'p_bandera','grammar.py',335),
  ('bandera -> FALSE','bandera',1,'p_bandera','grammar.py',336),
  ('tipo -> INT64','tipo',1,'p_tipo_datos','grammar.py',341),
  ('tipo -> FLOAT64','tipo',1,'p_tipo_datos','grammar.py',342),
  ('tipo -> STRING','tipo',1,'p_tipo_datos','grammar.py',343),
  ('tipo -> CHAR','tipo',1,'p_tipo_datos','grammar.py',344),
  ('tipo -> BOOL','tipo',1,'p_tipo_datos','grammar.py',345),
  ('asignacion_instr -> ID IGUAL expresion DOSPUNTOS DOSPUNTOS tipo','asignacion_instr',6,'p_asignacion_var_tipo','grammar.py',359),
  ('asignacion_instr -> ID IGUAL expresion','asignacion_instr',3,'p_asignacion_var','grammar.py',364),
  ('declaracion_var_instr -> LOCAL ID','declaracion_var_instr',2,'p_declaracion_local','grammar.py',368),
  ('declaracion_var_instr -> GLOBAL ID','declaracion_var_instr',2,'p_declaracion_global','grammar.py',372),
  ('imprimir_instr -> PRINT PARENTESISA expresion PARENTESISC','imprimir_instr',4,'p_imprimir','grammar.py',377),
  ('imprimir_instr -> PRINTLN PARENTESISA expresion PARENTESISC','imprimir_instr',4,'p_imprimirln','grammar.py',381),
  ('funciones_instr -> FUNCTION ID PARENTESISA PARENTESISC instrucciones END','funciones_instr',6,'p_funciones','grammar.py',386),
  ('funciones_instr -> FUNCTION ID PARENTESISA parametros PARENTESISC instrucciones END','funciones_instr',7,'p_funciones_parametros','grammar.py',390),
  ('parametros -> parametros COMA parametro','parametros',3,'p_parametros_funcion','grammar.py',395),
  ('parametros -> parametro','parametros',1,'p_parametros_parametro','grammar.py',400),
  ('parametro -> ID DOSPUNTOS DOSPUNTOS tipo','parametro',4,'p_parametro_tipo','grammar.py',405),
  ('parametro -> ID','parametro',1,'p_parametro','grammar.py',409),
  ('llamada_funcion_instr -> ID PARENTESISA PARENTESISC','llamada_funcion_instr',3,'p_llamada_funcion','grammar.py',414),
  ('while_instr -> WHILE expresion instrucciones END','while_instr',4,'p_While','grammar.py',419),
]
