##############################################################################################################################
#   object definitions
##############################################################################################################################

class Node(object):                                                                     #creates a node
   def __init__(self, name, value=None):                                                #initializer
       self.name = str(name)
       self.value = str(value)
   def getName(self):                                                                   #name getter
       return self.name
   def __str__(self):                                                                   #string version
       return self.name
   def __repr__(self):                                                                  #required for type
      return self.name
   def __eq__(self, other):                                                             #used for comparison
      return self.name == other.name                                    
   def __ne__(self, other):
      return not self.__eq__(other)                                                     

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
    def __init__(self, src, dest, distance):
        
        self.src  = src                                                                 #initialize instance variables
        self.dest = dest
        self.distance = int(distance)
        #self.direction  = direction

    def getSource(self):                                                                #source getter
        return self.src
    def getDestination(self):                                                           #destination getter
        return self.dest    
    def getDistance(self):                                                              #total distance getter
        return int(self.distance)
    #def getOutdoorDistance(self):                                                       #outdoor distance getter
     #   return int(self.outdoor)
    def __str__(self):                                                                  #create a pretty string to return
        return str(self.src.getName().rjust(6) ) + \
                   ' --' + str(self.distance).ljust(3) + '--> ' + \
                   str(self.dest.getName().ljust(6) )
                
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
   
   def updateValue(self,node,value):
       if node in self.nodes:
            self.nodes[self.nodes.index(node)].value = value
       else: raise Exception

   def getValue(self,node):
       if node in self.nodes:
           return self.nodes[self.nodes.index(node)].value
       else: raise Exception

   def calcPathLength(self, path, toPrint=False):                                       #calculates a numeric value of a path in format ['1','3','5']
        distances=[]                                                                    #locals
        for i in range (0,len(path)-1):                                                 #for each leg of the journey
            d = self.distanceFromParentToChild(Node(path[i]),Node(path[i+1]))           #get the distance between each node
            distances.append(d)                                                         #and put them in an array
        if toPrint==True:                                                               #if i want to display some debug info
            print ( str(sum(distances)).rjust(3) )
        return ( sum(distances) )                                                       #return the sum

   def distanceFromParentToChild(self, src, dest):                                      #get the distance from one node to another node
        for edge in self.edges[str(src)]:                                                  #check all possible pathways initiating from the source node
            if edge.getDestination() == dest:                                              #if it exists
                return (edge.getDistance())                                                #return a tuple containing the total and outdoor distances
        
   def __str__(self):                                                                   #convert this graph to a useful string
       res = ''                                                                         #empty str t return
       for k in sorted(self.edges):                                                     #for all the nodes
           for d in self.edges[k]:                                                      #for each edge
               res = res + str(d) + '\n'                                                #create a pretty string :P
       return res[:-1]                                                                  

#############################################################################################################################
#   declare helper functions
#############################################################################################################################

def findStar(cols):
    for c in range(len(cols)):
        for x in range(len(cols[c])):
            square = cols[c][x]
            if square == '*':
                return (c,x)

#############################################################################################################################

def moveCoin(coin,cols,getDirection=False):
    for c in range(len(cols)):
        for x in range(len(cols[c])):
            square = cols[c][x]
            if coin == (c,x):
                if getDirection == True: return square
                if square == '*':
                    print ("REACHED GOAL WITH TIME TO SPARE!")
                    return (c,x)
                if square == 'U':
                    if c > 1:
                        return (c-1,x)
                    else: return None
                elif square == 'L':
                    if x > 0:
                        return (c,x-1)
                    else: return None
                elif square == 'D':
                    if c < len(cols):
                        return (c+1,x)
                    else: return None
                elif square == 'R':
                    if x < len(cols[c]):
                        return (c,x+1)
                    else:return None

#############################################################################################################################

def calcNumMoves(coin,star,cols,returnTuple=False):
    x = abs( coin[0] - star[0] )
    y = abs( coin[1] - star[1] )
    #print("(x,y)=(",x,",",y,")")
    if returnTuple:
        return (x,y)
    else: return x + y

#############################################################################################################################

def tryThisBoard(coin,cols):
    loc = cols[ coin[0] ][ coin[1] ]
    for step in range(time):
        coin = moveCoin(coin,cols)
        #print("coin=",coin)
    newloc = cols[ coin[0] ][ coin[1] ]
    if newloc == '*':
        return True
    else:
        return False

#############################################################################################################################

def addThis(dest,g,srcNode,distance,square):
    destNode = Node(dest,square) #create a node
    if g.hasNode(destNode) == False: # if it doesn't already exist
        g.addNode(destNode) #add it
    wEdge = WEdge(srcNode,destNode,distance) #create a wedge
    g.addEdge(wEdge)

#############################################################################################################################
#   this is the workhorse function that does all the calculation...
#############################################################################################################################

