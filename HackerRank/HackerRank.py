import sys
cols=[]
with open("coinsTest4.txt","r") as f:
    numRows,numCols,time = [int(x) for x in f.readline().split()]
    for line in range(numRows):
        cols.append(f.readline().strip())
for row in cols:
    print(row)

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
    print("coin=",coin)
    loc = cols[ coin[0] ][ coin[1] ]
    for step in range(time):
        coin = moveCoin(coin,cols)
    if coin != None:
        newloc = cols[ coin[0] ][ coin[1] ]
    else: newloc = None
    if newloc == '*':
        return True
    else:
        return False

#############################################################################################################################
def calcPath(g,nodes):
    distance=0
    for i in range(len(nodes)-1): #for each node...find the distance...(OR MAYBE FOR all but the LAST entry)
        #print("i=",i,"nodes[i]=",nodes[i])
        src = nodes[i]
        dest = nodes[i+1]
        #print("src=",src,"dest=",dest)
        #print("g[src]=",g[src])
        for x in g[src]: 
            #print("x=",x,"list(x)[0]=", list(x)[0])
            if list(x)[0] == dest:
                distance += x[ list(x)[0] ]
        #print("distance=",distance)     
    return distance
#############################################################################################################################
def find_path(g, start, end, time, visited = None, memo = None):
    if visited == None : visited = []                                                   #initialize visited on our first trip thru
    if memo == None : memo = {}                                                         #initialize the memo
    #try:
    #    g[start]
    #    g[end]
    #except:
    #    raise ValueError("Start or End does not exist")
    #input()
    path = [start]                                                                 #this is only EVER 1 node long???
    if start == end : 
        print("Found the End!")
        return path                                                       #if we found it, start backtracking
    shortest = None                                                                     #initialize the shortest path
    bestDist = None                                                                     #initialize the best path val
  
    for node in g[start]:                                                               #for each node
        destination = list(node)[0]
        distance = node[destination]
        #print ("node=",node,"start=",start,"destination=",destination,"distance=",distance,"visited=",visited,"memo=",memo )
        if destination not in visited:                                         #check to see if we've been there before
            visited = visited + [destination]                                      #if not, we plan to visit it now, so update the list
            try:
                #print("trying memo")
                newPath = memo[destination,end]
                print("saved time?")
            except:
                newPath = find_path(   g,                                         #call the function with the same graph
                                       destination,                                     #using the current child node
                                       end,                                             #the same end
                                       time,
                                       visited,                                         #and the recently updated copy of the visited list
                                       memo   )                               

            if newPath == None :                                                        #when we cant find a way thru, newPath will be none so...
                continue                                                                #try the next child by breaking out of the loop
            print("path + newPath=",path + newPath)                                                                            #otherwise if we have SOME value for newPath, then we found a way thru
            #input()
            #potentialDist = calcPath(g, path + newPath)                                  #if we did find a way thru  
            #if potentialDist >= time:                                            #check to see if it would be too long
            #    visited.remove(destination)                                        #if so we have to backtrack a little
            #    try:                                                                    #and remove any references to this node if they exist
            #        del(memo[destination,end])                                #in our visited and memo collections
            #    except:                                                                 #we use a try in case the item doesn't actually exist in memo
            #        pass                                                                #if it doesn't exist, no harm done, just do nothing
            #    continue                                                                #break out of the loop and try the next child

            #currentDist = calcPath(g, newPath)                               #if we made it thru AND it wasn't too big
            if  shortest == None or newPath < shortest:                              #check to see if its our first time to get this far on this level, 
                #if bestDist != None: print("Okay found a smaller case")
                #else: print("well...i found something")
                shortest = newPath                                                      #OR if our currentPath is shorter than the best path found so far 
                #bestDist = potentialDist                                                  #and if so, set shortest = newPath to signify that we found an initial way thru OR a shorter way thru
                print("start=",start,"destination=",destination)
                memo[start,destination] = path + newPath                             #and set the best Distance to the current Distance
                print("memo=",memo)
                                                                                        #and update memo for dynamic programming application(speed)
                                                                                        #memo should be set to the string representation of the path we found...                
    if shortest != None:                                                                #when we've made it thru all the children,check to make sure we found something
        return path + shortest                                                          #and if so, add the current node shortest path to the existing path and return it
    else :                                                                              #if we didn't find a way thru for this level,
        return None

#############################################################################################################################
#   this is the workhorse function that does all the calculation...
#############################################################################################################################

def buildGraph(cols):
    g={}
    for r in range(len(cols)):                  #for each row
        for c in range( len(cols[r] )) :        #for each column
            square=cols[r][c]                   #
            #print ("r=",r,"c=",c,"square=",square)
            name = (r,c)
            g[name] = None
            if square == '*':
                g[name] = []
                pass
            else:
                if r > 0:   #if theres a path upward
                    if square == 'U':
                        distance = 0
                    else: distance = 1
                    dest = (r-1,c)
                    edge = { dest:distance }
                    #if the destination node does not already exist, add it,
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
                                
                if c < len(cols[r])-1:   #if there's a path to the right
                    #print("c=",c)
                    if square == 'R':
                        distance = 0
                    else: distance = 1
                    dest=(r,c+1)
                    edge = { dest:distance }
                    #if the destination node does not already exist, add it,
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
            
                if r < len(cols)-1:   #if theres a path down
                    if square == 'D':
                        distance = 0
                    else : distance = 1
                    dest=(r+1,c)
                    edge = { dest:distance }
                    #if the destination node does not already exist, add it,
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
                
                if c > 0: #if theres a path to the left
                    if square == 'L':
                        distance = 0
                    else: distance = 1
                    dest = (r, c-1)
                    edge = { dest:distance }
                    #if the destination node does not already exist, add it,
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.

    #print("g=")
    #for i in g: 
    #    print(i, "=")
    #    if g[i] == None: print("********************")
    #    else:
    #        for x in g[i]:
    #            print ("  x=",x)            
    #input()
    return g

#get user input
#cols = []
#numRows, numCols, time = [int(x) for x in input().split()]

#for i in range(numRows):
#    cols.append(input())
#initializations...

coin = (0,0)
star = findStar(cols)

if calcNumMoves(coin,star,cols) <= time:    #if it can be done...
    if tryThisBoard(coin,cols) == False:    #can it be done with the current board?
        # if not, build the graph
        print ("numMoves=",calcNumMoves(coin,star,cols), "time=",time)
        print ("numRows=",numRows,"numCols=",numCols,"numRows*numCols=",numRows*numCols)
        print("star=",star)
        print("building graph")
        g=buildGraph(cols)
        print("len(g)=",len(g))
        numEdges = 0
        for node in g:
            if g[node] != None:
                numEdges += len(g[node])
        print("numEdges=",numEdges)
        ans=0       
        print("k...lets try and find the path")
                
        path=find_path(g,coin,star,time)               #get the optimal path

        print ("path=",path)
        input()

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

