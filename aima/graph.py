#!/usr/bin/python
# -*- coding: utf-8 -*- 

import string

'''

   The graph problem model

'''



class Graph():
    def __init__(self,keys):
        self.keys=keys
        zeros=[0 for i in range(0,len(self.keys))]
        self.distances=[zeros[:] for i in range(0,len(self.keys))]


    def __str__(self):
        s="  "
        for k in self.keys:
            s+="   "+k+" "
        s+="\n"

        i=0
        for row in self.distances:
            k=self.keys[i]
            s+=k+" "
            for col in row:
                s+="{:4d} ".format(col)
            s+="\n"
            i+=1
        return s



    def setDistance(self,city1,city2,dist):
        try:
            k1=self.keys.index(city1)
            k2=self.keys.index(city2)
            self.distances[k1][k2]=dist
            self.distances[k2][k1]=dist
        except:
            print "City "+city1+" or "+city2+" not exists"
            
    def getDistance(self,city1,city2):
        try:
            k1=self.keys.index(city1)
            k2=self.keys.index(city2)
            return self.distances[k1][k2]
        except:
            print "City "+city1+" or "+city2+" not exists"
            return 0



# A traveller is the state in the tree
class Traveller():
    
    def __init__(self,distances):
        self.cities=[]
        self.distances=distances


    def moveTo(self,city):
        if len(self.cities) > 0:
            now = self.cities[len(self.cities)-1]
            self.cities.append(city)
            return self.distances.getDistance(now,city)
        else:
            self.cities.append(city)
            return 0



