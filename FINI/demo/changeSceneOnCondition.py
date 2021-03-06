import pygame
import time
from time import sleep
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE
import sys
screen_x = 1000
screen_y = 700
t1 = 0
tsum = 0
img0 = pygame.image.load("Assets/nothing.png")
img1 = pygame.image.load("Assets/gotosc2.png")
img2 = pygame.image.load("Assets/usekey.png")
img3 = pygame.image.load("Assets/orange_scene1.png")
img4 = pygame.image.load("Assets/orange_scene2.png")
def f0():
    global key_used
    print(None)

def f1():
    global key_used
    if(key_used > 0.0):
        global currentScene
        currentScene = sc_2

def f2():
    global key_used
    key_used = 1.0
    sc_1 = {}
    sc_1 = {'bg' : img3, 'cli' : [cli_switchScene]}
    global currentScene
    currentScene = sc_1


#functiondefs

key_used = 0.0
cli_empty = {}
cli_empty = {'img' : img0, 'geo' : {'x' : 1.0,'y' : 1.0,'h' : 1.0,'w' : 1.0}, 'func' : f0}
cli_switchScene = {}
cli_switchScene = {'img' : img1, 'geo' : {'x' : 600.0,'y' : 200.0,'h' : 300.0,'w' : 300.0}, 'func' : f1}
cli_key = {}
cli_key = {'img' : img2, 'geo' : {'x' : 300.0,'y' : 250.0,'h' : 100.0,'w' : 100.0}, 'func' : f2}
sc_1 = {}
sc_1 = {'bg' : img3, 'cli' : [cli_key, cli_switchScene]}
sc_2 = {}
sc_2 = {'bg' : img4, 'cli' : [cli_empty]}
currentScene = sc_1

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