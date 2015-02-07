#!/usr/bin/python
# -*- coding: utf-8 -*- 


'''

   Search strategies to resolve the n-puzzle problem

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

