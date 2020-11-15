import operator

def getRouteWeight(start,End):
    theWeight= start.getWeight(End)
    return theWeight

def add_route(start, End, Weight):
    theroute = route(End, Weight)
    start.Neighbours.append(theroute)
    print ("route Added")
class node():
    def __init__(self,ID):
        self.ID = ID
        self.Neighbours = []
    def getID(self):
        return self.ID

    def __repr__(self):
        return 'node(ID=%s)' % (self.ID)

    def getWeight(self,destination):
        Weight = 0
        for N in self.Neighbours:
            if N.End == destination:
                Weight = N.Weight
        return Weight

    def getWeightbyID(self,destinationID):
        #print(destinationID)
        the_Weight = 0
        for N in self.Neighbours:
            #print ( "Neighbour", N.End.getID())
            if destinationID == N.End.getID():

                the_Weight = N.Weight
            return the_Weight
    def getNeighbours(self):
        return self.Neighbours


class route():
    def __init__(self,End,Weight):
        self.End = End
        self.Weight = Weight

    def __repr__(self):
        return 'route(End=%s, weight=%s)' % (self.End.getID(), self.Weight)

    def getEnd(self):
        return self.End

    def getWeight(self):
        return self.Weight

class card:

    def __repr__(self):
        return 'Card(Weight=%s, node=%s)' % (self.the_weight, self.theCardNode.getID())

    def __init__(self,theCardNode):
        self.theCardNode = theCardNode
        self.via = None
        self.the_weight = float('inf')

    def getWeight(self):
        return self.the_weight

    def getVia(self):
        return self.via

    def setWeight(self,weight):
        if self.the_weight > weight:
            self.the_weight = weight
            #print (self.theCardNode.getID(), ": I have Changed the Weight the weight is now ", self.the_weight)

    def getViaID(self):
        return self.theCardNode.getID()

def Start_Dijkstras(startNode, End_Node, list_of_Nodes):
    print (startNode, End_Node, list_of_Nodes)
    thestartnode = startNode
    EndNode = End_Node
    emptyNode = node("Blank")
    activeCards = []
    completedCards = []

    #create active cards
    for theNode in list_of_Nodes:
        #print(theNode.getID())
        theCard = card(theNode)
        activeCards.append(theCard)


    #for aCard in activeCards:
    #   print(aCard.theCardNode.ID)

    # find the card that repersents the start in the array
    for theCard in activeCards:
        if startNode == theCard.theCardNode:
            starCard = theCard

    #print("The Start Card is ", starCard.theCardNode.getID())
    theActiveCard =  starCard
    starCard.setWeight(0)
    #okay were ready to start
    Cardgotfound = False
    #print("the active Card =", theActiveCard.theCardNode.getID() )
    #print("the End Node = ",EndNode.getID())
    while theActiveCard.theCardNode.getID() != EndNode.getID():
        #print ("The active card is ", theActiveCard.theCardNode.getID(), "and the ENd Node is ", EndNode.getID())
        # get the list of _Neighbours
        list_of_Neighbours = theActiveCard.theCardNode.getNeighbours()


        for n in list_of_Neighbours:
            aNode = n.getEnd()

            #if any of the Neighbours is the end Node
            #print ("active Card is ", theActiveCard.theCardNode.getID(), "its Current Weight is ", theActiveCard.getWeight(), " Neighbour is ", aNode.getID(), " End Node is ", EndNode.getID())
            if aNode == EndNode:
                Cardgotfound = True
                print("card found")

            # find card that matches that aNode
            for  i in range(len(activeCards)):
                if activeCards[i].theCardNode == aNode:

                    #find the weight of that card
                    routeWeight = getRouteWeight(theActiveCard.theCardNode,activeCards[i].theCardNode)
                    activeCardWeight = theActiveCard.getWeight()
                    neightCardWeight = activeCards[i].getWeight()

                    #print("The Route Weight is : ", routeWeight, " The active Card Weight is :", activeCardWeight)
                    if activeCardWeight + routeWeight < neightCardWeight:
                        activeCards[i].setWeight(activeCardWeight + routeWeight)
                        activeCards[i].via = theActiveCard


        #put card in completed pile
        completedCards.append(theActiveCard)
        if len(activeCards) > 0:
            index = activeCards.index(theActiveCard)
            #print("popping : ", theActiveCard)
        activeCards.pop(index)
        #print("popping : ", theActiveCard.theCardNode.getID())
            #sort the cards
        activeCards.sort(key=operator.attrgetter('the_weight'))
        theActiveCard = activeCards[0]

        if theActiveCard.theCardNode.getID() == EndNode.getID():
            TheLastWayPoint = theActiveCard

    #
    #Leave the loop

    #if the card was found
    if Cardgotfound:
        print ("here at last we have found " ,TheLastWayPoint.theCardNode.getID(), " It is a weight of " , TheLastWayPoint.getWeight())

        # This is how we got here
        theroute = []

        while  TheLastWayPoint.theCardNode.getID() != starCard.theCardNode.getID():
            theroute.append(TheLastWayPoint)
            TheLastWayPoint = TheLastWayPoint.via
        theroute.append(TheLastWayPoint)

        #print(theroute)
        theroute.reverse()
        #print (theroute)
        #Traverse the root so that its Human readable


        for x in range(len(theroute)):
            if x  > 0:
                current_Node = theroute[x].theCardNode
                prev_Node = theroute[x-1].theCardNode
                #print("The Current Node is ", current_Node.getID(), " The Next Node is ", prev_Node.getID())
                distanceToNext = getRouteWeight(prev_Node,current_Node)
            else:
                # first node
                current_Node = theroute[x].theCardNode
                distanceToNext = 0

            print ("Make your way to " ,current_Node.getID(),  "it will take you ", distanceToNext)
    else:
        print ("we didnt get there")


