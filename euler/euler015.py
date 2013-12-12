'''
Problem 15

Starting in the top left corner of a 2×2 grid, and only being able to
move to the right and down, there are exactly 6 routes to the bottom
right corner.

How many such routes are there through a 20×20 grid?
'''

MAX_I=20
MAX_J=20


def paths(table,i,j):
    if (i>MAX_I) or (j>MAX_J):
        return 0
    
    if (i==MAX_I) and (j==MAX_J):
        table[i][j]=1
        return table[i][j]
    else:
        if (table[i][j]>0):
            return table[i][j]
        else:
            table[i][j]=paths(table,i+1,j)+paths(table,i,j+1)
            return table[i][j]




def main():

    table=[[0 for i in range(MAX_I+1)]for j in range(MAX_J+1)]

    r=paths(table,0,0)
    print (r)

    


if (__name__=='__main__'):
    main()
