# Dijikstas_Algotithm_py
A very basic and very poorly coded version of the Dijikstas_Algotithm in Python. Inspired by the example of Dijkstra's Algorithm in Computerphile Youtube episode. https://youtu.be/GazC3A4OQTE 

The Map contains an example Map but you could create your own if you want to replace it. Just make sure to import map at the start of your program

If you want to make your own map you first create your nodes this is done by

Node1 = map.node("Nodes String Name")
Node2 = map.node("can be anything")
Node3 = map.node("you want it to be")
Node4 = map.node("basically just a ")
Node5= map.node("test representation")
Node6= map.node("of where you node is ")
Node7= map.node("like monkey puzzle roundabout")

Then you need to all the routes between the nodes

then stick all those values into list
list_of_nodes = [Node1, Node2, Node 3,...]

then add all the routes between each one. Happy Days.
Note that for a two way street you add both the start and the end and the weight value

map.add_route(Node1,Node2 , 1)
map.add_route(Node1,Node3 , 2)
map.add_route(Node1,Node4 , 3)

map.add_route(Node2,Node1 , 1)
map.add_route(Node2,Node3 , 3)

map.add_route(Node3,Node1 , 3)
map.add_route(Node3,Node2 , 3)
map.add_route(Node3,Node4 , 5)
map.add_route(Node3,Node5 , 3)

map.add_route(Node4,Node2 , 3)
map.add_route(Node4,Node2 , 5)

map.add_route(Node5,Node3 , 3

The above is just an example the 3rd paramater is the weight of ho long it takes to get to and  from a point. 

And then to get the whole thing going simply type
map.Start_Dijkstras(a,l,list_of_nodes)

Then Bob's your dad's Brother you'll get a result


There are a few place that I plan to improve upon.
I'd like to tidy the code up to have most parts in individual definitions

There is a massive fudge I have in the Instance Variables where I set the Via value as none and then later assign a Card to. This is because I cant pass and Empty Instance Variable into itself, I've not worked out why. I think its because it creates itself which creates something that creates something ......
that eventually poops its self so I give a none value. This stops me using a better weight method than the one at the end and it looks like a piece of 

THe Next real plan is to create a Pygame interface to automate the creation of routes.

Few notes the weight is actually a float which means this could have a lot of application

Ive also included an alternative method to using a pycharm module too give a visual display to set things up


