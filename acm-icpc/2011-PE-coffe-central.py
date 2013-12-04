'''
Sergio de Mingo Gil
'''

def queryDistance(dx,dy,coffees,distance):
    #print (coffees)
    #print (distance)
    grid=[[0]*dx for i in range(dy)]
    maxp=0
    locations=[]
    for c in coffees:
        grid[c[0]-1][c[1]-1]=-100
        i=c[0]-distance
        while ((i<=c[0]+distance)  and (i<dy)):
            j=c[1]-distance
            while ((j<=c[1]+distance) and (j<dx)):
                grid[i][j]+=1
                if (grid[i][j]>=maxp):
                    maxp=grid[i][j]
                    locations.append([i,j])
                j+=1
            i+=1


    print (grid)
    #print (locations)
    loc=locations.pop()
    loc[0]+=1
    loc[1]+=1
    #print (loc)
    return loc

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
        d=distances[1]
        #for d in distances:
        loc=queryDistance(dx,dy,coffees,d)
        print (loc)




if (__name__=='__main__'):
    main()
