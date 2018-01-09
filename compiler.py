import AST
from AST import addToClass
from functools import reduce

operations = {
    '+' : "ADD",
    '-' : "SUB",
    '*' : "MULT",
    '/' : "DIV",
}
imgDecleration = {}
funcDecleration = {}
functiondefs = "\n#functiondefs\n\n"
nbIndent = 0
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
    #if isinstance(self.tok, str):
    bytecode += "%s" % self.tok
    return bytecode

@addToClass(AST.OpNode)
def compile(self):
    bytecode = ""
    args = [c.compile() for c in self.children]

    if len(args) == 1:
        if self.op == '-':
            bytecode += "-" + args[0]
    else:
        bytecode += args[0] + " "
        bytecode += self.op + " "
        bytecode += args[1]

    return bytecode

@addToClass(AST.PathNode)
def compile(self):
    if not self.children[0].compile() in imgDecleration:
        imgDecleration.update({self.children[0].compile() : len(imgDecleration)})
    bytecode = "img"
    bytecode += str(imgDecleration[self.children[0].compile()])
    return bytecode
    
@addToClass(AST.PathNode)
def read(self):
    return self.children[0].compile()
    
@addToClass(AST.AssignNode)
def compile(self):
    global nbIndent
    bytecode = ""
    if(self.children[1].type == 'cli' or self.children[1].type == 'scene' or self.children[1].type == 'rect'):
        if(len(self.children[0].children) > 1):
            bytecode += self.children[0].children[0].compile() + " = {}\n"
        else:
            bytecode += self.children[0].compile() + " = {}\n"
    if(self.children[1].type != 'Program'):
        bytecode += indent * nbIndent + self.children[0].compile() + " = " + str(self.children[1].compile()) + "\n"
    else:
        tmpNbIndent = nbIndent
        nbIndent = 1
        funcDecleration.update({len(funcDecleration): self.children[1].compile()})
        nbIndent = tmpNbIndent
        bytecode += indent * nbIndent + self.children[0].compile() + " = f" + str(len(funcDecleration) - 1) + "\n"
        
    return bytecode
    
@addToClass(AST.EmptyProgramNode)
def compile(self):
    return ""
    
@addToClass(AST.ShowNode)
def compile(self):
    return indent * nbIndent + "currentScene = " + self.children[0].compile() + "\n"
    
@addToClass(AST.PrintNode)
def compile(self):
    return indent * nbIndent + "print(str(" + self.children[0].compile() + "))\n"
@addToClass(AST.ConditionNode)
def compile(self):
    bytecode = ""
    if(len(self.children) == 4):
        bytecode = self.children[0].compile() + " " + self.children[1].compile() + self.children[2].compile() + " " + self.children[3].compile()
    else:
        bytecode = self.children[0].compile() + " " + self.children[1].compile() + " " + self.children[2].compile()
    return bytecode
    
@addToClass(AST.WhileNode)
def compile(self):
    global nbIndent
    #global bodyCount
    bytecode = ""
    #tmpCount = bodyCount
    #bodyCount += 1

    #bytecode += "JMP cond%s\n" % tmpCount
    #bytecode += "body%s: " % tmpCount
    #bytecode += self.children[1].compile()
    #bytecode += "cond%s: " % tmpCount
    #bytecode +=  self.children[0].compile()
    #bytecode += "JINZ body%s\n" %tmpCount
    
    bytecode += indent * nbIndent + "while(" + self.children[0].compile() + "):\n"
    nbIndent += 1
    bytecode += self.children[1].compile()
    nbIndent -= 1

    return bytecode

@addToClass(AST.IfNode)
def compile(self):
    global nbIndent
    bytecode = ""
    bytecode += indent * nbIndent + "if(" + self.children[0].compile() + "):\n"
    nbIndent += 1
    bytecode += self.children[1].compile()
    nbIndent -= 1

    return bytecode
    
