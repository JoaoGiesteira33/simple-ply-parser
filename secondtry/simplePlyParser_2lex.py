# Compilador
#
# prog.txt
#
import ply.lex as lex

tokens = ['LEX','YACC','CODE',
        'LexLITERALS','LexIGNORE','LexTOKENS','fLEX',
        'EQUALS','LPARENTHESIS','RPARENTHESIS','COMMA','POINT',
        'COLON','LBRACKET','RBRACKET','LCBRACKET','RCBRACKET',
        'YaccPRECEDENCE','fYACC','PREC',
        'DEF','RETURN','ERROR','functionParameters',
        'id',
        'quotationStr','apostropheStr','regex','regexreturn',
        'comment','text',
        'functionText']

states = (
    ('lexstate','exclusive'),
    ('yaccstate','exclusive'),
    ('codestate','exclusive'),
    ('regexstate','exclusive'),
    ('errorstate','exclusive'),
    ('yaccvariablestate','exclusive'),
    ('productionstate','exclusive'),
    ('productioncode','exclusive'),
    ('functionstate','exclusive'),
)
#############
#MAIN STATES#
def t_INITIAL_LEX(t):
    r'%%\s*LEX'
    t.lexer.begin('lexstate')
    return t
def t_lexstate_YACC(t):
    r'%%\s*YACC'
    t.lexer.begin('yaccstate')
    return t
def t_yaccstate_CODE(t):
    r'%%'
    t.lexer.begin('codestate')
    return t
###########
#LEX STATE#
def t_lexstate_LexLITERALS(t):
    r'%literals'
    return t
def t_lexstate_LexIGNORE(t):
    r'%ignore'
    return t
def t_lexstate_LexTOKENS(t):
    r'%tokens'
    return t
def t_lexstate_regex(t):
    r'r\'((\\\')|[^\'])*\''
    t.lexer.begin('regexstate')
    return t
def t_lexstate_POINT(t):
    r'\.'
    t.lexer.begin('errorstate')
    return t
def t_lexstate_fLEX(t):
    r'lex\(\)'
    return t
def t_lexstate_id(t):
    r'[a-zA-Z_]\w*'
    return t
#############
#REGEX STATE#
def t_regexstate_RETURN(t):
    r'return'
    return t
def t_regexstate_apostropheStr(t):
    r'\'[^\']*\''
    return t
def t_regexstate_COMMA(t):
    r','
    return t
def t_regexstate_text(t):
    r'[^\(\)]+'
    return t
def t_regexstate_LPARENTHESIS(t):
    r'\('
    t.lexer.parenthesis += 1
    return t
def t_regexstate_RPARENTHESIS(t):
    r'\)'
    t.lexer.parenthesis -= 1
    if(t.lexer.parenthesis == 0):
        t.lexer.begin('lexstate')
    return t
#############    
#ERROR STATE#
def t_errorstate_ERROR(t):
    r'error'
    return t
def t_errorstate_quotationStr(t):
    r'f?\"[^"]*\"'
    return t
def t_errorstate_COMMA(t):
    r','
    return t
def t_errorstate_text(t):
    r'[^\(\)]+'
    return t
def t_errorstate_LPARENTHESIS(t):
    r'\('
    t.lexer.parenthesis += 1
    return t
def t_errorstate_RPARENTHESIS(t):
    r'\)'
    t.lexer.parenthesis -= 1
    if(t.lexer.parenthesis == 0):
        t.lexer.begin('lexstate')
    return t
############
#YACC STATE#
def t_yaccstate_YaccPRECEDENCE(t):
    r'%precedence'
    return t
def t_yaccstate_EQUALS(t):
    r'='
    t.lexer.begin('yaccvariablestate')
    return t
def t_yaccstate_COLON(t):
    r':'
    t.lexer.begin('productionstate')
    return t
#####################
#YACC VARIABLE STATE#
def t_yaccvariablestate_LBRACKET(t):
    r'\['
    return t
def t_yaccvariablestate_RBRACKET(t):
    r'\]'
    return t
def t_yaccvariablestate_text(t):
    r'.+'
    return t
def t_yaccvariablestate_newline(t):
    r'\n'
    t.lexer.begin('yaccstate')
##################
#PRODUCTION STATE#
def t_productionstate_PREC(t):
    r'%prec'
    return t
def t_productionstate_LCBRACKET(t):
    r'\{'
    t.lexer.begin('productioncode')
    return t
#################
#PRODUCTION CODE#
def t_productioncode_text(t):
    r'[^\}]+'
    return t
def t_productioncode_RCBRACKET(t):
    r'\}'
    t.lexer.begin('yaccstate')
    return t





def t_codestate_DEF(t):
    r'^def'
    t.lexer.begin('codestate')
    return t
def t_codestate_functionParameters(t):
    r'[a-zA-Z_]\w*\([a-zA-Z_]\w*\):'
    t.lexer.begin('functionstate')
    return t
def t_codestate_fYACC(t):
    r'yacc\(\)'
    return t
def t_functionstate_functionText(t):
    r'(.*\n(\s|\t)+)+'
    t.lexer.begin('codestate')
    return t

#####
#ANY#
def t_ANY_quotationStr(t):
    r'\"[^"]*\"'
    return t
def t_ANY_apostropheStr(t):
    r'\'[^\']*\''
    return t
def t_ANY_COMMA(t):
    r','
    return t
def t_ANY_id(t):
    r'[a-zA-Z_]\w*'
    return t
def t_ANY_LPARENTHESIS(t):
    r'\('
    return t
def t_ANY_RPARENTHESIS(t):
    r'\)'
    return t
def t_ANY_LBRACKET(t):
    r'\['
    return t
def t_ANY_RBRACKET(t):
    r'\]'
    return t
def t_ANY_newline(t):
    r'\n'
    pass
def t_ANY_comment(t):
    r'\#.*'
    pass  
def t_ANY_EQUALS(t):
    r'='
    return t
def t_ANY_error(t):
    #print("Caráter Ilegal:", t.value[0])
    t.lexer.skip(1)

t_functionstate_ignore = ""
t_ANY_ignore = " \t"

lexer = lex.lex()
lexer.parenthesis = 0

#import sys
#program = sys.stdin.read()
#lexer.input(program)
#for tok in lexer:
#    print(tok)