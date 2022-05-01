import sys
import ply.yacc as yacc
from simplePlyParser_lex import tokens,literals

start = 'Program'

#Production rules
def p_Program(p):
    "Program : LEX LexDefinition YACC YaccDefinition CODE "#CodeDefinition"

#### Lex Structure ####
def p_LexDefinition(p):
    "LexDefinition : LexVALUES LexBEHAVIOR LexDECLARATION"

### LexVALUES ###
def p_LexVALUES_list(p):
    "LexVALUES : LexVALUES LexVALUE"
def p_LexVALUES_sing(p):
    "LexVALUES : LexVALUE"

## LexVALUE ##
def p_LexVALUE_literals(p):
    "LexVALUE : LexLITERALS '=' quotationStr"
def p_LexVALUE_ignore(p):
    "LexVALUE : LexIGNORE '=' quotationStr"
def p_LexVALUE_tokens(p):
    "LexVALUE : LexTOKENS '=' '[' TokenList ']'"

# TokenList #
def p_TokenList_list(p):
    "TokenList : TokenList ',' apostropheStr"
def p_TokenList_sing(p):
    "TokenList : apostropheStr"

## LexBEHAVIOR ##
def p_LexBEHAVIOR(p):
    "LexBEHAVIOR : TokenDefinitions ErrorDefinition"

# TokenDefinitions #
def p_TokenDefinitions_list(p):
    "TokenDefinitions : TokenDefinitions TokenDefinition"
def p_TokenDefinitions_empty(p):
    "TokenDefinitions : "
    pass
def p_TokenDefinition(p):
    "TokenDefinition : regex RETURN"

# Error Definition #
def p_ErrorDefinition(p):
    "ErrorDefinition : '.' ERROR"

# LexDECLARATION #
def p_LexDECLARATION(p):
    "LexDECLARATION : id '=' fLEX"

#### YaccDefinition ####
def p_YaccDefinition_precedence(p):
    "YaccDefinition : YaccDefinition YaccPRECEDENCE '=' '[' precedenceList ']'"
def p_YaccDefinition_id(p):
    "YaccDefinition : YaccDefinition YaccVariable"
def p_YaccDefinition_production(p):
    "YaccDefinition : YaccDefinition Production"
def p_YaccDefinition_empty(p):
    "YaccDefinition : "
    pass

### precedenceList ###
def p_precedenceList_list(p):
    "precedenceList : precedenceList '(' precedenceElement ')' ','"
def p_precedenceList_sing(p):
    "precedenceList : '(' precedenceElement ')' ','"

## precedenceElement ##
def p_precedenceElement_list(p):
    "precedenceElement : precedenceElement ',' apostropheStr"
def p_precedenceElement_duo(p):
    "precedenceElement : apostropheStr ',' apostropheStr"

## Production ##
def p_Production(p):
    "Production : id ':' SimbolList  productioncode"

# SimbolList
def p_SimbolList_list_id(p):
    "SimbolList : SimbolList id"
def p_SimbolList_list_literal(p):
    "SimbolList : SimbolList apostropheStr"
def p_SimbolList_list_prec(p):
    "SimbolList : SimbolList PREC"
def p_SimbolList_sing_id(p):
    "SimbolList : id"
def p_SimbolList_sing_literal(p):
    "SimbolList : apostropheStr"
def p_SimbolList_sing_prec(p):
    "SimbolList : PREC"

def p_error(p):
    print('Erro sintático: ',p)
    parser.sucess = False

parser = yacc.yacc()
parser.sucess = True
program = sys.stdin.read()

parser.parse(program)
if parser.sucess:
    print("Programa bem estruturado")
else:
    print("Programa Inválido")