@addToClass(AST.MemberNode)
def compile(self):
    bytecode = self.children[0].compile() + "["
    if(self.children[1].compile() != 'IMG' and self.children[1].compile() != 'FUNC'):
        bytecode += "'geo']"
    bytecode += "['" + str(self.children[1].compile()).lower() + "']"
    #bytecode = "" + self.children[0].compile() + "." + self.children[1].compile();
    return bytecode
    
@addToClass(AST.TabNode)
def compile(self):
    return self.children[0].compile() + "['cli'][" + str(int(float(self.children[1].compile()))) + "]"

@addToClass(AST.SceneNode)
def compile(self):
    #if not self.children[0].compile() in imgDecleration:
    #    imgDecleration.update({self.children[0].compile() : len(imgDecleration)})
    self.children[0].compile()
    bytecode = "{'bg' : img"
    bytecode += str(imgDecleration[self.children[0].read()])
    bytecode += ", 'cli' : ["
    bytecode += self.children[1].compile()
    bytecode += "]}"
    return bytecode
    
@addToClass(AST.IdListNode)
def compile(self):
    bytecode = ""
    bytecode += self.children[0].compile()
    if(len(self.children) > 1):
        bytecode += ", " + self.children[1].compile()
    return bytecode
    
@addToClass(AST.CliNode)
def compile(self):
    global nbIndent
    #if not self.children[0].compile() in imgDecleration:
    #    imgDecleration.update({self.children[0].compile() : len(imgDecleration)})
    self.children[0].compile()
    tmpNbIndent = nbIndent
    nbIndent = 1
    funcDecleration.update({len(funcDecleration): self.children[2].compile()})
    nbIndent = tmpNbIndent
    bytecode = "{'img' : img"
    bytecode += str(imgDecleration[self.children[0].read()])
    bytecode += ", 'geo' : "
    bytecode += self.children[1].compile()
    bytecode += ", 'func' : f"
    bytecode += str(len(funcDecleration) - 1)
    bytecode += "}"
    return bytecode
    
@addToClass(AST.RectNode)
def compile(self):
    bytecode = "{'x' : "
    bytecode += self.children[0].compile()
    bytecode += ",'y' : "
    bytecode += self.children[1].compile()
    bytecode += ",'h' : "
    bytecode += self.children[2].compile()
    bytecode += ",'w' : "
    bytecode += self.children[3].compile()
    bytecode += "}"
    return bytecode
    
def imgdeclarate():
    bytecode = ""
    for keys,values in imgDecleration.items():
        bytecode += "img" + str(values) + " = pygame.image.load(" + keys + ")\n"
    return bytecode
    
def funcdeclarate():
    global nbIndent
    bytecode = ""
    for keys,values in funcDecleration.items():
        nbIndent += 1
        bytecode += "def f" + str(keys) + "():\n" + values + "\n"
        nbIndent -= 1
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
    outfile.write("import sys\nscreen_x = 1000\nscreen_y = 700\nt1 = 0\ntsum = 0\n")

    outfile.write(imgdeclarate())
    outfile.write(funcdeclarate())
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
    outfile.write("\n" + indent + indent + indent + "window.blit(currentScene['cli'][i]['img'],(currentScene['cli'][i]['geo']['x'],currentScene['cli'][i]['geo']['y']))")
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
    outfile.write("\n" + indent + indent + indent + indent + indent + "if(mX > currentScene['cli'][i]['geo']['x'] and mY > currentScene['cli'][i]['geo']['y'] and mX < currentScene['cli'][i]['geo']['w'] + currentScene['cli'][i]['geo']['x'] and mY < currentScene['cli'][i]['geo']['h'] + currentScene['cli'][i]['geo']['y']):")
    outfile.write("\n" + indent + indent + indent + indent + indent + indent + "currentScene['cli'][i]['func']()")
    outfile.close()
    print("Wrote output to", name)
