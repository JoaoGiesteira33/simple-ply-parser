import sys
import ply.yacc as yacc
from simplePlyParser_lex import tokens,literals

#Production rules
def p_Program(p):
    "Program : LEX LexDefinition"# YACC YaccDefinition CODE CodeDefinition"

#### Lex Structure ####
def p_LexDefinition(p):
    "LexDefinition : LexVALUES LexBEHAVIOR "#LexDECLARATION"

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
    "LexBEHAVIOR : TokenDefinitions "#"ErrorDefinition"

# TokenDefinitions #
# Pode ser Vazio #
def p_TokenDefinitions_list(p):
    "TokenDefinitions : TokenDefinitions TokenDefinition"
def p_TokenDefinitions_empty(p):
    "TokenDefinitions : "
def p_TokenDefinition(p):
    "TokenDefinition : regex RETURN '(' apostropheStr ',' apostropheStr ')'"

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