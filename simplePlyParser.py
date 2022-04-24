import sys
import re
import ply.lex as lex

tokens = ["LEX","YACC","PYTHON",
        "LITERALS","LITERAL","FIMLITERAL",
        "IGNORES","IGNORED","FIMIGNORES",
        "TOKENS","FIMTOKENS",
        "TOKENDESC","ERRORDESC",
        "LEXDEC",
        "VARIABLE","YACCDEC",
        "PRECEDENCE","PRECEDENCESING","PRECEDENCEFIM",
        "PRODUCTION",
        "COMMENT","TEXTO"]

states = (
    ("lexState","exclusive"),
    ("yaccState","exclusive"),
    ("lexLiteralsState","exclusive"),
    ("lexIgnoresState","exclusive"),
    ("lexTokensState","exclusive"),
    ("yaccPrecedenceState","exclusive"),
    ("pythonState","exclusive"),
)

tokenDescription = re.compile(r'^(.*[^\s])\s*return\(\s*\'(\w+)\'\s*,\s*([^\s]*)\s*\)')
errorDescription = re.compile(r'\.\s*error\(\s*f\"(.+)\"\s*,\s*(.+)\s*\)')
productionDescription = re.compile(r'^(([a-zA-Z_]\w*)\s+:\s+.+[^\s])\s*{\s*(.*)\s*}')
lexerDeclaration = re.compile(r'([a-zA-Z]\w*)\s*=\s*lex\(\)')

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

def t_ANY_PYTHON(t):
    r'%%'
    t.lexer.begin("pythonState")

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
    print("\tt.value = " + aux.group(3))
    print("\treturn t")

def t_lexState_ERRORDESC(t):
    r'\.(\s|\n)*error\(.+\)'
    print()
    aux = errorDescription.match(t.value)
    print("def t_error(t):")
    print("\tprint(\""+aux.group(1)+"\")")
    print("\t"+aux.group(2))

def t_lexState_LEXDEC(t):
    r'[a-zA-Z]\w*\s*=\s*lex\(\)'
    aux = lexerDeclaration.match(t.value)
    print("\n"+aux.group(1)+"=lex.lex()")

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
def t_yaccState_PRECEDENCE(t):
    r'%precedence\s*=\s*\['
    print("\nprecedence = (",end="")
    t.lexer.begin("yaccPrecedenceState")

def t_yaccState_PRODUCTION(t):
    r'^[a-zA-Z_]\w*\s+:\s+(.+)\s*{(.*)}'
    aux = productionDescription.match(t.value)
    print("def p_"+ aux.group(2) + "_" + str(lexer.nProductions) + "(t):")
    lexer.nProductions += 1
    print("\t"+"\""+aux.group(1)+"\"")
    print("\t"+aux.group(3))

def t_yaccState_VARIABLE(t):
    r'^[a-zA-Z_]\w*\s*=\s*.+\s*'
    print(t.value)

t_yaccState_ignore = "\t\n"

#Yacc - Precedence

def t_yaccPrecedenceState_PRECEDENCEFIM(t):
    r'\]'
    print(")\n")
    t.lexer.begin("yaccState")

def t_yaccPrecedenceState_TEXTO(t):
    r'.|\n'
    print(t.value,end="")

#Python
def t_pythonState_YACCDEC(t):
    r'yacc\(\)'
    print("yacc.yacc()",end="")

def t_pythonState_TEXTO(t):
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
lexer.nProductions = 0

for linha in sys.stdin:
    lexer.input(linha)
    for tok in lexer:
        pass