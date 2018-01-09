import AST
from AST import addToClass
from functools import reduce

operations = {
    '+' : "ADD",
    '-' : "SUB",
    '*' : "MULT",
    '/' : "DIV",
}

functiondefs = "\n#functiondefs\n\n"

indent = "    "

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
        bytecode += "%s" % self.tok
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
        bytecode += operations[self.op]

    return bytecode

@addToClass(AST.AssignNode)
def compile(self):
    return self.children[1].compile() + "SET %s\n" % self.children[0].tok
    
@addToClass(AST.EmptyProgramNode)
def compile(self):
    return ""
    
@addToClass(AST.ShowNode)
def compile(self):
    return "\ncurrentScene = " + self.children[0].compile()
    
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

@addToClass(AST.MemberNode)
def compile(self):
    bytecode = "" + self.children[0].compile() + "." + self.children[0].compile();
    return bytecode

if __name__ == "__main__":
    from parserPandCl import parse
    import sys, os
    prog = open(sys.argv[1]).read()
    ast = parse(prog)
    compiled = ast.compile()
    name = os.path.splitext(sys.argv[1])[0] + '.py'
    outfile = open(name, 'w')
    outfile.write("import pygame\nimport time\nfrom time import sleep\n")
    outfile.write("from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE\n")
    outfile.write("import sys\nscreen_x = 1000\nscreen_y = 700\nt1 = 0\ntsum = 0")
    
    outfile.write(functiondefs)
    outfile.write(compiled)
    
    outfile.write("\ndef printScene():")
    outfile.write("\n" + indent + "global t1, tsum")
    outfile.write("\n" + indent + "t2 = time.time()")
    outfile.write("\n" + indent + "tsum += t2 - t1")
    outfile.write("\n" + indent + "t1 = t2")
    outfile.write("\n" + indent + "if tsum >= 1/30.0:")
    outfile.write("\n" + indent + indent + "tsum = 0")
    outfile.write("\n" + indent + indent + "window.blit(currentScene['bg'],(0,0))")
    outfile.write("\n" + indent + indent + "for i in range(0,len(currentScene['cli'])):")
    outfile.write("\n" + indent + indent + indent + "window.blit(currentScene['cli'][i]['img'],(currentScene['cli'][i]['geo'][0],currentScene['cli'][i]['geo'][1]))")
    outfile.write("\n" + indent + indent + "pygame.display.flip()")
    outfile.write("\n" + "if __name__ == \"__main__\":")
    outfile.write("\n" + indent + "pygame.init() ")
    outfile.write("\n" + indent + "window = pygame.display.set_mode((screen_x, screen_y))") 
    outfile.write("\n" + indent + "pygame.display.set_caption('Point & Click')")
    outfile.write("\n" + indent + "screen = pygame.display.get_surface()") 
    outfile.write("\n" + indent + "font = pygame.font.Font(None,30)")
    outfile.write("\n" + indent + "while True:")
    outfile.write("\n" + indent + indent + "printScene()")
    outfile.write("\n" + indent + indent + "for event in pygame.event.get():")
    outfile.write("\n" + indent + indent + indent + "if event.type == QUIT:")
    outfile.write("\n" + indent + indent + indent + indent + "sys.exit(0)")
    outfile.write("\n" + indent + indent + indent + "elif event.type == MOUSEBUTTONDOWN:")
    outfile.write("\n" + indent + indent + indent + indent + "(mX,mY) = pygame.mouse.get_pos()")
    outfile.write("\n" + indent + indent + indent + indent + "for i in range(0,len(currentScene['cli'])):")
    outfile.write("\n" + indent + indent + indent + indent + indent + "if(mX > currentScene['cli'][i]['geo'][0] and mY > currentScene['cli'][i]['geo'][1] and mX < currentScene['cli'][i]['geo'][2] + currentScene['cli'][i]['geo'][0] and mY < currentScene['cli'][i]['geo'][3] + currentScene['cli'][i]['geo'][1]):")
    outfile.write("\n" + indent + indent + indent + indent + indent + indent + "currentScene['cli'][i]['func']()")
    outfile.close()
    print("Wrote output to", name)
