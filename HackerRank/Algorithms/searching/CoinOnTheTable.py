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
    if returnTuple:
        return (x,y)
    else: return x + y
#############################################################################################################################
def tryThisBoard(coin,cols):
    loc = cols[ coin[0] ][ coin[1] ]
    for step in range(time):
        coin = moveCoin(coin,cols)
    if coin != None:
        newloc = cols[ coin[0] ][ coin[1] ]
    else: newloc = None
    #print("newloc=",newloc)
    if newloc == '*':
        return True
    else:
        return False
#############################################################################################################################
def find_path(g, start, end):
    distances={}
    order={}
    for i in g.keys():
        if i == start: distances[i] = 0
        else: distances[i] = float("inf")
    from copy import copy
    drop1 = copy(distances)
    while len(drop1) > 0:
        minNode = min(drop1, key = drop1.get)
        for i in g[minNode]:
            keyz = list(i)[0]
            dist = i[keyz]
            if distances[keyz] > (distances[minNode] + dist):
                distances[keyz] = distances[minNode] + dist
                drop1[keyz] = distances[minNode] + dist
                order[keyz] = minNode
        del drop1[minNode]
    temp = copy(end)
    rpath = []
    path = []
    while 1:
        rpath.append(temp)
        if temp in order: temp = order[temp]
        else: return -1
        if temp == start:
            rpath.append(temp)
            break
    for j in range(len(rpath)-1,-1,-1):
        path.append(rpath[j])
    return path
#############################################################################################################################
def buildGraph(cols,i):
    g={}
    for r in range(len(cols)):                  #for each row
        for c in range( len(cols[r] )) :        #for each column
            square=cols[r][c]                   #
            name = (r,c)
            g[name] = None
            if square == '*':
                g[name] = []
                pass
            else:
                if r > 0:   #if theres a path upward
                    if square == 'U':
                        distance = 1
                    else: distance = i
                    dest = (r-1,c)
                    edge = { dest:distance }
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
                                
                if c < len(cols[r])-1:   #if there's a path to the right
                    if square == 'R':
                        distance = 1
                    else: distance = i
                    dest=(r,c+1)
                    edge = { dest:distance }
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
            
                if r < len(cols)-1:   #if theres a path down
                    if square == 'D':
                        distance = 1
                    else : distance = i
                    dest=(r+1,c)
                    edge = { dest:distance }
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
                
                if c > 0: #if theres a path to the left
                    if square == 'L':
                        distance = 1
                    else: distance = i
                    dest = (r, c-1)
                    edge = { dest:distance }
                    if g[name] == None:
                        g[name] = [edge]
                    else: g[name] += [edge]     #else if it does already exist, concat the new dest.
    return g


cols = []
numRows, numCols, time = [int(x) for x in input().split()]

for i in range(numRows):
    cols.append(input())

coin = (0,0)
star = findStar(cols)
minMoves = calcNumMoves(coin,star,cols)
answer=[]

if minMoves <= time:    #if it can be done...
    if tryThisBoard(coin,cols) == False:    #can it be done with the current board?
        # if not, build the graph

        for i in [2,10,100]:
            g=buildGraph(cols,i)
            ans=0
            path=find_path(g,coin,star)                 	#get the optimal path

            if len(path) <= time+1:                           #assuming its not too long...
                for node in range(len(path)-1):             #for each step in our optimal path
                    x,y = path[node]                        #get the movement made
                    nextx,nexty = path[node+1]              #and the expected movement
                    movementCalledFor = cols[x][y]
                    deltax = x - nextx
                    deltay = y - nexty
                    if deltax == 0 and deltay < 0:          #if change in x is zero, and change in y is negative, we moved right (50%?)
                        movementMade = 'R'
                    elif deltay == 0 and deltax < 0:        #if change in y is zero, and change in x is negative, we moved down  (50%)
                        movementMade = 'D'
                    elif deltax == 0 and deltay > 0:        #if change in x is zero, and change in y is positive, we moved left 
                        movementMade = 'L'
                    elif deltay == 0 and deltax > 0:        #if chagne in y is zero, and change in x is positive, we moved up
                        movementMade = 'U'
            
                    else:raise Exception                    #otherwise, something funky happened, so exit with an error
            
                    if movementMade != movementCalledFor:   #and compare them...if there's been a change...
                        ans += 1
                #print (ans)
                answer.append(ans)
        print(min(answer))
    else:                                           #if tryThisBoard() is TRUE
        print("0")                                  #nothing needs to be done
else: print ("-1")                                  #if its impossible to solve this puzzle in the given time...