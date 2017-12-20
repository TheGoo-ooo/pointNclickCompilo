
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = '543502D30955EA511BA7F7286F3E0320'
    
_lr_action_items = {'ID':([0,5,8,9,10,12,16,18,19,23,24,37,38,44,47,50,53,55,],[3,14,20,3,14,14,14,14,14,14,14,3,3,14,3,14,14,14,]),'PRINT':([0,9,37,38,47,],[5,5,5,5,5,]),'WHILE':([0,9,37,38,47,],[6,6,6,6,6,]),'IF':([0,9,37,38,47,],[7,7,7,7,7,]),':':([0,9,37,38,47,],[8,8,8,8,8,]),'$end':([1,2,4,9,11,13,14,15,20,21,22,25,30,31,32,45,46,51,],[0,-1,-5,-2,-6,-14,-15,-16,-9,-3,-4,-18,-12,-13,-17,-7,-8,-10,]),'}':([2,4,9,11,13,14,15,20,21,22,25,30,31,32,41,42,45,46,49,51,],[-1,-5,-2,-6,-14,-15,-16,-9,-3,-4,-18,-12,-13,-17,45,46,-7,-8,51,-10,]),';':([2,4,11,13,14,15,20,22,25,30,31,32,45,46,51,],[9,-5,-6,-14,-15,-16,-9,-4,-18,-12,-13,-17,-7,-8,-10,]),'=':([3,],[10,]),'NUMBER':([5,10,12,16,18,19,23,24,44,50,53,55,],[13,13,13,13,13,13,13,13,13,13,13,13,]),'(':([5,6,7,10,12,16,17,18,19,23,24,40,44,50,53,55,],[16,18,19,16,16,16,27,16,16,16,16,44,16,16,16,16,]),'ADD_OP':([5,10,11,12,13,14,15,16,18,19,22,23,24,25,26,28,29,30,31,32,44,48,50,51,52,53,54,55,56,],[12,12,23,12,-14,-15,-16,12,12,12,23,12,12,-18,23,23,23,-12,-13,-17,12,23,12,-10,23,12,23,12,23,]),'CLI':([5,10,12,16,18,19,23,24,44,50,53,55,],[17,17,17,17,17,17,17,17,17,17,17,17,]),'MULT_OP':([11,13,14,15,22,25,26,28,29,30,31,32,48,51,52,54,56,],[24,-14,-15,-16,24,-18,24,24,24,24,-13,-17,24,-10,24,24,24,]),')':([13,14,15,25,26,28,29,30,31,32,39,51,56,57,],[-14,-15,-16,-18,32,34,35,-12,-13,-17,43,-10,57,-11,]),',':([13,14,15,25,30,31,32,33,48,51,52,54,],[-14,-15,-16,-18,-12,-13,-17,36,50,-10,53,55,]),'STRING':([27,],[33,]),'{':([34,35,43,],[37,38,47,]),'RECT':([36,],[40,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,9,37,38,47,],[1,21,41,42,49,]),'statement':([0,9,37,38,47,],[2,2,2,2,2,]),'structure':([0,9,37,38,47,],[4,4,4,4,4,]),'expression':([5,10,12,16,18,19,23,24,44,50,53,55,],[11,22,25,26,28,29,30,31,48,52,54,56,]),'cli':([5,10,12,16,18,19,23,24,44,50,53,55,],[15,15,15,15,15,15,15,15,15,15,15,15,]),'rect':([36,],[39,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> statement','program',1,'p_program','parser.py',20),
  ('program -> statement ;','program',2,'p_program','parser.py',21),
  ('program -> statement ; program','program',3,'p_program','parser.py',22),
  ('statement -> ID = expression','statement',3,'p_statement','parser.py',30),
  ('statement -> structure','statement',1,'p_statement','parser.py',31),
  ('statement -> PRINT expression','statement',2,'p_statement','parser.py',32),
  ('structure -> WHILE ( expression ) { program }','structure',7,'p_structure','parser.py',42),
  ('structure -> IF ( expression ) { program }','structure',7,'p_structure','parser.py',43),
  ('structure -> : ID','structure',2,'p_structure','parser.py',44),
  ('cli -> CLI ( STRING , rect ) { program }','cli',9,'p_cli_type','parser.py',60),
  ('rect -> RECT ( expression , expression , expression , expression )','rect',10,'p_rect_type','parser.py',66),
  ('expression -> expression ADD_OP expression','expression',3,'p_expression_op','parser.py',78),
  ('expression -> expression MULT_OP expression','expression',3,'p_expression_op','parser.py',79),
  ('expression -> NUMBER','expression',1,'p_number','parser.py',83),
  ('expression -> ID','expression',1,'p_variable','parser.py',87),
  ('expression -> cli','expression',1,'p_cli','parser.py',97),
  ('expression -> ( expression )','expression',3,'p_parenthesis','parser.py',101),
  ('expression -> ADD_OP expression','expression',2,'p_uminus','parser.py',105),
]
