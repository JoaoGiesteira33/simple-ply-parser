
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ProgramCODE COLON COMMA DEF EQUALS ERROR LBRACKET LCBRACKET LEX LPARENTHESIS LexIGNORE LexLITERALS LexTOKENS POINT PREC RBRACKET RCBRACKET RETURN RPARENTHESIS YACC YaccPRECEDENCE apostropheStr comment fLEX fYACC functionParameters functionText id quotationStr regex regexreturn textProgram : LEX LexDefinition YACC YaccDefinition CODELexDefinition : LexVALUES LexBEHAVIOR LexDECLARATIONLexVALUES : LexVALUES LexVALUELexVALUES : LexVALUELexVALUE : LexLITERALS EQUALS quotationStrLexVALUE : LexIGNORE EQUALS quotationStrLexVALUE : LexTOKENS EQUALS LBRACKET TokenList RBRACKETTokenList : TokenList COMMA apostropheStrTokenList : apostropheStrLexBEHAVIOR : TokenDefinitions ErrorDefinitionTokenDefinitions : TokenDefinitions TokenDefinitionTokenDefinitions : TokenDefinition : regex RETURN LPARENTHESIS apostropheStr COMMA RETURNVALUE RPARENTHESISRETURNVALUE : RETURNVALUE textRETURNVALUE : RETURNVALUE LPARENTHESISRETURNVALUE : RETURNVALUE RPARENTHESISRETURNVALUE : ErrorDefinition : POINT ERROR LPARENTHESIS quotationStr COMMA ERRORVALUE RPARENTHESISERRORVALUE : ERRORVALUE textERRORVALUE : ERRORVALUE LPARENTHESISERRORVALUE : ERRORVALUE RPARENTHESISERRORVALUE : LexDECLARATION : id EQUALS fLEXYaccDefinition : YaccDefinition YaccPRECEDENCE EQUALS LBRACKET precedenceList RBRACKETYaccDefinition : YaccDefinition YaccVariableYaccDefinition : YaccDefinition ProductionYaccDefinition : precedenceList : precedenceList LPARENTHESIS precedenceElement RPARENTHESIS COMMAprecedenceList : LPARENTHESIS precedenceElement RPARENTHESIS COMMAYaccVariable : id EQUALS textprecedenceElement : precedenceElement COMMA apostropheStrprecedenceElement : apostropheStr COMMA apostropheStrProduction : id COLON SimbolList LCBRACKET text RCBRACKETSimbolList : SimbolList idSimbolList : SimbolList apostropheStrSimbolList : SimbolList PRECSimbolList : '
    
