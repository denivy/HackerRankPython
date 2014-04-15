import sys
from test import test_generators as tg
numRowsArray = []
numColsArray = []
row=[]
boards=[]
count=0
with open("queensOnBoard.txt") as f:
    numTests = int( f.readline() )
    assert 1 <= numTests <= 100
    for i in range(0,numTests):
        numRows, numCols = [ int(x) for x in f.readline().split() ]
        #print("numRows=",numRows,"numCols=",numCols)
        assert 1 <= numRows <=50
        assert 1 <= numCols <=5
        numRowsArray.append(numRows)
        numColsArray.append(numCols)
        board=[]
        for r in range(0,numRows): #for designated number of rows...            
            row = str(f.readline()).strip()
            row = list(row)
            #print ("row=",row)
            assert 1 <= len(row) <= numCols
            board.append(row)
        #print("board=",board)
        boards.append(board)
#print ("numTests=",numTests,"numRowsArray=",numRowsArray, "numColsArray=",numColsArray)
#print ("boards=", boards)

#numTests=int(input())
#assert 1 <= numTests <= 100
for _ in range(0,numTests):
    #########################################################
    ###Get input from user....
    ##numRows,numCols = [int(x) for x in input().split()]
    ##assert 1 <= numRows <=50
    ##assert 1 <= numCols <=5
    ##board=[]
    ##for r in range(0,numRows):
    ##    row=input().strip()
    ##    assert 1 <= len(row) <= numCols
    ##    row=list(row)
    ##    board.append(row)
    #########################################################
    ###Get input from file
    numRows=numRowsArray[_]
    numCols=numColsArray[_]
    board=boards[_]
    #print ("numRows=",numRows,"numCols=",numCols)
    #print ("board=")
    columns=[]
    diagonal=[]
    for row in board:
        print (row)
    BOARD_SIZE = numRows

class BailOut(Exception):
    print("bailed out!")
    pass

def validate(queens):
    left = right = col = queens[-1]
    for r in reversed(queens[:-1]):
        left, right = left-1, right+1
        if r in (left, col, right):
            raise BailOut

def add_queen(queens):
    for i in range(BOARD_SIZE):
        test_queens = queens + [i]
        try:
            validate(test_queens)
            if len(test_queens) == BOARD_SIZE:
                return test_queens
            else:
                return add_queen(test_queens)
        except BailOut:
            pass
            #raise BailOut

queens = add_queen([3])
print (queens)
print ("\n".join(". "*q + "Q " + ". "*((BOARD_SIZE - q) - 1) for q in queens))
print("count=",count)





















#BOARD_SIZE = 8
#count=0
#def under_attack(col, queens):
#    left = right = col

#    for r, c in reversed(queens):
#        left, right = left - 1, right + 1

#        if c in (left, col, right):
#            return True
#    return False

#def solve(n):
#    if n == 0:
#        return [[]]

#    smaller_solutions = solve(n - 1)

#    return [solution+[(n,i+1)]
#        for i in range(BOARD_SIZE)
#            for solution in smaller_solutions
#                if not under_attack(i+1, solution)]
#for answer in solve(BOARD_SIZE):
#    count += 1
    #print (answer)

    #n = tg.Queens(3)
    #n.printsolution()
    #s= n.solve()
    ##print (next(s))
    #for i in s:
    #    print (i)    #for row in board:
    #    for col in range(len(board)):
    #        columns=[ board[x][col] for x in range(0, len(board))]  #
    #        #print ("columns=")
    #        #for i in columns: print (i)
    #for r in range(len(board)):
    #    for c in range( len(board[r]) ):            
    #        print("r=",r, "c=",c, "board[r]=",board[r],"board[r][c]=",board[r][c])
    #        #if r+1 <= len(board) and c+1 <= r:
    #        #    diagonal += board[r+1][c+1]
    #        ##diagonal = board[r][c] + board[r+1][c+1]
    #        print ("diagonal=",diagonal)
    ##for i in enumerate(board): print(i)

    


    #LONG diagonals
    #diagonal1 = [ board[x][x] for x in range(0,len(board)) ]
    #diagonal2 = [ board[x][len(board) - x- 1] for x in range(0,len(board)) ]


            ##print("board=",board)
            ##build diagonal
            #if i == '.':                #if the space is empty
            #    #are there any other queens on this row?
            #    if 'Q' not in row:
            #        #are there any other queens in this column?
            #        if 'Q' not in columns:
            #            if 'Q' not in diagonal:
            #                count+=1
        #got all the solos?

    #########################################################
    #Process Data
    #for the maximum number of queens possible (at worst, n*m) 
    #place a queen in all possible positions...
    #
    #for r in board:
    #    for c in board[r]:
    #        print("c=",c,"r=",r)
    #answer=count

    #print(answer % 100000000)
    #print(answer % 1000000007)
    #print(answer % 10**7)