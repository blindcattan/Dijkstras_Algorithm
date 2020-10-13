import pygame
import sys
import map as m
from pygame.locals import *

list_of_mNodes = []
list_of_dNodes = []


#Line States

startPos = (0,0)

#Naming for Test
Node_Name = 65
the_Node_selected = ""
Node_selected =False

lines = []

#char = ord(words[0])-1
#print(chr(char))

class dNode:
    width = 10
    Height = 20
    colour = (255,0,0)

    def __init__(self,x,y,mNode,displayName):
        self.x = x
        self.y = y
        self.mNode = mNode
        self.displayName = displayName

    def hasCollided(self, x,y):
        A = self

        if A.x + A.width > x and A.y + A.Height > y and x + 10 > x and y + 20 > y:
            return True
        else:
            return False


def create_a_node(x,y):
    global Node_Name
    name = chr(Node_Name)
    Node_Name = Node_Name +1
    New_Node = m.node(name)
    list_of_mNodes.append(New_Node)
    displayNode = dNode(x,y,New_Node,name)
    list_of_dNodes.append(displayNode)



CursorX = 0
CursorY = 0

list_of_Nodes = []

def display():
    drawing = False

    ScreenHeight = 700
    ScreenWidth = 700

    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
    pygame.display.set_caption("Second Game")
    run = True

    # Display loop
    while run:
        pygame.time.delay(50)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                MouseXY = pygame.mouse.get_pos()

                if event.button == 1:
                    create_a_node(MouseXY[0], MouseXY[1])
                if event.button == 3:
                    print("Drawing: ", drawing)
                    start_pos = MouseXY
                    for d in list_of_dNodes:
                        #Not clicked on anything yet, But managed to click on something
                        global startPos
                        if d.hasCollided(start_pos[0], start_pos[1]) and drawing == False:
                            global startNode
                            startNode = d
                            print("collided, now drawing")
                            drawing = True
                            startPos = start_pos
                        # Have already clicked on something, Looking to click on the end point
                        elif d.hasCollided(start_pos[0], start_pos[1]) and drawing == True:
                            print("collided stopped drawing")
                            drawing = False
                            lines.append((start_pos[0],start_pos[1], d.x, d.y))

                            #add route
                            m.add_route(startNode.mNode,d.mNode,1)

                            startNode = None

                        # these should cancel parts
                        elif d.hasCollided(start_pos[0], start_pos[1]) == False and drawing == True:
                            print ("not collided")
                            drawing == False

                            StartNode = None
                        elif d.hasCollided(start_pos[0], start_pos[1]) == False and drawing == False:
                            print("not collided")
                            drawing == False

                            StartNode = None



        keys = pygame.key.get_pressed()

        window.fill((0, 0, 0))

        #Draw circles
        for s in list_of_dNodes:
            pygame.draw.circle(window,s.colour,(s.x,s.y),s.Height,5)
            pygame.draw.circle(window, (255,255,255), (s.x, s.y), s.Height-5, 15)
            textsurface = myfont.render(s.displayName, False, (0, 0, 0))
            window.blit(textsurface, (s.x-6, s.y-8))
            #pygame.draw.circle(window, s.colour, (s.x, s.y, s.width, s.Height))
            #print (len(list_of_mNodes))

        # draw lines

        for l in lines:

            startX = l[0]
            startY = l[1]

            endX = l[2]
            endY= l[3]

            pygame.draw.line(window, (0, 0, 255),(startX, startY),(endX, endY),3 )

        if drawing == True:
            MouseXY = pygame.mouse.get_pos()
            pygame.draw.line(window,(255,255,255),(startPos[0],startPos[1]),(MouseXY[0],MouseXY[1]),3)

        pygame.display.update()
    pygame.quit()