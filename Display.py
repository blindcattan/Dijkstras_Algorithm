#modified 8th November added new features set to change colour of dNode
#finished modifications 15th november to clear bugs in last feature set. also fix issues from starting the program erroneously. still have a bug where code says that the route has not completed even though it has
#added funtionaity to follow a route visually
#added  Functionality for a speed options 
import pygame

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
routeLines = []


def displayRoute(theroute):

    for x in range(len(theroute)):
        if x < len(theroute) -1:
            current_Node = theroute[x].theCardNode
            nextNode = theroute[x + 1].theCardNode
            # print("The Current Node is ", current_Node.getID(), " The Next Node is ", prev_Node.getID())
        else:
            # first node
            current_Node = theroute[x].theCardNode


        routeLines.append((current_Node,nextNode))

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
    #  colour = (255,0,0)  colour can now change

    def __init__(self,x,y,mNode,displayName):
        self.x = x
        self.y = y
        self.mNode = mNode
        self.displayName = displayName
        self.colour = (128,128,128) # set the default colour is grey
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

    def setBlue(self):
        self.colour = (0,128,255)

    def setGreen(self):
        self.colour = (128,255,0) # I know its not super green but I like this colour better

    def setRed(self):
        self.colour = (204,0,0)

    def setYellow(self):
        self.colour = (255,255,51)

    def setMagenta(self):
        self.colour = (255,0,127)


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

ScreenHeight = 500
ScreenWidth = 900

hOption1 = (ScreenWidth - 20, ScreenHeight - 120)
hOPtColour1 = (255, 255, 255)
hOption2 = (ScreenWidth - 20, ScreenHeight - 80)
hOPtColour2 = (0, 0, 255)
hOption3 = (ScreenWidth - 20, ScreenHeight - 40)
hOPtColour3 = (255, 255, 255)
multiplier = 1

#beginningnode = None
#finishNode = None

def caughtOptionOne(x,y):
    #quite possibly the second worst way of doing this but hey its late you gonna do its late
    top = hOption1[1] - 16
    bottom = hOption1[1] + 16
    left = hOption1[0] - 16
    right = hOption1[0] + 16
    # print("Top ", top, " Bottom: ", bottom, " left", left, " right: ", right, "   Mouse x, y",x," ", y)
    if y > top and y < bottom and x > left and x < right:
        return True
    else:
        return False
def caughtOptionTwo(x,y):
    #quite possibly the second worst way of doing this but hey its late you gonna do its late
    top = hOption2[1] - 16
    bottom = hOption2[1] + 16
    left = hOption2[0] - 16
    right = hOption2[0] + 16
    # print("Top ", top, " Bottom: ", bottom, " left", left, " right: ", right, "   Mouse x, y",x," ", y)
    if y > top and y < bottom and x > left and x < right:
        return True
    else:
        return False
def caughtOptionThree(x,y):
    #quite possibly the second worst way of doing this but hey its late you gonna do its late
    top = hOption3[1] - 16
    bottom = hOption3[1] + 16
    left = hOption3[0] - 16
    right = hOption3[0] + 16
    # print("Top ", top, " Bottom: ", bottom, " left", left, " right: ", right, "   Mouse x, y",x," ", y)
    if y > top and y < bottom and x > left and x < right:
        return True
    else:
        return False


def display():
    drawing = False
    beginningnode = None
    finishNode = None

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

    #globals
    global hOPtColour1
    global hOPtColour2
    global hOPtColour3
    global hOption1
    global hOption2
    global hOption3
    global multiplier
    while run:


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == MOUSEBUTTONDOWN:
                MouseXY = pygame.mouse.get_pos()
                print(MouseXY)
                if event.button == 1:
                    if caughtOptionOne(MouseXY[0], MouseXY[1]):
                        print ("heyo1")
                        hOPtColour1 = (0,0,255)
                        hOPtColour2 = (255, 255, 255)
                        hOPtColour3 = (255, 255, 255)
                        multiplier = 2
                    elif caughtOptionTwo(MouseXY[0], MouseXY[1]):
                        print("heyo2")
                        hOPtColour1 = (255,255,255)
                        hOPtColour2 = (0, 0, 255)
                        hOPtColour3 = (255, 255, 255)
                        multiplier = 1
                    elif caughtOptionThree(MouseXY[0],MouseXY[1]):
                        print("heyo3")
                        hOPtColour3 = (0, 0, 255)
                        hOPtColour2 = (255, 255, 255)
                        hOPtColour1 = (255, 255, 255)
                        multiplier = 0.5
                    else:
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
                            lines.append((lineStart, tempNode,distance * multiplier))
                            m.add_route(lineStart.mNode,tempNode.mNode,distance * multiplier)
                            m.add_route(tempNode.mNode, lineStart.mNode, distance * multiplier)
                            #sett the correct colour of the two points to dente that they are linked
                            lineStart.setMagenta()
                            tempNode.setMagenta()
                            drawing = False
                            lineStart = None
            if event.type == KEYDOWN:
                MouseXY = pygame.mouse.get_pos()
                keys = pygame.key.get_pressed()
                if keys[K_s]:
                    for d in list_of_dNodes:
                        #Not clicked on anything yet, But managed to click on something
                        if d.hasCollided(MouseXY[0], MouseXY[1]):
                            d.setBlue()
                            beginningnode = d
                if keys[K_e]:
                    for d in list_of_dNodes:
                        # Not clicked on anything yet, But managed to click on something
                        if d.hasCollided(MouseXY[0], MouseXY[1]):
                            tempNode = d
                            print("End: ", d.displayName)
                            tempNode.setRed()
                    finishNode = tempNode

                                        # End
                if keys[K_RETURN]:
                    # go
                    routeLines.clear()
                    if beginningnode == None or finishNode == None:
                        print("please select a start and a finish")
                    else:
                        print("Start: ", beginningnode.mNode, "end Node: ",finishNode.mNode  )
                        theRoute = m.Start_Dijkstras(beginningnode.mNode, finishNode.mNode, list_of_mNodes)

                        #added functionailty show the route if one is found
                        if theRoute == "ERROR":
                            print("Error Found")
                        else:
                            displayRoute(theRoute)



        window.fill((0, 0, 0))

        #Draw circles
        for s in list_of_dNodes:
            pygame.draw.circle(window,s.colour,(s.x,s.y),s.Height,5)
            pygame.draw.circle(window, (255,255,255), (s.x, s.y), s.Height-5, 15)
            textsurface = myfont.render(s.displayName, False, (0, 0, 0))
            window.blit(textsurface, (s.x-6, s.y-8))
            #pygame.draw.circle(window, s.colour, (s.x, s.y, s.width, s.Height))
            #print (len(list_of_mNodes))

        #draw GUI
        pygame.draw.circle(window, hOPtColour1, hOption1,15,20)
        pygame.draw.circle(window, hOPtColour2, hOption2,15,20)
        pygame.draw.circle(window, hOPtColour3, hOption3,15,20)

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

        for l in routeLines:


            #find the Start node for
            for d in list_of_dNodes:
                if d.mNode == l[0]:

                    startX = d.x
                    startY = d.y

            for d in list_of_dNodes:
                if d.mNode == l[1]:

                    endX = d.x
                    endY = d.y

            pygame.draw.line(window, (0, 255, 0),(startX, startY),(endX, endY),6 )

        if drawing == True:
            MouseXY = pygame.mouse.get_pos()
            pygame.draw.line(window,(255,255,255),(startPos[0],startPos[1]),(MouseXY[0],MouseXY[1]),3)

        pygame.display.update()
    pygame.quit()
