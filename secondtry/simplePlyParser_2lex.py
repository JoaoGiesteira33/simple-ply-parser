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
        'DEF','RETURN','ERROR','FUNCTIONEND','PARSE',
        'id',
        'quotationStr','apostropheStr','regex',
        'comment','text']

states = (
    ('lexstate','exclusive'),
    ('yaccstate','exclusive'),
    ('codestate','exclusive'),
    ('regexstate','exclusive'),
    ('errorstate','exclusive'),
    ('yaccvariablestate','exclusive'),
    ('precedencestate','exclusive'),
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
    t.lexer.begin('precedencestate')
    return t
def t_yaccstate_EQUALS(t):
    r'='
    t.lexer.begin('yaccvariablestate')
    return t
def t_yaccstate_COLON(t):
    r':'
    t.lexer.begin('productionstate')
    return t
##################
#PRECEDENCE STATE#
def t_precedencestate_RBRACKET(t):
    r'\]'
    t.lexer.begin('yaccstate')
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
############
#CODE STATE#
def t_codestate_DEF(t):
    r'def'
    return t
def t_codestate_COLON(t):
    r':'
    t.lexer.begin('functionstate')
    return t
def t_codestate_fYACC(t):
    r'yacc\(\)'
    return t
def t_codestate_POINT(t):
    r'\.'
    return t
def t_codestate_PARSE(t):
    r'parse'
    return t
################
#FUNCTION STATE#
def t_functionstate_DEF(t):
    r'def'
    t.lexer.begin('codestate')
    return t
def t_functionstate_text(t):
    r'(.|\t|\ )+'
    return t
def t_functionstate_newline(t):
    r'\n\ '
def t_functionstate_FUNCTIONEND(t):
    r'\n'
    t.lexer.begin('codestate')
    return t
#def t_codestate_functionParameters(t):
#    r'[a-zA-Z_]\w*\([a-zA-Z_]\w*\):'
#    t.lexer.begin('functionstate')
#    return t


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

t_ANY_ignore = ""
t_regexstate_ignore = " \t"
t_errorstate_ignore = " \t"
t_productioncode_ignore = " "

lexer = lex.lex()
lexer.parenthesis = 0

#import sys
#program = sys.stdin.read()
#lexer.input(program)
#for tok in lexer:
#    print(tok)