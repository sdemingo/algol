'''
Problem E
Coffe Central
'''

import math



# Para cada distancia dada recibo la lista de todos los cafes del grid
# compruebo un área con forma de cuadrado de lado 'dist' y con el centro
# el cafe. Desde todos estos puntos mido la distancia al cafe y para los
# puntos que sean válida, incremento su valor en la matriz de pesos. Al
# final solo he de tomar de esta matriz de pesos la casilla que tenga un
# número mayor (maxp). En caso de encontrar un casilla con un valor
# igual al último maxp encontrado me quedo con la que esté más al sur y
# más al oeste.


def queryDistance(dx,dy,coffees,dist):

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
                    # Si maxp es mayor sustituimos siempre
                    if (grid[i][j]>maxp): 
                        maxp=grid[i][j]
                        loc=[i,j]

                    if (grid[i][j]==maxp):
                        if (j<loc[1]):   # si está más al sur
                            maxp=grid[i][j]
                            loc=[i,j]
                        else:
                            # si igual al sur pero más al oeste
                            if ((j==loc[1]) and (i<loc[0])): 
                                maxp=grid[i][j]
                                loc=[i,j]

    return (maxp,"({0},{1})".format(loc[0]+1,loc[1]+1))



def distance(a,b,c,d):
    return math.fabs(a-c)+math.fabs(b-d)



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

        print ("Case "+str(test))
        for d in distances:
            n,loc=queryDistance(dx,dy,coffees,d)
            print ("{0} {1}".format(n,loc))




if (__name__=='__main__'):
    main()
