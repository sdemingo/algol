'''
Problem 26

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It
can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest
recurring cycle in its decimal fraction part.  
'''

import re
import decimal

def period(n):
    ns=str(n)
    r = re.compile(r"(.+?)\1+")
    l=r.findall(ns)
    l.sort(key=len,reverse=True)
    return l




def main():

    for d in range(1,1000):
        print (d,1/d, 10%d)
        




if (__name__=='__main__'):
    main()
