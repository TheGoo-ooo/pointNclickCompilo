import pygame
import time
from time import sleep
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE
import sys
screen_x = 1000
screen_y = 700
t1 = 0
tsum = 0
img0 = pygame.image.load("Assets/text1.png")
img1 = pygame.image.load("Assets/emptycli.png")
img2 = pygame.image.load("Assets/BIPcontent.png")
img3 = pygame.image.load("Assets/bg_erruption.png")
img4 = pygame.image.load("Assets/BIPnormal.png")
img5 = pygame.image.load("Assets/BIPfache.png")
img6 = pygame.image.load("Assets/text2.png")
img7 = pygame.image.load("Assets/toaster.png")
img8 = pygame.image.load("Assets/text3.png")
img9 = pygame.image.load("Assets/text6.png")
img10 = pygame.image.load("Assets/BIPtendu.png")
img11 = pygame.image.load("Assets/bg_sacrifice.png")
img12 = pygame.image.load("Assets/text8.png")
img13 = pygame.image.load("Assets/text4.png")
img14 = pygame.image.load("Assets/BIPtriste.png")
img15 = pygame.image.load("Assets/text7.png")
img16 = pygame.image.load("Assets/BIPwtf.png")
img17 = pygame.image.load("Assets/lavedisp.png")
img18 = pygame.image.load("Assets/text5.png")
img19 = pygame.image.load("Assets/bg_heureu.png")
def f0():
    print(None)

def f1():
    erruptCliBIP['img'] = img2
    errupt = {}
    errupt = {'bg' : img3, 'cli' : [erruptCliBIP]}
    while(erruptCliBIP['geo']['x'] < 500.0):
        erruptCliBIP['geo']['x'] = erruptCliBIP['geo']['x'] + 5.0
        printScene()
        sleep(0.01)
    while(erruptCliBIP['geo']['x'] < 500.0):
        erruptCliBIP['geo']['x'] = erruptCliBIP['geo']['x'] + 5.0
        printScene()
        sleep(0.01)
    while(erruptCliBIP['geo']['y'] > 200.0):
        erruptCliBIP['geo']['y'] = erruptCliBIP['geo']['y'] - 3.0
        printScene()
        sleep(0.01)
    global currentScene
    currentScene = sacrif

def f2():
    erruptCliBIP['img'] = img5
    errupt = {}
    errupt = {'bg' : img3, 'cli' : [erruptCliBIP, errupttext, erruptgotovolcan]}
    global currentScene
    currentScene = errupt

def f3():
    print(None)

def f6():
    print(None)

def f8():
    printScene()

def f9():
    sacrificetoaster['geo']['x'] = 350.0
    sacrificetoaster['geo']['y'] = 150.0
    while(sacrificetoaster['geo']['y'] < 300.0):
        sacrificetoaster['geo']['y'] = sacrificetoaster['geo']['y'] + 1.0
        printScene()
        sleep(0.01)
    sacrificetext['img'] = img13
    while(sacrifCliBIP['geo']['y'] < 700.0):
        sacrifCliBIP['geo']['y'] = sacrifCliBIP['geo']['y'] + 5.0
        printScene()
        sleep(0.01)
    global currentScene
    currentScene = fin

def f7():
    erruptCliBIP['img'] = img10
    errupt = {}
    errupt = {'bg' : img3, 'cli' : [erruptCliBIP, sacrificetoaster]}
    while(erruptCliBIP['geo']['x'] > 500.0):
        erruptCliBIP['geo']['x'] = erruptCliBIP['geo']['x'] - 3.0
        sacrificetoaster['geo']['x'] = sacrificetoaster['geo']['x'] - 3.0
        printScene()
        sleep(0.01)
    while(erruptCliBIP['geo']['y'] > 200.0):
        erruptCliBIP['geo']['y'] = erruptCliBIP['geo']['y'] - 3.0
        sacrificetoaster['geo']['y'] = sacrificetoaster['geo']['y'] - 3.0
        printScene()
        sleep(0.01)
    sacrifLave['func'] = f8
    sacrif = {}
    sacrif = {'bg' : img11, 'cli' : [sacrifCliBIP, sacrificetext, sacrificetoaster, sacrifLave]}
    global currentScene
    currentScene = sacrif
    sacrificetoaster['geo']['y'] = 740.0
    sacrificetoaster['geo']['x'] = 745.0
    sacrificetext['img'] = img1
    while(sacrifCliBIP['geo']['y'] > 400.0):
        sacrifCliBIP['geo']['y'] = sacrifCliBIP['geo']['y'] - 5.0
        sacrificetoaster['geo']['y'] = sacrificetoaster['geo']['y'] - 5.0
        printScene()
        sleep(0.01)
    sacrificetext['img'] = img12
    sacrifLave['func'] = f9

def f10():
    print(None)

def f5():
    sacrificetext['img'] = img9
    sacrifCliBIP['img'] = img10
    sacrificetoaster['geo']['x'] = 745.0
    sacrificetoaster['geo']['y'] = 440.0
    sacrificetoaster['func'] = f6
    printScene()
    a = 1.0
    while(a < 20.0):
        a = a + 1.0
        sleep(0.01)
        printScene()
    while(sacrifCliBIP['geo']['y'] < 700.0):
        sacrifCliBIP['geo']['y'] = sacrifCliBIP['geo']['y'] + 5.0
        sacrificetoaster['geo']['y'] = sacrificetoaster['geo']['y'] + 5.0
        printScene()
        sleep(0.01)
    erruptCliBIP['geo']['x'] = 750.0
    erruptCliBIP['geo']['y'] = 500.0
    erruptgotovolcan['func'] = f7
    erruptCliBIP['img'] = img14
    sacrificetext['img'] = img15
    sacrificetoaster['geo']['y'] = 540.0
    erruptCliBIP['func'] = f10
    errupt = {}
    errupt = {'bg' : img3, 'cli' : [erruptCliBIP, sacrificetoaster, sacrificetext, erruptgotovolcan]}
    global currentScene
    currentScene = errupt

