'''
Sergio de Mingo Gil
'''

import math

def distance(a,b,c,d):
    return math.fabs(a-c)+math.fabs(b-d)


def queryDistance(dx,dy,coffees,dist):
    #print (coffees)
    #print (distance)
    grid=[[0]*dx for i in range(dy)]
    maxp=0
    loc=[0,0]
    for c in coffees:
        c_i=c[0]-1
        c_j=c[1]-1
        grid[c_i][c_j]=-100
        for i in range(max(0,c_i-dist),min(c_i+dist+1,dy)):
            for j in  range(max(0,c_j-dist),min(c_j+dist+1,dx)):
                if (distance(i,j,c_i,c_j)<=dist):
                    grid[i][j]+=1
                    if (grid[i][j]>maxp): # Si maxp es mayor sustituimos siempre
                        maxp=grid[i][j]
                        loc=[i,j]
                    if (grid[i][j]==maxp):
                        if (j>loc[1]):   # si está más al sur
                            #pillado
                            maxp=grid[i][j]
                            loc=[i,j]
                        else:
                            if ((j==loc[1]) and (i>loc[0])):  # si igual al sur pero más al oeste
                                maxp=grid[i][j]
                                loc=[i,j]
                                
                        # solo sustituimos si las coordeandas con menores
                        #locations.append((grid[i][j],[i,j]))
                        #locations.append("({0},{1})".format(i+1,j+1))


    #print (grid)
    #print (locations)
    #locations.sort()
    #loc=locations.pop()
    #loc[0]+=1
    #loc[1]+=1
    return (maxp,"({0},{1})".format(loc[0]+1,loc[1]+1))

def main():
    
    f=open("2011-PE-coffe-central.input")
    lines=f.readlines()
    i=0
    test=1
    while (i<len(lines)):
        city=lines[i].strip().split()
        city=list(map(int,city))
        if max(city)==0:
            break
        coffees=[]
        distances=[]
        dx=city[0]
        dy=city[1]
        n=city[2]
        q=city[3]

        i+=1
        for p in range(0,n):
            point=lines[i+p].strip().split()
            point=list(map(int,point))
            coffees.append(point)
        i+=n

        for d in range (0,q):
            distance=lines[d+i].strip().split()
            distances.append(int(distance[0]))
        i+=q
            
        # print (city)
        # print (coffes)
        # print (distances)

        print ("Case "+str(test))
        #d=distances[0]
        for d in distances:
            n,loc=queryDistance(dx,dy,coffees,d)
            print ("{0} {1}".format(n,loc))




if (__name__=='__main__'):
    main()
