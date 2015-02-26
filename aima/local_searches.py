#!/usr/bin/python
# -*- coding: utf-8 -*- 


import copy


'''

   Local search strategies

'''

 
def hillClimbing(state,heuristic):
    
    current=state

    while (True):
        h_current=heuristic(current)
        nexts=current.nexts()

        candidates=[]
        for c in nexts:
            h=heuristic(c)
            candidates.append((h,c))

        # sort nexts states childs by heuristic value
        candidates.sort(key=lambda tup:tup[0])

        # take the lowest
        if (len(candidates)>0):
            nh,ns=candidates[0]
        else:
            return state

        if nh > h_current:
            return current
        else:
            current = ns
