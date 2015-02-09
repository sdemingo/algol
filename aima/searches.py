#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''

   Uninformed search strategies to resolve the n-puzzle problem

'''


def breadFirstSearch(treenode):
    
    q=[]
    q.append(treenode)
    while (len(q)>0):
        node = q.pop(0)
        if node.state.isFinal():
            return node
        else:
            node.expand()
            q.extend(node.childs[:])
    
    return None





MAX_DEPTH=12   #Depth limite


def deepFirstSearch(node):
    
    if node.depth() >= MAX_DEPTH:
        return None

    if node.state.isFinal():
        return node
    else:
        node.expand()
        childs=node.childs
        for c in childs:
            fstate = deepFirstSearch(c)
            if fstate != None:
                return fstate

        return None



'''

   Informed search strategies to resolve the n-puzzle problem

'''


def greedy(node, heuristic):

    if node.depth() >= MAX_DEPTH:
        return None

    if node.state.isFinal():
        return node
    else:
        node.expand()
        childs=node.childs

        # sort candidates childs by heuristic value
        candidates=[]
        for c in childs:
            h=heuristic(c.state)
            candidates.append((h,c))
        
        candidates.sort(key=lambda tup:tup[0])

        for h,c in candidates:
            fstate = greedy(c,heuristic)
            if fstate != None:
                return fstate

        return None
