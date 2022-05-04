import sys
import ply.yacc as yacc
from simplePlyParser_2lex import tokens

start = 'Program'

#Production rules
def p_Program(p):
    "Program : LEX LexDefinition YACC YaccDefinition CODE CodeDefinition"

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
    "LexVALUE : LexLITERALS EQUALS quotationStr"
def p_LexVALUE_ignore(p):
    "LexVALUE : LexIGNORE EQUALS quotationStr"
def p_LexVALUE_tokens(p):
    "LexVALUE : LexTOKENS EQUALS LBRACKET TokenList RBRACKET"

# TokenList #
def p_TokenList_list(p):
    "TokenList : TokenList COMMA apostropheStr"
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
    "TokenDefinition : regex RETURN LPARENTHESIS apostropheStr COMMA RETURNVALUE RPARENTHESIS"
# RETURNVALUE #
def p_RETURNVALUE_text(p):
    "RETURNVALUE : RETURNVALUE text"
def p_RETURNVALUE_lparenthesis(p):
    "RETURNVALUE : RETURNVALUE LPARENTHESIS"
def p_RETURNVALUE_rparenthesis(p):
    "RETURNVALUE : RETURNVALUE RPARENTHESIS"
def p_RETURNVALUE_empty(p):
    "RETURNVALUE : "
    pass

## Error Definition #
def p_ErrorDefinition(p):
    "ErrorDefinition : POINT ERROR LPARENTHESIS quotationStr COMMA ERRORVALUE RPARENTHESIS"
# ERRORVALUE #
def p_ERROR_text(p):
    "ERRORVALUE : ERRORVALUE text"
def p_ERRORVALUE_lparenthesis(p):
    "ERRORVALUE : ERRORVALUE LPARENTHESIS"
def p_ERRORVALUE_rparenthesis(p):
    "ERRORVALUE : ERRORVALUE RPARENTHESIS"
def p_ERRORVALUE_empty(p):
    "ERRORVALUE : "
    pass
# LexDECLARATION #
def p_LexDECLARATION(p):
    "LexDECLARATION : id EQUALS fLEX"

#### YaccDefinition ####
def p_YaccDefinition_precedence(p):
    "YaccDefinition : YaccDefinition YaccPRECEDENCE EQUALS LBRACKET precedenceList RBRACKET"
def p_YaccDefinition_id(p):
    "YaccDefinition : YaccDefinition YaccVariable"
def p_YaccDefinition_production(p):
    "YaccDefinition : YaccDefinition Production"
def p_YaccDefinition_empty(p):
    "YaccDefinition : "
    pass

### precedenceList ###
def p_precedenceList_list(p):
    "precedenceList : precedenceList LPARENTHESIS precedenceElement RPARENTHESIS COMMA"
def p_precedenceList_sing(p):
    "precedenceList : LPARENTHESIS precedenceElement RPARENTHESIS COMMA"

## YaccVariable ##
def p_YaccVariable(p):
    "YaccVariable : id EQUALS text"

## precedenceElement ##
def p_precedenceElement_list(p):
    "precedenceElement : precedenceElement COMMA apostropheStr"
def p_precedenceElement_duo(p):
    "precedenceElement : apostropheStr COMMA apostropheStr"

## Production ##
def p_Production(p):
    "Production : id COLON SimbolList LCBRACKET text RCBRACKET"

# SimbolList #
def p_SimbolList_list_id(p):
    "SimbolList : SimbolList id"
def p_SimbolList_list_literal(p):
    "SimbolList : SimbolList apostropheStr"
def p_SimbolList_list_prec(p):
    "SimbolList : SimbolList PREC"
def p_SimbolList_empty(p):
    "SimbolList : "

#### CodeDefinition ####
def p_CodeDefinition_funtion(p):
    "CodeDefinition : Functions "#YaccDeclaration"# Parses"
    print(p[1])
### Functions ###
def p_Functions_list(p):
    "Functions : Functions Function"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_Functions_empty(p):
    "Functions : "
    pass

## Function ##
def p_Function(p):
    "Function : DEF id LPARENTHESIS id RPARENTHESIS COLON FunctionText"
    p[0] = p[1] + " " + p[2] + p[3] + p[4] + p[5] + p[6] + p[7]

# Function Text#
def p_FunctionText_list(p):
    "FunctionText : FunctionText text"
    p[0] = p[1] + p[2]
def p_FunctionText_sing(p):
    "FunctionText : text"
    p[0] = p[1]

### YaccDeclaration ###
def p_YaccDeclaration(p):
    "YaccDeclaration : id EQUALS fYACC"

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