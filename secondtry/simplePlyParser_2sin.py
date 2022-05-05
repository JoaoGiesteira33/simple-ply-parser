import sys
import ply.yacc as yacc
from simplePlyParser_2lex import tokens

start = 'Program'

#Production rules
def p_Program(p):
    "Program : LEX LexDefinition YACC YaccDefinition CODE CodeDefinition"
    print("import ply.lex as lex\n" +  p[2] + "\n" + "import ply.yacc as yacc\n" + p[4] + "\n" + p[6])
#### Lex Structure ####
def p_LexDefinition(p):
    "LexDefinition : LexVALUES LexBEHAVIOR LexDECLARATION"
    p[0] = p[1] + "\n" + p[2] + "\n" + p[3]

### LexVALUES ###
def p_LexVALUES_list(p):
    "LexVALUES : LexVALUES LexVALUE"
    if(p[1]):
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[2]
def p_LexVALUES_sing(p):
    "LexVALUES : LexVALUE"
    p[0] = p[1]

## LexVALUE ##
def p_LexVALUE_literals(p):
    "LexVALUE : LexLITERALS EQUALS quotationStr"
    p[0] = (p[1])[1:] + p[2] + p[3]
def p_LexVALUE_ignore(p):
    "LexVALUE : LexIGNORE EQUALS quotationStr"
    p[0] = (p[1])[1:] + p[2] + p[3]
def p_LexVALUE_tokens(p):
    "LexVALUE : LexTOKENS EQUALS LBRACKET TokenList RBRACKET"
    p[0] = (p[1])[1:] + p[2] + p[3] + p[4] + p[5]

# TokenList #
def p_TokenList_list(p):
    "TokenList : TokenList COMMA apostropheStr"
    if(p[1]):
        p[0] = p[1] + p[2] + p[3]
    else:
        p[0] = p[3]
def p_TokenList_sing(p):
    "TokenList : apostropheStr"
    p[0] = p[1]

## LexBEHAVIOR ##
def p_LexBEHAVIOR(p):
    "LexBEHAVIOR : TokenDefinitions ErrorDefinition"
    p[0] = p[1] + "\n" + p[2]
# TokenDefinitions #
def p_TokenDefinitions_list(p):
    "TokenDefinitions : TokenDefinitions TokenDefinition"
    if(p[1]):
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[2]
def p_TokenDefinitions_empty(p):
    "TokenDefinitions : "
    pass
def p_TokenDefinition(p):
    "TokenDefinition : regex RETURN LPARENTHESIS apostropheStr COMMA RETURNVALUE RPARENTHESIS"
    p[0] = "def t_" + (p[4])[1:-1] + "(t):\n\t" + p[1] + "\n\tt.value = " + p[6] + "\n\treturn t"
# RETURNVALUE #
def p_RETURNVALUE_text(p):
    "RETURNVALUE : RETURNVALUE text"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_RETURNVALUE_lparenthesis(p):
    "RETURNVALUE : RETURNVALUE LPARENTHESIS"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_RETURNVALUE_rparenthesis(p):
    "RETURNVALUE : RETURNVALUE RPARENTHESIS"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_RETURNVALUE_empty(p):
    "RETURNVALUE : "
    pass

## Error Definition #
def p_ErrorDefinition(p):
    "ErrorDefinition : POINT ERROR LPARENTHESIS quotationStr COMMA ERRORVALUE RPARENTHESIS"
    p[0] = "def t_error(t):\n\t" + "print(" + p[4] + ")\n\t" + p[6]
# ERRORVALUE #
def p_ERROR_text(p):
    "ERRORVALUE : ERRORVALUE text"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_ERRORVALUE_lparenthesis(p):
    "ERRORVALUE : ERRORVALUE LPARENTHESIS"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_ERRORVALUE_rparenthesis(p):
    "ERRORVALUE : ERRORVALUE RPARENTHESIS"
    if(p[1]):
        p[0] = p[1] + p[2]
    else:
        p[0] = p[2]
def p_ERRORVALUE_empty(p):
    "ERRORVALUE : "
    pass
# LexDECLARATION #
def p_LexDECLARATION(p):
    "LexDECLARATION : id EQUALS fLEX"
    p[0] = p[1] + " " + p[2] + "lex." + p[3]

