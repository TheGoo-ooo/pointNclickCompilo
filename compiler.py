import AST
from AST import addToClass
from functools import reduce

operations = {
    '+' : "ADD",
    '-' : "SUB",
    '*' : "MULT",
    '/' : "DIV",
}

bodyCount = 1 # Flag jump for while(cond){}

@addToClass(AST.ProgramNode)
def compile(self):
    bytecode = ""
    for c in self.children:
        bytecode += str(c.compile())
    return bytecode

@addToClass(AST.TokenNode)
def compile(self):
    bytecode = ""
    if isinstance(self.tok, str):
        bytecode += "PUSHV %s\n" % self.tok
    else:
        bytecode += "PUSHC %s\n" % self.tok
    return bytecode

@addToClass(AST.OpNode)
def compile(self):
    bytecode = ""
    args = [c.compile() for c in self.children]

    if len(args) == 1:
        if self.op == '-':
            bytecode += "USUB %s\n" % args[0]
    else:
        bytecode += args[0]
        bytecode += args[1]
        bytecode += "%s\n" % operations[self.op]

    return bytecode

@addToClass(AST.AssignNode)
def compile(self):
    return self.children[1].compile() + "SET %s\n" % self.children[0].tok

@addToClass(AST.PrintNode)
def compile(self):
    return self.children[0].compile() + "PRINT\n"

@addToClass(AST.WhileNode)
def compile(self):
    global bodyCount
    bytecode = ""
    tmpCount = bodyCount
    bodyCount += 1

    bytecode += "JMP cond%s\n" % tmpCount
    bytecode += "body%s: " % tmpCount
    bytecode += self.children[1].compile()
    bytecode += "cond%s: " % tmpCount
    bytecode +=  self.children[0].compile()
    bytecode += "JINZ body%s\n" %tmpCount

    return bytecode

if __name__ == "__main__":
    from parser5 import parse
    import sys, os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.vm'
    outfile = open(name, 'w')
    outfile.write(compiled)
    outfile.close()
    print("Wrote output to", name)