_lr_action_items = {'LEX':([0,],[2,]),'$end':([1,26,],[0,-1,]),'LexLITERALS':([2,4,5,11,23,24,42,],[6,6,-4,-3,-5,-6,-7,]),'LexIGNORE':([2,4,5,11,23,24,42,],[7,7,-4,-3,-5,-6,-7,]),'LexTOKENS':([2,4,5,11,23,24,42,],[8,8,-4,-3,-5,-6,-7,]),'YACC':([3,17,39,],[9,-2,-23,]),'POINT':([4,5,11,12,20,23,24,42,74,],[-12,-4,-3,21,-11,-5,-6,-7,-13,]),'regex':([4,5,11,12,20,23,24,42,74,],[-12,-4,-3,22,-11,-5,-6,-7,-13,]),'EQUALS':([6,7,8,18,27,30,],[13,14,15,31,36,37,]),'CODE':([9,16,28,29,45,58,69,],[-27,26,-25,-26,-30,-24,-33,]),'YaccPRECEDENCE':([9,16,28,29,45,58,69,],[-27,27,-25,-26,-30,-24,-33,]),'id':([9,10,16,19,28,29,38,45,46,52,54,55,58,69,71,],[-27,18,30,-10,-25,-26,-37,-30,52,-34,-35,-36,-24,-33,-18,]),'quotationStr':([13,14,40,],[23,24,47,]),'LBRACKET':([15,36,],[25,44,]),'ERROR':([21,],[32,]),'RETURN':([22,],[33,]),'apostropheStr':([25,38,41,43,46,51,52,54,55,59,67,68,],[35,-37,48,49,54,61,-34,-35,-36,61,78,79,]),'COLON':([30,],[38,]),'fLEX':([31,],[39,]),'LPARENTHESIS':([32,33,44,50,56,57,63,64,70,71,72,73,74,75,77,80,],[40,41,51,59,-22,-17,70,73,-20,-21,-19,-15,-16,-14,-29,-28,]),'RBRACKET':([34,35,49,50,77,80,],[42,-9,-8,58,-29,-28,]),'COMMA':([34,35,47,48,49,60,61,65,66,76,78,79,],[43,-9,56,57,-8,67,68,67,77,80,-31,-32,]),'text':([37,53,56,57,63,64,70,71,72,73,74,75,],[45,62,-22,-17,72,75,-20,-21,-19,-15,-16,-14,]),'LCBRACKET':([38,46,52,54,55,],[-37,53,-34,-35,-36,]),'PREC':([38,46,52,54,55,],[-37,55,-34,-35,-36,]),'RPARENTHESIS':([56,57,60,63,64,65,70,71,72,73,74,75,78,79,],[-22,-17,66,71,74,76,-20,-21,-19,-15,-16,-14,-31,-32,]),'RCBRACKET':([62,],[69,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Program':([0,],[1,]),'LexDefinition':([2,],[3,]),'LexVALUES':([2,],[4,]),'LexVALUE':([2,4,],[5,11,]),'LexBEHAVIOR':([4,],[10,]),'TokenDefinitions':([4,],[12,]),'YaccDefinition':([9,],[16,]),'LexDECLARATION':([10,],[17,]),'ErrorDefinition':([12,],[19,]),'TokenDefinition':([12,],[20,]),'YaccVariable':([16,],[28,]),'Production':([16,],[29,]),'TokenList':([25,],[34,]),'SimbolList':([38,],[46,]),'precedenceList':([44,],[50,]),'precedenceElement':([51,59,],[60,65,]),'ERRORVALUE':([56,],[63,]),'RETURNVALUE':([57,],[64,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Program","S'",1,None,None,None),
  ('Program -> LEX LexDefinition YACC YaccDefinition CODE','Program',5,'p_Program','simplePlyParser_2sin.py',9),
  ('LexDefinition -> LexVALUES LexBEHAVIOR LexDECLARATION','LexDefinition',3,'p_LexDefinition','simplePlyParser_2sin.py',13),
  ('LexVALUES -> LexVALUES LexVALUE','LexVALUES',2,'p_LexVALUES_list','simplePlyParser_2sin.py',17),
  ('LexVALUES -> LexVALUE','LexVALUES',1,'p_LexVALUES_sing','simplePlyParser_2sin.py',19),
  ('LexVALUE -> LexLITERALS EQUALS quotationStr','LexVALUE',3,'p_LexVALUE_literals','simplePlyParser_2sin.py',23),
  ('LexVALUE -> LexIGNORE EQUALS quotationStr','LexVALUE',3,'p_LexVALUE_ignore','simplePlyParser_2sin.py',25),
  ('LexVALUE -> LexTOKENS EQUALS LBRACKET TokenList RBRACKET','LexVALUE',5,'p_LexVALUE_tokens','simplePlyParser_2sin.py',27),
  ('TokenList -> TokenList COMMA apostropheStr','TokenList',3,'p_TokenList_list','simplePlyParser_2sin.py',31),
  ('TokenList -> apostropheStr','TokenList',1,'p_TokenList_sing','simplePlyParser_2sin.py',33),
  ('LexBEHAVIOR -> TokenDefinitions ErrorDefinition','LexBEHAVIOR',2,'p_LexBEHAVIOR','simplePlyParser_2sin.py',37),
  ('TokenDefinitions -> TokenDefinitions TokenDefinition','TokenDefinitions',2,'p_TokenDefinitions_list','simplePlyParser_2sin.py',41),
  ('TokenDefinitions -> <empty>','TokenDefinitions',0,'p_TokenDefinitions_empty','simplePlyParser_2sin.py',43),
  ('TokenDefinition -> regex RETURN LPARENTHESIS apostropheStr COMMA RETURNVALUE RPARENTHESIS','TokenDefinition',7,'p_TokenDefinition','simplePlyParser_2sin.py',46),
  ('RETURNVALUE -> RETURNVALUE text','RETURNVALUE',2,'p_RETURNVALUE_text','simplePlyParser_2sin.py',49),
  ('RETURNVALUE -> RETURNVALUE LPARENTHESIS','RETURNVALUE',2,'p_RETURNVALUE_lparenthesis','simplePlyParser_2sin.py',51),
  ('RETURNVALUE -> RETURNVALUE RPARENTHESIS','RETURNVALUE',2,'p_RETURNVALUE_rparenthesis','simplePlyParser_2sin.py',53),
  ('RETURNVALUE -> <empty>','RETURNVALUE',0,'p_RETURNVALUE_empty','simplePlyParser_2sin.py',55),
  ('ErrorDefinition -> POINT ERROR LPARENTHESIS quotationStr COMMA ERRORVALUE RPARENTHESIS','ErrorDefinition',7,'p_ErrorDefinition','simplePlyParser_2sin.py',60),
  ('ERRORVALUE -> ERRORVALUE text','ERRORVALUE',2,'p_ERROR_text','simplePlyParser_2sin.py',63),
  ('ERRORVALUE -> ERRORVALUE LPARENTHESIS','ERRORVALUE',2,'p_ERRORVALUE_lparenthesis','simplePlyParser_2sin.py',65),
  ('ERRORVALUE -> ERRORVALUE RPARENTHESIS','ERRORVALUE',2,'p_ERRORVALUE_rparenthesis','simplePlyParser_2sin.py',67),
  ('ERRORVALUE -> <empty>','ERRORVALUE',0,'p_ERRORVALUE_empty','simplePlyParser_2sin.py',69),
  ('LexDECLARATION -> id EQUALS fLEX','LexDECLARATION',3,'p_LexDECLARATION','simplePlyParser_2sin.py',73),
  ('YaccDefinition -> YaccDefinition YaccPRECEDENCE EQUALS LBRACKET precedenceList RBRACKET','YaccDefinition',6,'p_YaccDefinition_precedence','simplePlyParser_2sin.py',77),
  ('YaccDefinition -> YaccDefinition YaccVariable','YaccDefinition',2,'p_YaccDefinition_id','simplePlyParser_2sin.py',79),
  ('YaccDefinition -> YaccDefinition Production','YaccDefinition',2,'p_YaccDefinition_production','simplePlyParser_2sin.py',81),
  ('YaccDefinition -> <empty>','YaccDefinition',0,'p_YaccDefinition_empty','simplePlyParser_2sin.py',83),
  ('precedenceList -> precedenceList LPARENTHESIS precedenceElement RPARENTHESIS COMMA','precedenceList',5,'p_precedenceList_list','simplePlyParser_2sin.py',88),
  ('precedenceList -> LPARENTHESIS precedenceElement RPARENTHESIS COMMA','precedenceList',4,'p_precedenceList_sing','simplePlyParser_2sin.py',90),
  ('YaccVariable -> id EQUALS text','YaccVariable',3,'p_YaccVariable','simplePlyParser_2sin.py',94),
  ('precedenceElement -> precedenceElement COMMA apostropheStr','precedenceElement',3,'p_precedenceElement_list','simplePlyParser_2sin.py',98),
  ('precedenceElement -> apostropheStr COMMA apostropheStr','precedenceElement',3,'p_precedenceElement_duo','simplePlyParser_2sin.py',100),
  ('Production -> id COLON SimbolList LCBRACKET text RCBRACKET','Production',6,'p_Production','simplePlyParser_2sin.py',104),
  ('SimbolList -> SimbolList id','SimbolList',2,'p_SimbolList_list_id','simplePlyParser_2sin.py',108),
  ('SimbolList -> SimbolList apostropheStr','SimbolList',2,'p_SimbolList_list_literal','simplePlyParser_2sin.py',110),
  ('SimbolList -> SimbolList PREC','SimbolList',2,'p_SimbolList_list_prec','simplePlyParser_2sin.py',112),
  ('SimbolList -> <empty>','SimbolList',0,'p_SimbolList_empty','simplePlyParser_2sin.py',114),
]
