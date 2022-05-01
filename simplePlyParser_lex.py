# Compilador
#
# prog.txt
#
import ply.lex as lex

literals = ['(',')',',','=','[',']',
            '.',':','}','{']
tokens = ['LEX','YACC','CODE',
        'LexLITERALS','LexIGNORE','LexTOKENS','fLEX',
        'YaccPRECEDENCE','fYACC','YaccVariable','PREC',
        'DEF','RETURN','ERROR',
        'id',
        'quotationStr','apostropheStr','regex',
        'comment','productioncode']

states = (
    ('lexstate','exclusive'),
    ('yaccstate','exclusive'),
    ('codestate','exclusive'),
)

def t_ANY_LEX(t):
    r'%%\s*LEX'
    t.lexer.begin('lexstate')
    return t
def t_ANY_YACC(t):
    r'%%\s*YACC'
    t.lexer.begin('yaccstate')
    return t
def t_ANY_CODE(t):
    r'%%'
    t.lexer.begin('codestate')
    return t

def t_lexstate_LexLITERALS(t):
    r'%literals'
    return t
def t_lexstate_LexIGNORE(t):
    r'%ignore'
    return t
def t_lexstate_LexTOKENS(t):
    r'%tokens'
    return t
def t_lexstate_fLEX(t):
    r'lex\(\)'
    return t

def t_yaccstate_YaccPRECEDENCE(t):
    r'%precedence'
    return t
def t_yaccstate_PREC(t):
    r'%prec'
    return t
def t_yaccstate_fYACC(t):
    r'yacc\(\)'
    return t

def t_codestate_DEF(t):
    r'def'
    return t
def t_lexstate_RETURN(t):
    r'return\(\s*\'(\w+)\'\s*,\s*([^\s]*)\s*\)'
    return t
def t_lexstate_ERROR(t):
    r'error\(\s*f\"(.+)\"\s*,\s*(.+)\s*\)'
    return t

def t_lexstate_regex(t):
    r'r\'((\\\')|[^\'])*\''
    return t
def t_ANY_quotationStr(t):
    r'\"[^"]*\"'
    return t
def t_ANY_apostropheStr(t):
    r'\'[^\']*\''
    return t

def t_yaccstate_YaccVariable(t):
    r'[a-zA-Z_]\w*\s*=\s*.*[^\s]'
    return t
def t_ANY_id(t):
    r'[a-zA-Z_]\w*'
    return t
def t_yaccstate_productioncode(t):
    r'\{.*\}'
    return t



t_ANY_ignore = " \t"

def t_ANY_newline(t):
    r'\n'
    pass
def t_ANY_comment(t):
    r'\#.*'
    pass
     
def t_ANY_error(t):
    #print("Caráter Ilegal:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
#import sys
#program = sys.stdin.read()
#lexer.input(program)
#for tok in lexer:
#    print(tok)