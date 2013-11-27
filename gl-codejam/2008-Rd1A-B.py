# -*- coding: utf-8 -*- 
'''
Round 1A 2008
=============

Problem B

Problem

You own a milkshake shop. There are N different flavors that you can
prepare, and each flavor can be prepared "malted" or "unmalted". So,
you can make 2N different types of milkshakes.

Each of your customers has a set of milkshake types that they like,
and they will be satisfied if you have at least one of those types
prepared. At most one of the types a customer likes will be a "malted"
flavor.

You want to make N batches of milkshakes, so that:

    * There is exactly one batch for each flavor of milkshake, and it
      is either malted or unmalted.
    * For each customer, you make at least one milkshake type that they like.
    * The minimum possible number of batches are malted. 

Find whether it is possible to satisfy all your customers given these
constraints, and if it is, what milkshake types you should make.

If it is possible to satisfy all your customers, there will be only
one answer which minimizes the number of malted batches.

Input

    * One line containing an integer C, the number of test cases in the input file. 

For each test case, there will be:

    * One line containing the integer N, the number of milkshake flavors.
    * One line containing the integer M, the number of customers.
    * M lines, one for each customer, each containing:
        + An integer T >= 1, the number of milkshake types the customer likes, followed by
        + T pairs of integers "X Y", one for each type the customer
        likes, where X is the milkshake flavor between 1 and N
        inclusive, and Y is either 0 to indicate unmalted, or 1 to
        indicated malted. Note that:

            + No pair will occur more than once for a single customer.
            + Each customer will have at least one flavor that they like
            (T >= 1).
            + Each customer will like at most one malted flavor. (At
            most one pair for each customer has Y = 1). 

    * All of these numbers are separated by single spaces. 

'''

import sys
import string
import os

def areConflicts(flavour,option):
    for c in clients:
        if c[flavour]!=option:
            return True;   #Otro cliente lo ha pedido diferente
    return False;


def prepare(clients,batches):

    # Ordenar los clientes por peso, de más a menos:  los que solo piden
    # una cosa caliente, los que solo piden una cosa fria, los que piden
    # varias cosas pero al menos una caliente, los que piden varias
    # cosas y todas frias
        
        
               
            



    
def main():
    f =open("2008-Rd1A-B.input")
    f2=open("2008-Rd1A-B.output","w")
    lines=f.readlines()
    ntest=int(lines[0].strip())

    lines=lines[1:]
    t=0
    off=0
    while (t<ntest):
        nflav=int(lines[off])
        batches=[0 for x in range(nflav)]  # estado final de mis N vasos
        ncost=int(lines[off+1])
        costs=[]   # estado todos los clientes
        for i in range(0,ncost):
            request=[-1 for x in range(nflav)]   # peticion de ese cliente
            c=lines[off+2+i].split(" ")
            c=list(map(int,c))
            nmilks=c[0]
            c=c[1:]
            for m in range(nmilks):
                f,m,*rest=c
                request[f-1]=m   # el cliente i quiere ese sabor f como m (malted o unmalted)
                c=rest
            costs.append(request)
    
        batches=prepare(costs,batches)
        t+=1
       
        print ("Case #"+str(t)+": "+batches)
        print (costs)
                




if (__name__=='__main__'):
    main()
