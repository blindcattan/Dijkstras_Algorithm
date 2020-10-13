import map
import Display

# list of all nodes


s = map.node("S")
a = map.node("A")
c = map.node("C")
d = map.node("D")
b = map.node("B")
l = map.node("L")
i = map.node("I")
j = map.node("J")
k = map.node("K")
e = map.node("E")
g = map.node("G")
h = map.node("H")
f = map.node("F")

list_of_nodes = [s, a, c, d, b, l, i, j, k, e, g, h, f]

map.add_route(s,a, 7)
map.add_route(s,c, 3)
map.add_route(s,b, 2)

map.add_route(a,d, 4)
map.add_route(a,b, 3)
map.add_route(a,s, 7)

map.add_route(c,s, 3)
map.add_route(c,l, 2)

map.add_route(d,b, 4)
map.add_route(d,a, 4)
map.add_route(d,f, 5)

map.add_route(b,s, 2)
map.add_route(b,a, 3)
map.add_route(b,d, 4)
map.add_route(b,h, 1)

map.add_route(l,c, 2)
map.add_route(l,i, 4)
map.add_route(l,j, 4)

map.add_route(i,l,4)
map.add_route(i,j,6)
map.add_route(i,k,4)

map.add_route(j,l,4)
map.add_route(j,i,6)
map.add_route(j,k,4)

map.add_route(e,k,5)
map.add_route(e,g,2)

map.add_route(f,h,3)
map.add_route(f,d,5)

map.add_route(h,b,1)
map.add_route(h,f,3)
map.add_route(h,g,2)

map.add_route(g,e,2)
map.add_route(g,h,2)

map.add_route(k,e,5)
map.add_route(k,i,4)
map.add_route(k,j,4)






#print ("hi", s.Neighbours)
#test = s.getNeighbours()
#for i in test:
#    print (i.End.ID)

#map.Start_Dijkstras(d,k,list_of_nodes)

Display.display()
#print ("test area", e.getNeighbours())


#print(map.getRouteWeight(s,c))

words = "A"
Node_Name = 64
ascii = []
char = ord(words[0])-1
print(chr(char))