def directedDFS(digraph, start, end, maxTotalDist=10**5, visited = None, memo = None, counter=0): #max total distance not really used for this application

    if visited == None : visited = []                                                   #initialize visited on our first trip thru
    if memo == None : memo = {}                                                         #initialize the memo
    start = Node(start)                                                                 #create nodes for the given values
    end = Node(end)
    if not (digraph.hasNode(start) and digraph.hasNode(end)):                           #and confirm that these nodes exist int he graph
        raise ValueError("Start or End does not exist")
    path = [str(start)]                                                                 #this is only EVER 1 node long???
    if start == end : return path                                                       #if we found it, start backtracking
    shortest = None                                                                     #initialize the shortest path
    bestDist = None                                                                     #initialize the best path val
  
    for node in digraph.childrenOf(start):                                              #for each child of the current node
        destination = node.getDestination()                                             #find out the destination
        if ( str(destination) not in visited ):                                         #check to see if we've been there before
            visited = visited + [str(destination)]                                      #if not, we plan to visit it now, so update the list
            try:
                newPath = memo[str(destination),str(end)]
            except:
                newPath = directedDFS (digraph,                                         #call the function with the same graph
                                       destination,                                     #using the current child node
                                       end,                                             #the same end
                                       maxTotalDist,                                    #same maxtotaldist
                                       visited,                                         #and the recently updated copy of the visited list
                                       memo,                                            #and the potentially new copy of memo.
                                       counter=counter+1)                               #and the incremented counter

            if newPath == None :                                                        #when we cant find a way thru, newPath will be none so...
                continue                                                                #try the next child by breaking out of the loop
                                                                                        #otherwise if we have SOME value for newPath, then we found a way thru
            potentialDist = digraph.calcPathLength(path + newPath)                      #if we did find a way thru  
            if potentialDist > maxTotalDist:                                            #check to see if it would be too long
                visited.remove(str(destination))                                        #if so we have to backtrack a little
                try:                                                                    #and remove any references to this node if they exist
                    del(memo[str(destination),str(end)])                                #in our visited and memo collections
                except:                                                                 #we use a try in case the item doesn't actually exist in memo
                    pass                                                                #if it doesn't exist, no harm done, just do nothing
                continue                                                                #break out of the loop and try the next child

            currentDist = digraph.calcPathLength(newPath)                               #if we made it thru AND it wasn't too big
            if  bestDist == None or currentDist < bestDist:                              #check to see if its our first time to get this far on this level, 
                shortest = newPath                                                      #OR if our currentPath is shorter than the best path found so far 
                bestDist = potentialDist                                                  #and if so, set shortest = newPath to signify that we found an initial way thru OR a shorter way thru
                memo[str(destination), str(end)] = shortest                             #and set the best Distance to the current Distance
                                                                                        #and update memo for dynamic programming application(speed)
                                                                                        #memo should be set to the string representation of the path we found...                
    if shortest != None:                                                                #when we've made it thru all the children,check to make sure we found something
        return path + shortest                                                          #and if so, add the current node shortest path to the existing path and return it
    else :                                                                              #if we didn't find a way thru for this level,
        if counter==0:                                                                  #if we didn't make it thru in TIME, we need to modify this graph somehow...
            raise ValueError                                                            #check to see if we never found a solution otherise return none 
            return None

#############################################################################################################################

#cols = []
#numRows, numCols, time = [int(x) for x in input().split()]
#for i in range(numRows):
#    cols.append(input())

numRows,numCols,time=2,2,1
cols=['RD','*L']

#numRows, numCols, time= 2, 2, 3
#cols=['RD','*L']

#numRows,numCols,time=3,3,4
#cols=['RDL',
#      'LDR',
#      'UL*']

answer=0
coin = (0,0)
star = findStar(cols)

if calcNumMoves(coin,star,cols) <= time: #if it can be done...
    if tryThisBoard(coin,cols) == False:    #can it be done with the current board?
        #build the graph
        g = Digraph()
        ans=0
        for r in range(len(cols)):
            for c in range( len(cols[r] )) :
                square=cols[r][c]
                src = (r,c)
                srcNode = Node(src, square)
                if g.hasNode( srcNode ) == False:
                    g.addNode( srcNode )
                else: 
                    g.updateValue(srcNode,square)

                if square != '*':
                    if r > 0:   #if theres a path upward
                        if square == 'U':
                            distance = 1
                        else: distance = 10
                        dest=(r-1,c)
                        addThis(dest,g,srcNode,distance,square)
                                
                    if c < len(cols[r])-1:   #if there's a path to the right
                        if square == 'R':
                            distance = 1
                        else: distance = 10
                        dest=(r,c+1)
                        addThis(dest,g,srcNode,distance,square)
            
                    if r < len(cols[r])-1:   #if theres a path down
                        if square == 'D':
                            distance = 1
                        else : distance = 10
                        dest=(r+1,c)
                        addThis(dest,g,srcNode,distance,square)
                
                    if c > 0: #if theres a path to the left
                        if square == 'L':
                            distance = 1
                        else: distance = 10
                        dest = (r, c-1)
                        addThis(dest,g,srcNode,distance,square)        
        
        path=directedDFS(g,coin,star)               #get the optimal path        
        for node in range(len(path)-1):             #for each step in our optimal path
            x,y = eval(path[node])                  #get the movement made
            nextx,nexty = eval(path[node+1])        #and the expected movement
            movementCalledFor = cols[x][y]
            deltax = x - nextx
            deltay = y - nexty
            if deltax == 0 and deltay < 0:          #if change in x is zero, and change in y is negative, we moved right (50%?)
                movementMade = 'R'
            elif deltay == 0 and deltax < 0:        #if change in y is zero, and change in x is negative, we moved down  (50%)
                movementMade = 'D'
            elif deltax == 0 and deltay > 0:        #if change in x is zero, and change in y is positive, we moved left  (SHOULD NEVER HAPPEN?)
                movementMade = 'L'
            elif deltay == 0 and deltax > 0:        #if chagne in y is zero, and change in x is positive, we moved up    (SHOULD NEVER HAPPEN?)
                movementMade = 'U'
            
            else:raise Exception                    #otherwise, something funky happened, so exit with an error
            
            if movementMade != movementCalledFor:   #and compare them...if there's been a change...
                ans += 1
        print (ans)

    else:                                           #if tryThisBoard() is TRUE
        print("0")                                  #nothing needs to be done
else: print ("-1")                                  #if its impossible to solve this puzzle in the given time...

