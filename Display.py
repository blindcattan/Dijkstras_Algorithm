import pygame
import sys
import map as m
import math
from pygame.locals import *

list_of_mNodes = []
list_of_dNodes = []


#Line States

startPos = (0,0)

#Naming for Test
Node_Name = 65
the_Node_selected = ""
Node_selected =False

#Highway options

# multipliers


# text


lines = []
def calcCenter (startX,startY,endX,endY):
    centerX =  ((startX + endX) / 2)
    centerY =  ((startY + endY) / 2)
    return (centerX,centerY)


def calcDistance(startX,startY,endX,endY):
    distance = math.sqrt((startX - endX)**2 + (startY - endY)**2)
    #print (distance)
    return distance

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
        top = A.y - A.Height
        bottom = A.y + A.Height
        left = A.x - A.Height
        right = A.x + A.Height

        #print("Top ", top, " Bottom: ", bottom, " left", left, " right: ", right, "   Mouse x, y",x," ", y)
        if y > top and y < bottom and x > left and x < right:
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
    ScreenWidth = 900



    pygame.init()
    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    Dmyfont = pygame.font.SysFont('Comic Sans MS', 18)

    window = pygame.display.set_mode((ScreenWidth, ScreenHeight))
    pygame.display.set_caption("Dijkstras Algorithm")
    run = True

    lineStart = None
    drawing = False
    # Display loop
    while run:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                MouseXY = pygame.mouse.get_pos()
                print(MouseXY)
                if event.button == 1:
                    collided = False
                    for d in list_of_dNodes:
                        #Not clicked on anything yet, But managed to click on something
                        global startPos
                        if d.hasCollided(MouseXY[0], MouseXY[1]):
                            collided = True
                            print("Collided", d.displayName)
                    if collided is False:
                        create_a_node(MouseXY[0], MouseXY[1])
                    collided = False
                if event.button == 3:

                    tempNode = None

                    for d in list_of_dNodes:
                        #Not clicked on anything yet, But managed to click on something
                        global startPos
                        if d.hasCollided(MouseXY[0], MouseXY[1]):
                            tempNode = d
                            print("Collided", d.displayName)

                    # Not collided

                    if tempNode == None:
                        if lineStart != None: # cancel
                            lineStart = None
                            drawing = False
                    else: # fun stuff
                        if lineStart == None: # Start line
                            lineStart = tempNode
                            print("started at , ", tempNode )
                            drawing = True
                            startPos = pygame.mouse.get_pos()
                        else:

                            distance = calcDistance(lineStart.x,lineStart.y,tempNode.x,tempNode.y)
                            lines.append((lineStart, tempNode,distance))
                            m.add_route(lineStart.mNode,tempNode.mNode,distance)
                            m.add_route(tempNode.mNode, lineStart.mNode, distance)
                            drawing = False
                            lineStart = None
            if event.type == KEYDOWN:
                MouseXY = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()
                if keys[K_s]:
                    for d in list_of_dNodes:
                        #Not clicked on anything yet, But managed to click on something
                        if d.hasCollided(MouseXY[0], MouseXY[1]):
                            tempNode = d
                            print("Collided", d.displayName)
                    beginningnode = tempNode
                if keys[K_e]:
                    for d in list_of_dNodes:
                        # Not clicked on anything yet, But managed to click on something
                        if d.hasCollided(MouseXY[0], MouseXY[1]):
                            tempNode = d
                            print("Collided", d.displayName)
                    finishNode = tempNode
                    print("ended")
                                        # End
                if keys[K_RETURN]:
                    # go
                    print (beginningnode.mNode, " : ",  finishNode.mNode)
                    m.Start_Dijkstras(beginningnode.mNode, finishNode.mNode, list_of_mNodes)
                    print("Go find a route")



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
            #print ("hi", l)
            startX = l[0].x
            startY = l[0].y

            endX = l[1].x
            endY= l[1].y

            theDistance = l[2]

            pygame.draw.line(window, (0, 0, 255),(startX, startY),(endX, endY),3 )
            textsurface = Dmyfont.render(str(theDistance), False, (255, 255, 255))
            midCoords=  calcCenter(startX,startY,endX,endY)
            window.blit(textsurface, midCoords)

        if drawing == True:
            MouseXY = pygame.mouse.get_pos()
            pygame.draw.line(window,(255,255,255),(startPos[0],startPos[1]),(MouseXY[0],MouseXY[1]),3)

        pygame.display.update()
    pygame.quit()