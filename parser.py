import ply.yacc as yacc
import AST

from lex5 import tokens

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

variables = {}

def p_program(p):
    '''program : statement
        | statement ';'
        | statement ';' program'''
    try:
        p[0] = AST.ProgramNode([p[1]] + p[3].children)
    except IndexError:
        p[0] = AST.ProgramNode(p[1])

def p_statement(p):
    '''statement : ID '=' expression
        | structure
        | PRINT expression'''
    try:
        #variables[p[1]] = p[3]
        p[0] = AST.AssignNode([AST.TokenNode(p[1]), p[3]])
    except IndexError:
        if p[1] == 'print':
            p[0] = AST.PrintNode(p[2])
        else:
            p[0] = p[1]

def p_structure(p):
    '''structure : WHILE '(' expression ')' '{' program '}'
        | IF '(' expression ')' '{' program '}'
        | ':' ID '''
    if p[1] == 'while':
        p[0] = AST.WhileNode([p[3], p[6]])
    elif p[1].type == "if":
        p[0] = AST.IfNode([p[3], p[6]])
    elif p[1].type == ":":
        p[0] = AST.ShowNode([p[2]])

def p_expression_op(p):
    '''expression : expression ADD_OP expression
         | expression MULT_OP expression'''
    #p[0] = operations[p[2]](p[1], p[3])
    p[0] = AST.OpNode(p[2], [p[1], p[3]])

def p_number(p):
    '''expression : NUMBER'''
    p[0] = AST.TokenNode(p[1])

def p_variable(p):
    '''expression : ID'''
    #p[0] = variables[p[1]]
    p[0] = AST.TokenNode(p[1])

def p_parenthesis(p):
    '''expression : '(' expression ')' '''
    p[0] = p[2]

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
    result = yacc.parse(prog, debug=0)
    #print(result)

    graph = result.makegraphicaltree()
    name = os.path.splitext(sys.argv[1])[0]+'-ast.pdf'
    graph.write_pdf(name)
    print("wrote ast to", name)
