
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "leftADD_OPleftMULT_OPrightUMINUSNUMBER ADD_OP MULT_OP ID STRING WHILE IF PRINT CLI RECT SCENE FUNC IMGprogram : statement\n        | statement ';'\n        | statement ';' programstatement : ID '=' expression\n        | structure\n        | PRINT expressionstructure : WHILE '(' expression ')' '{' program '}'\n        | IF '(' expression ')' '{' program '}'\n        | ':' ID scene : SCENE '(' STRING ',' '[' id_list ']' ')' cli : CLI '(' STRING ',' rect ')'  rect : RECT '(' NUMBER ',' NUMBER ',' NUMBER ',' NUMBER ')' id_list : ID\n    | ID ',' id_list expression : expression ADD_OP expression\n        | expression MULT_OP expressionexpression : NUMBERexpression : IDexpression : sceneexpression : CLIexpression : '(' expression ')' expression : ADD_OP expression %prec UMINUS"
    
_lr_action_items = {'ID':([0,5,8,9,10,12,17,19,20,24,25,38,39,40,48,],[3,14,21,3,14,14,14,14,14,14,14,3,3,44,44,]),'PRINT':([0,9,38,39,],[5,5,5,5,]),'WHILE':([0,9,38,39,],[6,6,6,6,]),'IF':([0,9,38,39,],[7,7,7,7,]),':':([0,9,38,39,],[8,8,8,8,]),'$end':([1,2,4,9,11,13,14,15,16,21,22,23,26,31,32,33,45,46,49,],[0,-1,-5,-2,-6,-17,-18,-19,-20,-9,-3,-4,-22,-15,-16,-21,-7,-8,-10,]),'}':([2,4,9,11,13,14,15,16,21,22,23,26,31,32,33,41,42,45,46,49,],[-1,-5,-2,-6,-17,-18,-19,-20,-9,-3,-4,-22,-15,-16,-21,45,46,-7,-8,-10,]),';':([2,4,11,13,14,15,16,21,23,26,31,32,33,45,46,49,],[9,-5,-6,-17,-18,-19,-20,-9,-4,-22,-15,-16,-21,-7,-8,-10,]),'=':([3,],[10,]),'NUMBER':([5,10,12,17,19,20,24,25,],[13,13,13,13,13,13,13,13,]),'CLI':([5,10,12,17,19,20,24,25,],[16,16,16,16,16,16,16,16,]),'(':([5,6,7,10,12,17,18,19,20,24,25,],[17,19,20,17,17,17,28,17,17,17,17,]),'ADD_OP':([5,10,11,12,13,14,15,16,17,19,20,23,24,25,26,27,29,30,31,32,33,49,],[12,12,24,12,-17,-18,-19,-20,12,12,12,24,12,12,-22,24,24,24,-15,-16,-21,-10,]),'SCENE':([5,10,12,17,19,20,24,25,],[18,18,18,18,18,18,18,18,]),'MULT_OP':([11,13,14,15,16,23,26,27,29,30,31,32,33,49,],[25,-17,-18,-19,-20,25,-22,25,25,25,25,-16,-21,-10,]),')':([13,14,15,16,26,27,29,30,31,32,33,47,49,],[-17,-18,-19,-20,-22,33,35,36,-15,-16,-21,49,-10,]),'STRING':([28,],[34,]),',':([34,44,],[37,48,]),'{':([35,36,],[38,39,]),'[':([37,],[40,]),']':([43,44,50,],[47,-13,-14,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,9,38,39,],[1,22,41,42,]),'statement':([0,9,38,39,],[2,2,2,2,]),'structure':([0,9,38,39,],[4,4,4,4,]),'expression':([5,10,12,17,19,20,24,25,],[11,23,26,27,29,30,31,32,]),'scene':([5,10,12,17,19,20,24,25,],[15,15,15,15,15,15,15,15,]),'id_list':([40,48,],[43,50,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','parser.py',22),
  ('program -> statement ;','program',2,'p_program','parser.py',23),
  ('program -> statement ; program','program',3,'p_program','parser.py',24),
  ('statement -> ID = expression','statement',3,'p_statement','parser.py',31),
  ('statement -> structure','statement',1,'p_statement','parser.py',32),
  ('statement -> PRINT expression','statement',2,'p_statement','parser.py',33),
  ('structure -> WHILE ( expression ) { program }','structure',7,'p_structure','parser.py',44),
  ('structure -> IF ( expression ) { program }','structure',7,'p_structure','parser.py',45),
  ('structure -> : ID','structure',2,'p_structure','parser.py',46),
  ('scene -> SCENE ( STRING , [ id_list ] )','scene',8,'p_scene_type','parser.py',56),
  ('cli -> CLI ( STRING , rect )','cli',6,'p_cli_type','parser.py',60),
  ('rect -> RECT ( NUMBER , NUMBER , NUMBER , NUMBER )','rect',10,'p_rect_type','parser.py',64),
  ('id_list -> ID','id_list',1,'p_id_list','parser.py',68),
  ('id_list -> ID , id_list','id_list',3,'p_id_list','parser.py',69),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser.py',74),
  ('expression -> expression MULT_OP expression','expression',3,'p_expression_op','parser.py',75),
  ('expression -> NUMBER','expression',1,'p_number','parser.py',80),
  ('expression -> ID','expression',1,'p_variable','parser.py',84),
  ('expression -> scene','expression',1,'p_scene','parser.py',89),
  ('expression -> CLI','expression',1,'p_cli','parser.py',93),
  ('expression -> ( expression )','expression',3,'p_parenthesis','parser.py',97),
  ('expression -> ADD_OP expression','expression',2,'p_uminus','parser.py',101),
]
