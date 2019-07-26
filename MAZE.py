import pygame
import time
import random
import os

# maze node's class 
class Node:
    def __init__(self,x,y,n):
        self.x = x
        self.y = y
        self.Neighbours = n
        self.connected = []
        self.visited = False
        
# objects sizes
WIDTH = 40
HEIGHT = 25
NODE_SIZE = 20
BORDER = 5

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (50,50)

#pygame initialization
pygame.init()
win = pygame.display.set_mode(
    (WIDTH * (NODE_SIZE + BORDER) + BORDER, HEIGHT * (NODE_SIZE + BORDER) + BORDER) )
pygame.display.set_caption("Maze")
win.fill((0, 0, 0))
pygame.display.update()

random.seed()


Nodes = []

# create nodes
for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        n = []
        if x - 1 >= 0:
            n.append(x - 1 + y * WIDTH)
        if x + 1 < WIDTH:
            n.append(x + 1 + y * WIDTH)
        if y - 1 >= 0:
            n.append(x + (y-1)*WIDTH)
        if y + 1 <HEIGHT:
            n.append(x + (y+1)*WIDTH)

        Nodes.append(Node(x,y,n))


def Draw_Board(current=None):
    
    win.fill((0, 0, 0))

    # draw all nodes
    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):

            #different drawing for current node while creating the maze 
            if current:
                if (x + y * WIDTH) == current:
                    pygame.draw.rect(
                        win, (0, 4, 255), (Nodes[x + y * WIDTH].x*(NODE_SIZE+BORDER) + BORDER, Nodes[x + y * WIDTH].y*(NODE_SIZE+BORDER) + BORDER, NODE_SIZE, NODE_SIZE))
                    continue

            #basic drawing
            pygame.draw.rect(
                win, (255, 255, 255), (Nodes[x + y * WIDTH].x*(NODE_SIZE+BORDER) + BORDER, Nodes[x + y * WIDTH].y*(NODE_SIZE+BORDER) + BORDER, NODE_SIZE, NODE_SIZE))

            # draw connection with right node
            if (x+1 + y*WIDTH) in Nodes[x + y * WIDTH].connected:
                pygame.draw.rect(
                    win, (255, 255, 255), (Nodes[x + y * WIDTH].x*(NODE_SIZE+BORDER) + BORDER + NODE_SIZE, Nodes[x + y * WIDTH].y*(NODE_SIZE+BORDER) + BORDER, BORDER, NODE_SIZE))
            
            # draw connection with lower node
            if (x + (y+1)*WIDTH) in Nodes[x + y * WIDTH].connected:
                pygame.draw.rect(
                    win, (255, 255, 255), (Nodes[x + y * WIDTH].x*(NODE_SIZE+BORDER) + BORDER, Nodes[x + y * WIDTH].y*(NODE_SIZE+BORDER) + BORDER + NODE_SIZE, NODE_SIZE, BORDER))

            
    pygame.display.update()


def Make_Maze(Nodes = Nodes):
    # we need to create empty stack
    stack = []

    # algorithm starts in left-upper corner
    stack.append(0)

    while len(stack) > 0:
        # draw actuall

        Draw_Board(stack[-1])

        # if node's neighbours are visited we have to go back
        print(Nodes[stack[-1]].Neighbours," : ",stack[-1])
        if len(Nodes[stack[-1]].Neighbours) == list(Nodes[i].visited for i in Nodes[stack[-1]].Neighbours).count(True):
            Nodes[stack[-1]].visited = True
            stack.pop(-1)
            continue
        
        # picking random not visited neighbour
        _random = random.choice(Nodes[stack[-1]].Neighbours)

        while Nodes[_random].visited:
            _random = random.choice(Nodes[stack[-1]].Neighbours)
        
        # setting conenction between two nodes
        Nodes[_random].connected.append(stack[-1])
        Nodes[stack[-1]].connected.append(_random)

        Nodes[stack[-1]].visited = True

        stack.append(_random)

    return True
        

        


run = True
Make_Maze()

while run:

    Draw_Board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


