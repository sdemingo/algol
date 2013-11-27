# -*- coding: utf-8 -*- 
'''
Round 1A 2008
=============

Problem A

You are given two vectors v1=(x1,x2,...,xn) and v2=(y1,y2,...,yn). The
scalar product of these vectors is a single number, calculated as
x1y1+x2y2+...+xnyn.

Suppose you are allowed to permute the coordinates of each vector as
you wish. Choose two permutations such that the scalar product of your
two new vectors is the smallest possible, and output that minimum
scalar product.

Input

The first line of the input file contains integer number T - the
number of test cases. For each test case, the first line contains
integer number n. The next two lines contain n integers each, giving
the coordinates of v1 and v2 respectively. 

http://code.google.com/codejam/contest/32016/dashboard#s=p0

'''

import sys
import string
import operator


def main():
    f=open("2008-Rd1A-A.small.input")
    f2=open("2008-Rd1A-A.output","w")
    lines=f.readlines()
    ntest=int(lines[0].strip())

    lines=lines[1:]
    t=0
    off=0
    while (t<ntest):
        vlen=lines[off]
        v1=lines[off+1].strip().split(" ")
        v2=lines[off+2].strip().split(" ")
        v1=list(map(int,v1))
        v2=list(map(int,v2))
        v1.sort()
        v2.sort(reverse=True)
        scalar=0

        for i in range(0,len(v1)):
            scalar=scalar+(v1[i]*v2[i])

        f2.write("Case #"+str(int(t)+1)+": "+str(scalar)+"\n")

        t+=1
        off+=3

    f2.close()



if (__name__=='__main__'):
    main()
