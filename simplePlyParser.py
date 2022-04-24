import sys
import ply.lex as lex

tokens = ["LEX","TEXTO"]

states = (
    ("lexState","exclusive"),
    #("yaccState","exclusive"),
)

#Entering States
def t_ANY_LEX(t):
    r'%% LEX'
    print("import ply.lex as lex")
    t.lexer.begin("lexState")

#Resto

def t_ANY_TEXTO(t):
    r'.|\n'
    #print(t.value,end="")

t_ANY_ignore = ' \t\n'

def t_ANY_error(t):
    t.lexer.skip(1)


lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass