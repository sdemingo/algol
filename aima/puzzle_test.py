#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''

   The n-puzzle problem with differents approaches

'''

from searches import *
from puzzle import *
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
def search(tree,f):
    return f(tree)



def main():

    initState=[[1,2,0],[5,4,8],[3,6,7]]

    p=Puzzle(initState)
    
    print " Solving ... "
    
    rootState = TreeNode(None,p)  
    finalState = search(rootState,breadFirstSearch)
    
    rootState = TreeNode(None,p)
    finalState = search(rootState,deepFirstSearch)
    
    





if (__name__=='__main__'):
    main()