def f4():
    sacrificetext['img'] = img8
    sacrifCliBIP['img'] = img4
    sacrifCliBIP['func'] = f5
    sacrif = {}
    sacrif = {'bg' : img11, 'cli' : [sacrifCliBIP, sacrificetext, sacrificetoaster, sacrifLave]}
    global currentScene
    currentScene = sacrif

def f11():
    sacrificetext['img'] = img6
    sacrif = {}
    sacrif = {'bg' : img11, 'cli' : [sacrifCliBIP, sacrificetext, sacrificetoaster, sacrifLave]}
    global currentScene
    currentScene = sacrif

def f12():
    sacrificetoaster['geo']['x'] = 350.0
    sacrificetoaster['geo']['y'] = 150.0
    while(sacrificetoaster['geo']['y'] < 300.0):
        sacrificetoaster['geo']['y'] = sacrificetoaster['geo']['y'] + 1.0
        printScene()
        sleep(0.01)
    sacrificetext['img'] = img13
    while(sacrifCliBIP['geo']['y'] < 700.0):
        sacrifCliBIP['geo']['y'] = sacrifCliBIP['geo']['y'] + 5.0
        printScene()
        sleep(0.01)
    global currentScene
    currentScene = fin

def f13():
    print(None)

def f14():
    print(None)


#functiondefs

errupttext = {}
errupttext = {'img' : img0, 'geo' : {'x' : 250.0,'y' : 500.0,'h' : 100.0,'w' : 500.0}, 'func' : f0}
erruptgotovolcan = {}
erruptgotovolcan = {'img' : img1, 'geo' : {'x' : 250.0,'y' : 250.0,'h' : 100.0,'w' : 500.0}, 'func' : f1}
erruptCliBIP = {}
erruptCliBIP = {'img' : img4, 'geo' : {'x' : 150.0,'y' : 500.0,'h' : 90.0,'w' : 120.0}, 'func' : f2}
sacrificetext = {}
sacrificetext = {'img' : img6, 'geo' : {'x' : 250.0,'y' : 500.0,'h' : 100.0,'w' : 500.0}, 'func' : f3}
sacrificetoaster = {}
sacrificetoaster = {'img' : img7, 'geo' : {'x' : 200.0,'y' : 400.0,'h' : 100.0,'w' : 100.0}, 'func' : f4}
sacrifCliBIP = {}
sacrifCliBIP = {'img' : img16, 'geo' : {'x' : 750.0,'y' : 400.0,'h' : 90.0,'w' : 120.0}, 'func' : f11}
sacrifLave = {}
sacrifLave = {'img' : img17, 'geo' : {'x' : 200.0,'y' : 200.0,'h' : 250.0,'w' : 600.0}, 'func' : f12}
heureutext = {}
heureutext = {'img' : img18, 'geo' : {'x' : 250.0,'y' : 500.0,'h' : 100.0,'w' : 500.0}, 'func' : f13}
heureuCliBIP = {}
heureuCliBIP = {'img' : img2, 'geo' : {'x' : 150.0,'y' : 500.0,'h' : 90.0,'w' : 120.0}, 'func' : f14}
sacrif = {}
sacrif = {'bg' : img11, 'cli' : [sacrifCliBIP]}
errupt = {}
errupt = {'bg' : img3, 'cli' : [erruptCliBIP]}
fin = {}
fin = {'bg' : img19, 'cli' : [heureuCliBIP, heureutext]}
currentScene = errupt

def printScene():
    global t1, tsum
    t2 = time.time()
    tsum += t2 - t1
    t1 = t2
    if tsum >= 1/30.0:
        tsum = 0
        window.blit(currentScene['bg'],(0,0))
        for i in range(0,len(currentScene['cli'])):
            window.blit(currentScene['cli'][i]['img'],(currentScene['cli'][i]['geo']['x'],currentScene['cli'][i]['geo']['y']))
        pygame.display.flip()
if __name__ == "__main__":
    pygame.init() 
    window = pygame.display.set_mode((screen_x, screen_y))
    pygame.display.set_caption('Point & Click')
    screen = pygame.display.get_surface()
    font = pygame.font.Font(None,30)
    while True:
        printScene()
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit(0)
            elif event.type == MOUSEBUTTONDOWN:
                (mX,mY) = pygame.mouse.get_pos()
                isNotClicked = True
                for i in range(0,len(currentScene['cli'])):
                    if(isNotClicked):
                        if(mX > currentScene['cli'][i]['geo']['x'] and mY > currentScene['cli'][i]['geo']['y'] and mX < currentScene['cli'][i]['geo']['w'] + currentScene['cli'][i]['geo']['x'] and mY < currentScene['cli'][i]['geo']['h'] + currentScene['cli'][i]['geo']['y']):
                            currentScene['cli'][i]['func']()
                            isNotClicked = False