import ply.lex as lex

reserved_words = (
    'while',
    'if',
    'print',
    'CLI',
    'RECT',
    'SCENE',
    'FUNC',
    'IMG',
)

tokens = (
    'NUMBER',
    'ADD_OP',
    'MULT_OP',
    'ID',
    'STRING',
) + tuple(map(lambda s:s.upper(), reserved_words))

literals = r'(){}[],;:='

# r : row, on évite les \.
t_ignore = ' \t'

def t_ADD_OP(t):
    r'[\+-]'
    return t

def t_MULT_OP(t):
    r'[\*\/]'
    return t

def t_NUMBER(t):
    r'(\d+(\.\d+)?|\.\d+)' # Docstring (kind of). Lu par lex (spécial).
    t.value = float(t.value) #TRY CATCH
    return t

def t_ID(t):
    r'([a-zA-Z_][\w_]*)'
    if t.value in reserved_words:
        t.type = t.value.upper()
    return t

def t_STRING(t):
    r'(\"[^\"]*\")'
    return t

def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print ("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex()

if __name__== "__main__":
    import sys
    prog = open(sys.argv [1]).read()
    lex.input (prog)
    while 1:
        tok = lex.token()
        if not tok: break
        print("%s(%s)" % (tok.type, tok.value) )
        #print ("line %d: %s(%s)" % (tok.lineno, tok.type, tok.value))
