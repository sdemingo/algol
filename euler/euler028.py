'''
Problem 28

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is
101.

What is the sum of the numbers on the diagonals in a 1001 by 1001
spiral formed in the same way?
'''

MAX_SPIRAL=1001*1001

def main():

    cont=0
    inc=2
    i=1
    total=0

    while (i<=MAX_SPIRAL):
        total+=i
        cont+=1
        if (cont<4):
            i+=inc
        else:  #cont==4
            i+=inc
            inc=inc+2
            cont=0

    print (total)
            



if (__name__=='__main__'):
    main()
