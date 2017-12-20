import ply.yacc as yacc
import AST

from lex import tokens

operations = {
    '+' : lambda x,y: x+y,
    '-' : lambda x,y: x-y,
    '*' : lambda x,y: x*y,
    '/' : lambda x,y: x/y
}

precedence = (
    ('left', 'ADD_OP'),
    ('left', 'MULT_OP'),
    ('right', 'UMINUS')
)

def p_program(p):
    '''program : statement
        | statement ';'
        | statement ';' program'''
    try:
        p[0] = AST.ProgramNode([p[1]] + p[3].children)
    except IndexError:
        p[0] = AST.ProgramNode(p[1])
    print("==========================")
    print(p[0])

#statement : id = { program }
def p_statement(p):
    '''statement : ID '=' expression
        | member '=' expression
        | structure
        | PRINT expression'''
    try:
        p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])
    except IndexError:
        if p[1] == 'print':
            p[0] = AST.PrintNode(p[2])
        else:
            p[0] = p[1]
            

def p_structure(p):
    '''structure : WHILE '(' expression ')' '{' program '}'
        | IF '(' expression ')' '{' program '}'
        | ':' expression '''
    if p[1] == 'while':
        p[0] = AST.WhileNode([p[3], p[6]])
    elif p[1] == 'if':
        p[0] = AST.IfNode([p[3], p[6]])
    elif p[1] == ':':
        p[0] = AST.ShowNode([p[2]])

# Type area.

def p_scene_type(p):
    '''scene : SCENE '(' expression ',' '[' id_list ']' ')' '''
    p[0] = AST.SceneNode([p[3], p[6]])


def p_cli_type(p):
    '''cli : CLI '(' expression ',' rect ')' '{' program '}' '''
    p[0] = AST.CliNode([p[3], p[5], p[8]])

def p_rect_type(p):
    '''rect : RECT '(' expression ',' expression ',' expression ',' expression ')' '''
    p[0] = AST.RectNode([p[3], p[5], p[7], p[9]])


def p_id_list(p):
    '''id_list : expression
    | expression ',' id_list '''
    try:
        p[0] = AST.IdListNode([p[1], p[3]])
    except IndexError:
        p[0] = AST.IdListNode(p[1])


# Expression area.
def p_expression_op(p):
    '''expression : expression ADD_OP expression
         | expression MULT_OP expression'''
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_number(p):
    '''expression : NUMBER'''
    p[0] = AST.TokenNode(p[1])

def p_variable(p):
    '''expression : ID'''
    p[0] = AST.TokenNode(p[1])
    
def p_string(p):
    '''expression : STRING'''
    p[0] = AST.TokenNode(p[1])
    
def p_scene(p):
    '''expression : scene'''
    p[0] = AST.SceneNode(p[1])

def p_cli(p):
    '''expression : cli'''
    p[0] = AST.CliNode(p[1])
    
def p_cli(p):
    '''expression : '{' program '}' '''
    p[0] = AST.CliNode(p[2])

def p_parenthesis(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]
    
def p_member(p):
    '''member : iden '.' FUNC
         | iten '.' IMG'''
    p[0] = AST.MemberNode([p[1], p[3]])
    print(p[0])
    print("äöäöäöäöäö")

def p_uminus(p):
    'expression : ADD_OP expression %prec UMINUS'
    #p[0] = operations[p[1]](0,p[2])
    p[0] = AST.OpNode(p[1], [p[2]])

def p_error(p):
    print ("syntax error in line %d" % p.lineno)
    yacc.errok()
def parse(program):
    return yacc.parse(program)

yacc.yacc(outputdir = 'generated')

if __name__ == "__main__":
    import sys
    import os

    prog = open(sys.argv[1]).read()
    result = yacc.parse(prog, debug=1)
    #print(result)

    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    #graph.write_pdf(name)
    print("wrote ast to", name)
