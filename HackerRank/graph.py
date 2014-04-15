##############################################################################################################################
##      Dennis Tracy Ivy, Jr.
##      04/4/2014
##      self study of MIT 6.00
##      ps11 - optimization, dynamic programming, graphs, etc
##############################################################################################################################

###############################################################################################################################
#  Customized class definitions for use in the ps11 problem set
##############################################################################################################################

class Node(object):                                                                     #creates a node
   def __init__(self, name):                                                            #initializer
       self.name = str(name)
   def getName(self):                                                                   #name getter
       return self.name
   def __str__(self):                                                                   #string version
       return self.name
   def __repr__(self):                                                                  #required for type
      return self.name
   def __eq__(self, other):                                                             #used for comparison
      return self.name == other.name                                    
   def __ne__(self, other):
      return not self.__eq__(other)                                                     #explicit comparison
#############################################################################################################################
class Edge(object):                                                                     #creates an edge
   def __init__(self, src, dest):                                                       #initializer
       self.src = src
       self.dest = dest
   def getSource(self):                                                                 #source getter
       return self.src
   def getDestination(self):                                                            #destination getter
       return self.dest
   def __str__(self):                                                                   #pretty string
       return str(self.src) + '->' + str(self.dest)
#############################################################################################################################
class WEdge(Edge):                                                                      #create a weighted edge object (extends Edge)
    def __init__(self, src, dest, distance, outdoor):
        
        self.src  = src                                                                 #initialize instance variables
        self.dest = dest
        self.distance = int(distance)
        self.outdoor  = int(outdoor)

    def getSource(self):                                                                #source getter
        return self.src
    def getDestination(self):                                                           #destination getter
        return self.dest    
    def getDistance(self):                                                              #total distance getter
        return int(self.distance)
    def getOutdoorDistance(self):                                                       #outdoor distance getter
        return int(self.outdoor)
    def __str__(self):                                                                  #create a pretty string to return
        return str(self.src.getName().rjust(2) ) + '->' + \
                str(self.dest.getName().ljust(2) ) + \
                ' distance=' + str(self.distance).rjust(3) + \
                ' outdoor=' + str(self.outdoor).rjust(3)
#############################################################################################################################
class Digraph(object):

   def __init__(self):                                                                  #initialize the graph
       self.nodes = []
       self.edges = {}
   def addNode(self, node):                                                             #add a node to the graph
       
       if node in self.nodes:                                                           #if it already exists.
           #print("Duplicate Node!")
           raise ValueError('Duplicate node')                                           #raise an error
       else:
           if type(node) != Node:                                                       #if its not the right type
                raise TypeError                                                         #raise an error
           self.nodes.append(node)                                                      #add it to the graph
           self.edges[str(node)] = []                                                   #create an empty list container to hold the nodes future edges

   def addEdge(self, edge):                                                             #add an edge to the graph
       src = edge.getSource()                                                           #find the source
       dest = edge.getDestination()                                                     #and the destination of the supplied edge
       if not(src in self.nodes and dest in self.nodes):                                #check to make sure they exist
           #print ("Node not in graph!")                                                #and if not throw an exception
           raise ValueError('Node not in graph')                                        
       self.edges[str(src)].append(edge)                                                #if they do exist, add them to the graph

   def childrenOf(self, node):                                                          #returns a list of children
       return self.edges[ str(node) ]                                                   #for the current node (returns a list of WEdge objects)

   def hasNode(self, node):                                                             #if this node exists in the graph
       if node in self.nodes:                                                           #find it
           return True                                                                  #and return either true
       else: return False                                                               #or false accordingly

   def calcPathLength(self, path, toPrint=False):                                       #calculates a numeric value of a path in format ['1','3','5']
        distances=[]                                                                    #locals
        outdoors=[]
        for i in range (0,len(path)-1):                                                 #for each leg of the journey
            d,o = self.distanceFromParentToChild(Node(path[i]),Node(path[i+1]))         #get the distance between each node
            distances.append(d)                                                         #and put them in an array
            outdoors.append(o)
        if toPrint==True:                                                               #if i want to display some debug info
            print (str(sum(distances)).rjust(3), "/", str(sum(outdoors)).ljust(3))
        return ( sum(distances), sum(outdoors) )                                        #return the sums in tuple format i.e. (120,75)

   def distanceFromParentToChild(self, src, dest):                                      #get the distance from one node to another node
        for i in self.edges[str(src)]:                                                  #check all possible pathways initiating from the source node
            if i.getDestination() == dest:                                              #if it exists
                return (i.getDistance(), i.getOutdoorDistance())                        #return a tuple containing the total and outdoor distances
        
   def __str__(self):                                                                   #convert this graph to a useful string
       res = ''                                                                         #empty str t return
       for k in sorted(self.edges):                                                     #for all the nodes
           for d in self.edges[k]:                                                      #for each edge
               res = res + str(d) + '\n'                                                #create a pretty string :P
       return res[:-1]                                                                  #slice off the last newline and return