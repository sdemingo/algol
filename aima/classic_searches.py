#!/usr/bin/python
# -*- coding: utf-8 -*- 


import copy



'''

   Search tree

'''
 
class TreeNode():
    
    def __init__(self,parent,s):
        self.parent=parent
        self.state=s


    def expand(self):
        self.childs=[]
        news=self.state.nexts()
        for nstate in news:
            c_nstate=copy.deepcopy(nstate)
            child=TreeNode(self,c_nstate)
            self.childs.append(child)


    def depth(self):
        c=0
        node=self
        while(node.parent):
            c+=1
            node=node.parent
        return c










'''

   Uninformed search strategies

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





MAX_DEPTH=11   #Depth limite


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

   Informed search strategies

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



def a_star(node, heuristic):

    if node.depth() >= MAX_DEPTH:
        return None

    if node.state.isFinal():
        return node
    else:
        node.expand()
        child_cost=node.depth()+1
        childs=node.childs

        # sort candidates childs by heuristic and acumulated cost (in
        # this example, is the depth of the node) value
        candidates=[]
        for c in childs:
            h=heuristic(c.state) + child_cost
            candidates.append((h,c))
        
        candidates.sort(key=lambda tup:tup[0])

        for h,c in candidates:
            fstate = greedy(c,heuristic)
            if fstate != None:
                return fstate

        return None