#### YaccDefinition ####
def p_YaccDefinition_precedence(p):
    "YaccDefinition : YaccDefinition YaccPRECEDENCE EQUALS LBRACKET precedenceList RBRACKET"
    if(p[1]):
        p[0] = p[1] + "\n" + (p[2])[1:] + p[3] + p[4] + "\n" + p[5] + p[6]
    else:
        p[0] = (p[2])[1:] + p[3] + p[4] + "\n" + p[5] + p[6]
def p_YaccDefinition_id(p):
    "YaccDefinition : YaccDefinition YaccVariable"
    if(p[1]):
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[2]
def p_YaccDefinition_production(p):
    "YaccDefinition : YaccDefinition Production"
    if(p[1]):
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[2]
def p_YaccDefinition_empty(p):
    "YaccDefinition : "
    pass

### precedenceList ###
def p_precedenceList_list(p):
    "precedenceList : precedenceList LPARENTHESIS precedenceElement RPARENTHESIS COMMA"
    if(p[1]):
        p[0] = p[1] + "\t" + p[2] + p[3] + p[4] + p[5] + "\n"
    else:
        p[0] = "\t" + p[2] + p[3] + p[4] + p[5] + "\n"
def p_precedenceList_sing(p):
    "precedenceList : LPARENTHESIS precedenceElement RPARENTHESIS COMMA"
    p[0] = "\t" + p[1] + p[2] + p[3] + p[4] + "\n"

## YaccVariable ##
def p_YaccVariable(p):
    "YaccVariable : id EQUALS text"
    p[0] = p[1] + " " + p[2] + p[3]


## precedenceElement ##
def p_precedenceElement_list(p):
    "precedenceElement : precedenceElement COMMA apostropheStr"
    p[0] = p[1] + p[2] + p[3]
def p_precedenceElement_duo(p):
    "precedenceElement : apostropheStr COMMA apostropheStr"
    p[0] = p[1] + p[2] + p[3]

## Production ##
def p_Production(p):
    "Production : id COLON SimbolList LCBRACKET text RCBRACKET"
    p[0] = "def p_" + p[1] + "_" + str(parser.nproductions) +  "(t):\n\t\"" + p[1] + " : " + p[3] + "\"\n\t" + p[5] 
    parser.nproductions += 1
# SimbolList #
def p_SimbolList_list_id(p):
    "SimbolList : SimbolList id"
    if(p[1]):
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[2]
def p_SimbolList_list_literal(p):
    "SimbolList : SimbolList apostropheStr"
    if(p[1]):
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[2]
def p_SimbolList_list_prec(p):
    "SimbolList : SimbolList PREC"
    if(p[1]):
        p[0] = p[1] + " " + p[2]
    else:
        p[0] = p[2]
def p_SimbolList_empty(p):
    "SimbolList : "
    pass

#### CodeDefinition ####
def p_CodeDefinition_funtion(p):
    "CodeDefinition : Functions YaccDeclaration Parses"
    p[0] = p[1] + "\n" + p[2] + "\n" + p[3]
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
    "Function : DEF id LPARENTHESIS id RPARENTHESIS COLON FunctionText FUNCTIONEND"
    p[0] = p[1] + " " + p[2] + p[3] + p[4] + p[5] + p[6] + "\n" + p[7] + p[8]

# Function Text#
def p_FunctionText_list(p):
    "FunctionText : FunctionText text"
    p[0] = p[1] + " " + p[2] + "\n"
def p_FunctionText_sing(p):
    "FunctionText : text"
    p[0] = " " + p[1] + "\n"

### YaccDeclaration ###
def p_YaccDeclaration(p):
    "YaccDeclaration : id EQUALS fYACC"
    p[0] = p[1] + p[2] + "yacc." + p[3]

### Parses ###
def p_Parses_list(p):
    "Parses : Parses Parse"
    if(p[1]):
        p[0] = p[1] + "\n" + p[2]
    else:
        p[0] = p[2]
def p_Parses_empty(p):
    "Parses : "
    pass
## Parse ##
def p_Parse(p):
    "Parse : id POINT PARSE LPARENTHESIS quotationStr RPARENTHESIS"
    p[0] = p[1] + p[2] + p[3] + p[4] + p[5] + p[6]

def p_error(p):
    print('Erro sintático: ',p)
    parser.sucess = False

parser = yacc.yacc()
parser.nproductions = 0
parser.sucess = True
program = sys.stdin.read()

parser.parse(program)
if parser.sucess:
    pass
else:
    print("Programa Inválido")