import pygame
import time
from time import sleep
from pygame.locals import KEYDOWN, QUIT, MOUSEBUTTONDOWN, K_RETURN, K_ESCAPE
import sys
screen_x = 1000
screen_y = 700
t1 = 0
tsum = 0
img0 = pygame.image.load("Assets/usekey.png")
img1 = pygame.image.load("Assets/orange_scene1.png")
def f0():
    global move_right
    global position
    while(cli_move['geo']['x'] * move_right < position * move_right):
        cli_move['geo']['x'] = cli_move['geo']['x'] + 20.0 * move_right
        printScene()
        sleep(0.01)
    move_right = move_right * -1.0
    position = position + 500.0 * move_right


#functiondefs

move_right = 1.0
position = 700.0
cli_move = {}
cli_move = {'img' : img0, 'geo' : {'x' : 300.0,'y' : 250.0,'h' : 100.0,'w' : 100.0}, 'func' : f0}
sc_1 = {}
sc_1 = {'bg' : img1, 'cli' : [cli_move]}
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