'''
* Problem 4.1-3 of CLRS. Pág 74

The brute-force rutine for solving the maximum-subarray problem in an
integer vector.
'''

import random

def forcebrute(v):
    max=-1000000
    r=len(v)
    l=0
    for i in range(len(v)):
        sum=0
        for j in range(i,len(v)):
            sum+=v[j]
            if (sum>=max):
                max=sum
                r=j
                l=i
    return (l,r,max)


def main():
    #v=[random.randint(-9,9) for i in range(10)]
    v=[-2,1,8,9,4,-3,-5,6,1,-2]

    print (v)
    left,right,value=forcebrute(v)
    print ("left={0} right={1} value={2}".format(left,right,value))






if (__name__=='__main__'):
    main()
