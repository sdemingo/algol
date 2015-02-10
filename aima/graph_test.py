#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''

   The n-puzzle problem with differents approaches

'''

from searches import *
from graph import *
import time



# Decorator to measure the time
def wtime(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print '%s with %s function took %0.3f ms' % (f.func_name, args[1].__name__,(time2-time1)*1000.0)
        return ret
    return wrap



@wtime
def search(tree,f,h=None):
    if h==None:
        return f(tree)
    else:
        return f(tree,h)




def main():

    cities=["A","B","C","D","E"]

    m=Graph(cities)
    m.setDistance("A","B",5)
    m.setDistance("A","D",10)
    m.setDistance("B","C",3)
    m.setDistance("C","D",6)
    m.setDistance("C","E",5)
    m.setDistance("D","E",4)


    print " Distances map:"
    print 
    print m

    t=Traveller(m)
    d=t.moveTo("A")
    print "walked "+str(d)
    d=t.moveTo("B")
    print "walked "+str(d)
    d=t.moveTo("C")
    print "walked "+str(d)



if (__name__=='__main__'):
    main()


