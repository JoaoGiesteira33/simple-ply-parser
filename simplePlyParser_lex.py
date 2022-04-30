# Compilador
#
# prog.txt
#
import ply.lex as lex

literals = ['(',')',',','=','[',']',
            '.',':','}','{']
tokens = ['LEX','YACC','CODE',
        'LexLITERALS','LexIGNORE','LexTOKENS','fLEX',
        'YaccPRECEDENCE','fYACC',
        'DEF','RETURN','ERROR',
        'ID',
        'quotationStr','apostropheStr','regex',
        'COMMENT','TEXTO']

def t_LEX(t):
    r'%%\s*LEX'
    return t
def t_YACC(t):
    r'%%\s*YACC'
    return t
def t_CODE(t):
    r'%%'
    return t

def t_LexLITERALS(t):
    r'%literals'
    return t
def t_LexIGNORE(t):
    r'%ignore'
    return t
def t_LexTOKENS(t):
    r'%tokens'
    return t
def t_fLEX(t):
    r'lex\(\)'
    return t

def t_YaccPRECEDENCE(t):
    r'%precedence'
    return t
def t_fYACC(t):
    r'yacc\(\)'
    return t

def t_DEF(t):
    r'def'
    return t
def t_RETURN(t):
    r'return'
    return t
def t_ERROR(t):
    r'error'
    return t

def t_regex(t):
    r'r\'((\\\')|[^\'])*\''
    return t
def t_quotationStr(t):
    r'\"[^"]*\"'
    return t
def t_apostropheStr(t):
    r'\'[^\']*\''
    return t
def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t

t_ignore = " \t\n"

#def t_newline(t):
   # r'\n'
    #t.lexer.lexpos += t.lexer.lexpos + 1

def t_COMMENT(t):
     r'\#.*'
     pass
     # No return value. Token discarded

def t_error(t):
    #print("Caráter Ilegal:", t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()
#import sys
#program = sys.stdin.read()
#lexer.input(program)
#for tok in lexer:
#    print(tok)