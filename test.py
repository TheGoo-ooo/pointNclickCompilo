import pygame
import time
from time import sleep
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE
import sys
screen_x = 1000
screen_y = 700
t1 = 0
tsum = 0
img0 = pygame.image.load("Assets/cli1_1.png")
img1 = pygame.image.load("Assets/cli1_2.PNG")
img2 = pygame.image.load("Assets/cli1_2.png")
img3 = pygame.image.load("Assets/bg1.png")
def f1():
    global currentScene
    currentScene = S2

def f0():
    S1C2['func'] = f1
    S1C1['img'] = img1
    while(S1['cli'][0]['geo']['x'] < 500.0):
        S1['cli'][0]['geo']['x'] = S1['cli'][0]['geo']['x'] + 5.0
        printScene()
        sleep(0.01)

def f2():
    print(None)

def f3():
    global currentScene
    currentScene = S1


#functiondefs

S1C1 = {}
S1C1 = {'img' : img0, 'geo' : {'x' : 100.0,'y' : 100.0,'h' : 500.0,'w' : 300.0}, 'func' : f0}
S1C2 = {}
S1C2 = {'img' : img2, 'geo' : {'x' : 400.0,'y' : 200.0,'h' : 500.0,'w' : 300.0}, 'func' : f2}
S2C2 = {}
S2C2 = {'img' : img2, 'geo' : {'x' : 100.0,'y' : 100.0,'h' : 500.0,'w' : 300.0}, 'func' : f3}
S1 = {}
S1 = {'bg' : img3, 'cli' : [S1C1, S1C2]}
S2 = {}
S2 = {'bg' : img3, 'cli' : [S2C2]}
currentScene = S1

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