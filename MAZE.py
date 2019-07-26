import pygame

class Node:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.connected = [False]*4
        

WIDTH = 25
HEIGHT = 15
NODE_SIZE = 35
BORDER = 5

LEFT, TOP, RIGHT, DOWN = 0, 1, 2, 3

pygame.init()
win = pygame.display.set_mode(
    (WIDTH * (NODE_SIZE + BORDER) + BORDER, HEIGHT * (NODE_SIZE + BORDER) + BORDER))
pygame.display.set_caption("Maze")
win.fill((0, 0, 0))
pygame.display.update()

Nodes = []

for y in range(0, HEIGHT):
    for x in range(0, WIDTH):
        Nodes.append(Node(x*(NODE_SIZE+BORDER) + BORDER,y*(NODE_SIZE+BORDER)+BORDER))


def Draw_Board():

    for y in range(0, HEIGHT):
        for x in range(0, WIDTH):
            pygame.draw.rect(
                win, (255, 255, 255), (Nodes[x + y * WIDTH].x, Nodes[x + y * WIDTH].y, NODE_SIZE, NODE_SIZE))

            if Nodes[x + y * WIDTH].connected[RIGHT]:
                pygame.draw.rect(
                    win, (255, 255, 255), (Nodes[x + y * WIDTH].x + NODE_SIZE, Nodes[x + y * WIDTH].y, BORDER, NODE_SIZE))
            
            if Nodes[x + y * WIDTH].connected[DOWN]:
                pygame.draw.rect(
                    win, (255, 255, 255), (Nodes[x + y * WIDTH].x, Nodes[x + y * WIDTH].y + NODE_SIZE, NODE_SIZE, BORDER))

            
    pygame.display.update()

Nodes[0].connected[RIGHT]=True

def Make_Maze():
    stos = []



run = True

while run:

    Draw_Board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


