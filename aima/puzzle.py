#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''

   The n-puzzle problem mode. 

'''


import random
import copy


N=3                                 # N-puzzle dimension
FINAL=[[0,1,2],[3,4,5],[6,7,8]]     # Final state

class Puzzle():

    def __init__(self,board=None):
        if board==None:
            a=0
            self.board=FINAL[:]
            random.shuffle(self.board)
            for row in self.board:
                random.shuffle(row)
        else:
            self.board=board[:]


    def __str__(self):
        s=""
        for row in self.board:
            for col in row:
                s+=str(col)+" "
            s+="\n"
        return s

    # Find a tile in the board
    def find(self,i):
         for row,c in enumerate(self.board):
            for col,c in enumerate(self.board[row]):
                if self.board[row][col] == i:
                    return row,col

    # Performs a move
    def applyMove(self,move):
        row1,col1=self.find(0)
        row2,col2=move

        self.board[row1][col1]=self.board[row2][col2]
        self.board[row2][col2]=0


    # Returns all the puzzles based on this, before performing all legal moves
    def nexts(self):
        row,col=self.find(0)
        nexts=[]
        
        if (row>0):
            nexts.append([row-1,col])
        if (row<N-1):
            nexts.append([row+1,col])
        if (col>0):
            nexts.append([row,col-1])
        if (col<N-1):
            nexts.append([row,col+1])
        
        nexts_puzzles=[]
        for move in nexts:
            p=copy.deepcopy(self)
            p.applyMove(move)
            nexts_puzzles.append(p)

        return nexts_puzzles
        
    # Returns True is the puzzle is the final
    def isFinal(self):
        for row,c in enumerate(self.board):
            for col,c in enumerate(self.board[row]):
                if self.board[row][col] != FINAL[row][col]:
                    return False
        return True
        




# NPuzzle Heuristics functions

def misplacedTiles(puzzle):

    mplaced=0
    pFinal=Puzzle(FINAL)
    for row,c in enumerate(puzzle.board):
        for col,c in enumerate(puzzle.board[row]):
            if puzzle.board[row][col] != pFinal.board[row][col]:
                mplaced+=1

    return mplaced


def manhattanDistances(puzzle):

    dist=0
    for i in range(0,(N*N)-1):
        (col,row)=puzzle.find(i)
        expected_row = int(i / N)
        expected_col = int(i % N)
        dist += abs(col-expected_col) + abs(row-expected_row)

    return dist
 
