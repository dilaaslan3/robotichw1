from random import random, randint
import pygame, sys
from robot import Robot

"""" Define Tiles """
N = 0  # NOTHING
R1 = 1  # ROBOT1
R2 = 2  # ROBOT2
W = 3  # WALL
F = 4  # FOOD

"""" Define Tile Colors (RGB)"""
GRAY = (82, 82, 82)
PINK = (195, 131, 128)
BLUE = (46, 179, 201)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)

"""" Link Tile to Color """

TileColor = {
    N: GRAY,
    R1: PINK,
    R2: BLUE,
    W: BLACK,
    F: GREEN
}


""" Generate randomly position in the map """

r1 =Robot(randint(0,14), randint(0,14),"Robot 1")
r2 = Robot(randint(0,14), randint(0,14),"Robot 2")




"""" Create Map """

map = [[W, N, N, N, N, N, N, N, W, N, N, W, N, N, N],  # 15X15
       [N, W, N, N, N, W, N, N, N, W, N, N, N, N, N],
       [N, N, N, F, N, N, N, N, F, N, N, N, N, W, N],
       [N, N, W, N, N, W, F, N, W, N, N, N, N, N, F],
       [W, W, N, F, N, N, W, N, N, N, W, N, N, W, N],
       [N, N, N, N, W, N, N, W, N, W, N, N, F, N, N],
       [N, N, N, W, N, N, N, W, N, W, N, N, W, N, N],
       [W, N, W, N, N, W, N, N, N, W, N, N, W, N, W],
       [W, N, N, N, N, N, F, N, N, N, N, W, N, N, N],
       [N, N, N, W, N, N, N, N, W, N, F, N, N, N, N],
       [F, N, N, F, N, N, W, N, N, F, N, N, N, N, W],
       [N, W, N, N, W, N, N, F, N, N, W, N, N, W, N],
       [F, N, N, N, N, N, N, N, W, N, N, N, F, N, N],
       [N, W, N, F, W, F, N, N, N, N, W, F, N, W, W],
       [N, N, N, W, N, N, N, W, N, N, N, W, N, N, N]]




""" Creating Map-Size """

TILESIZE = 40
MAPWIDTH = 15
MAPHEIGHT = 15




""" Finding Food Cells"""

numFoodCells = 0
for row in range(MAPHEIGHT):
    for column in range(MAPWIDTH):
        if map[row][column] == F:
            numFoodCells += 1




""" Create Display """

pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH * TILESIZE, MAPHEIGHT * TILESIZE))


"""---------------------------------------------------------Methods-----------------------------------------------------"""



""" Eating Food """

def eat(robot):
    if map[robot.row][robot.column] == F:
        map[robot.row][robot.column] =N
        robot.score += 5
        print ("New Score of", robot.name ,"is: ",  robot.score)
        global numFoodCells
        numFoodCells -= 1



""" Algorithm of the robots """

def randomMove(robot):
    randomMoves= randint(5,8)
    if randomMoves == 5:
        up(robot)
    elif randomMoves == 6:
        down(robot)
    elif randomMoves == 7:
        right(robot)
    else:
        left(robot)


""" ROBOT MOVE """

def up(robot):
    if robot.row!=0 and map[robot.row-1][robot.column]!=W:
        robot.row -= 1


def down(robot):
    if  robot.row!=14 and map[robot.row+1][robot.column]!=W:
        robot.row += 1


def left(robot):
    if robot.column!=0 and map[robot.row][robot.column-1]!=W:
        robot.column -= 1


def right(robot):
    if robot.column!=14 and map[robot.row][robot.column+1]!=W:
        robot.column += 1


""" MAIN """


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

#when the food is all taken the simulation is ended.
    if numFoodCells == 0:
        pygame.quit()
        sys.exit()


    randomMove(r1)
    randomMove(r2)
    eat(r1)
    eat(r2)


    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            pygame.draw.rect(DISPLAY, TileColor[map[row][column]],
                             (column * TILESIZE, row * TILESIZE, TILESIZE, TILESIZE))

    pygame.draw.rect(DISPLAY, PINK, (r1.column * TILESIZE, r1.row * TILESIZE, TILESIZE, TILESIZE))
    pygame.draw.rect(DISPLAY, BLUE, (r2.column * TILESIZE, r2.row * TILESIZE, TILESIZE, TILESIZE))



    pygame.display.update()
