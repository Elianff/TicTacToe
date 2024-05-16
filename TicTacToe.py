#import modules
import pygame
from pygame.locals import *

pygame.init()


SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = pygame.display.set_mode((SCREEN_HEIGHT,SCREEN_WIDTH))
pygame.display.set_caption("TicTacToe")


#define variables
LINE_WIDTH=7
MARKERS=[]
clicked=False
pos=[]
player=1
winner = 0
game_over=False



#define colors
green = (0,255,0)
red = (255,0,0)
blue = (0,0,255)

#define font
font = pygame.font.SysFont(None,40)

#create play again rectangle
again_rect= Rect(SCREEN_WIDTH//2-80,SCREEN_HEIGHT//2,160,50)
def draw_grid():
    background=(255,255,200)
    grid=(50,50,50)
    screen.fill(background)
    for x in range(1,3):
        pygame.draw.line(screen,grid,(0,x*100),(SCREEN_WIDTH,x*100),LINE_WIDTH)
        pygame.draw.line(screen,grid,(x*100,0),(x*100,SCREEN_HEIGHT),LINE_WIDTH)



for x in range(3):
    row = [0,0,0] #or: [0]*3
    MARKERS.append(row)


def draw_markers():
    x_pos = 0
    for x in MARKERS:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen,green, (x_pos * 100+15,y_pos*100+15),(x_pos*100+85,y_pos*100+85),LINE_WIDTH)
                pygame.draw.line(screen,green, (x_pos * 100+15,y_pos*100+85),(x_pos*100+85,y_pos*100+15),LINE_WIDTH)
            if y == -1:
                pygame.draw.circle(screen,red,(x_pos*100+50,y_pos*100+50),38,LINE_WIDTH)
            y_pos += 1
        x_pos+=1


def check_winner():

    global winner
    global game_over
    y_pos = 0
    for x in MARKERS:
        #check columns
        if sum(x) ==3 :
            winner = 1
            game_over = True
        if sum(x)== -3:
            winner=2
            game_over = True
        #check rows
        if MARKERS[0][y_pos] + MARKERS[1][y_pos]+MARKERS[2][y_pos] == 3:
            winner = 1
            game_over = True
        if MARKERS[0][y_pos] + MARKERS[1][y_pos]+MARKERS[2][y_pos] == -3:
            winner = 2
            game_over = True
        y_pos += 1

    #check cross
    if MARKERS[0][0]+MARKERS[1][1]+MARKERS[2][2] == 3 or MARKERS[2][2]+MARKERS[1][1]+MARKERS[0][0] == -3:
        winner = 1
        game_over = True
    if MARKERS[0][0]+MARKERS[1][1]+MARKERS[2][2] == -3 or MARKERS[2][2]+MARKERS[1][1]+MARKERS[0][0] == 3:
        winner = 2
        game_over = True





def draw_winner(winner):
    win_text = "Player "+str(winner) + " wins!"
    win_img = font.render(win_text,True,blue)
    pygame.draw.rect(screen,green,(SCREEN_WIDTH//2-100,SCREEN_HEIGHT//2-60,200,50))
    screen.blit(win_img, (SCREEN_WIDTH//2-100,SCREEN_HEIGHT //2-50))

    again_text = "Play Again?"
    again_img = font.render(again_text,True,blue)
    pygame.draw.rect(screen,green,again_rect)
    screen.blit(again_img, (SCREEN_WIDTH//2-80,SCREEN_HEIGHT//2+10))
    


run=True
while run:

    draw_grid()
    draw_markers()

    #add event handlers
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run = False
        if game_over == 0:
            if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
                clicked = True
            if event.type==pygame.MOUSEBUTTONUP and clicked== True:
                clicked = False
                pos = pygame.mouse.get_pos()
                cell_x = pos[0]
                cell_y = pos[1]
                if MARKERS[cell_x//100][cell_y//100]==0:
                    MARKERS[cell_x//100][cell_y//100] = player
                    player *= -1
                    check_winner()




    if game_over == True:
        draw_winner(winner)
        #check for mouseclick to see if user has clicked on Play Again
        if event.type==pygame.MOUSEBUTTONDOWN and clicked==False:
            clicked = True
        if event.type==pygame.MOUSEBUTTONUP and clicked== True:
            clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                #reset variables
                MARKERS=[]
                pos=[]
                player=1
                winner = 0
                game_over=False
                for x in range(3):
                    row = [0,0,0] #or: [0]*3
                    MARKERS.append(row)


    pygame.display.update()


pygame.quit()

