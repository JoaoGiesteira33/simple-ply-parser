import sys
import re
import ply.lex as lex

tokens = ["LEX","YACC",
        "LITERALS","LITERAL","FIMLITERAL",
        "IGNORES","IGNORED","FIMIGNORES",
        "TOKENS","FIMTOKENS",
        "TOKENDESC","ERRORDESC",
        "VARIABLE","YACCDEC",
        "PRECEDENCE","PRECEDENCESING","PRECEDENCEFIM"
        "COMMENT","TEXTO"]

states = (
    ("lexState","exclusive"),
    ("yaccState","exclusive"),
    ("lexLiteralsState","exclusive"),
    ("lexIgnoresState","exclusive"),
    ("lexTokensState","exclusive"),
    ("yaccPrecedenceState","exclusive"),
)

tokenDescription = re.compile(r'^(.*[^\s])\s*return\(\s*\'(\w+)\'\s*,\s*([^\s]*)\s*\)')
errorDescription = re.compile(r'\.\s*error\(\s*f\"(.+)\"\s*,\s*(.+)\s*\)')

yacc_state_variables = [] #Print when yacc is declared
yacc_variable_name = ""

#Entering States
def t_ANY_LEX(t):
    r'%%\s*LEX'
    print("import ply.lex as lex")
    print()
    t.lexer.begin("lexState")

def t_ANY_YACC(t):
    r'%%\s*YACC'
    print()
    print("import ply.yacc as yacc")
    t.lexer.begin("yaccState")

#Lexer
def t_lexState_LITERALS(t):
    r'%literals\s*=\s*"'
    print("literals = [",end="")
    t.lexer.begin("lexLiteralsState")

def t_lexState_IGNORES(t):
    r'%ignore\s*=\s*"'
    print("t_ignore = \"",end="")
    t.lexer.begin("lexIgnoresState")

def t_lexState_TOKENS(t):
    r'%tokens\s*=\s*\['
    print(t.value[1:],end="")
    t.lexer.begin("lexTokensState")

def t_lexState_TOKENDESC(t):
    r'^.*\s*return\(.*\)'
    print()
    aux = tokenDescription.match(t.value)
    print("def t_" + aux.group(2) + "(t):")
    print("\tr\'"+ aux.group(1) + "\'")
    print("\treturn " + aux.group(3))

def t_lexState_ERRORDESC(t):
    r'\.(\s|\n)*error\(.+\)'
    print()
    aux = errorDescription.match(t.value)
    print("def t_error(t):")
    print("\tprint(\""+aux.group(1)+"\")")
    print("\t"+aux.group(2))

t_lexState_ignore = "\t\n"

#Lexer - Literals
def t_lexLiteralsState_FIMLITERAL(t):
    r'.\"'
    print("\'"+t.value[0]+"\'",end="]\n")
    t.lexer.begin("lexState")

def t_lexLiteralsState_LITERAL(t):
    r'.'
    print("\'"+t.value+"\'",end=",")

#Lexer - Ignores
def t_lexIgnoresState_FIMIGNORES(t):
    r'.\"'
    print(t.value[0],end="\"\n")
    t.lexer.begin("lexState")

def t_lexIgnoresState_IGNORED(t):
    r'.'
    print(t.value,end="")

#Lexer - Tokens
def t_lexTokensState_FIMTOKENS(t):
    r'\]'
    print(t.value)
    t.lexer.begin("lexState")

def t_lexTokensState_TEXTO(t):
    r'.'
    print(t.value,end="")

#Yacc State
def t_yaccState_YACCDEC(t):
    r'^[a-zA-Z_]\w*\s*=\s*yacc\(\)'
    aux = re.match(r'^([a-zA-Z_]\w*)\s*=',t.value)
    yacc_variable_name = aux.group(1) #Save yacc() variable name
    print("\n"+t.value)
    for v in yacc_state_variables:
        print(yacc_variable_name + "." + v)

def t_yaccState_VARIABLE(t):
    r'^[a-zA-Z_]\w*\s*=\s*.+\s*'
    yacc_state_variables.append(t.value)

def t_yaccState_PRECEDENCE(t):
    r'%precedence\s*=\s*\['
    print("\nprecendence = (",end="")
    t.lexer.begin("yaccPrecedenceState")

t_yaccState_ignore = "\t\n"

#Yacc - Precedence

def t_yaccPrecedenceState_PRECEDENCEFIM(t):
    r'\]'
    print("\t)\n")
    t.lexer.begin("yaccState")

def t_yaccPrecedenceState_TEXTO(t):
    r'.|\n'
    print(t.value,end="")

#Comments

def t_ANY_COMMENT(t):
     r'\#.*$'
     print(t.value)
     #pass to ignore comments

#Resto

def t_ANY_TEXTO(t):
    r'.|\n'
    #print(t.value,end="")

t_ANY_ignore = '\t'

def t_ANY_error(t):
    t.lexer.skip(1)

lexer = lex.lex()

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass