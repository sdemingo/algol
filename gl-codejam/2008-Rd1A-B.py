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

import operator

def prepare(clients,batches):

    clients.sort(key=operator.itemgetter(0))
    #print (clients)
    for c in clients:
        client_ok=False
        request=c[1]
        for r in enumerate(request):
            i,f=r
            if (f!=-1):
                if (batches[i]==-1):   # Vaso no configurado
                    batches[i]=f
                    client_ok=True
                else:                  # Vaso ya configurado
                    if (batches[i]==f):  
                        client_ok=True
            if (client_ok):  # Si el cliente ya se ha satisfecho sigo
                break
    
        if (not client_ok):  # Si el cliente no tiene más peticiones y no está satisfecho error
            return "IMPOSSIBLE"


    # Los vasos no utilizados los pongo a 0
    for i in range(len(batches)):
        if batches[i]==-1:
            batches[i]=0

    batches=map(str,batches)
    return " ".join(batches)

            
def client_weight(request):
    
    # Se suman los -1s y los 0s. Los que menos cosas pidan tendrán menos peso
    # Además los que tengan algún uno multiplican esta suma por N (longitud de request)
    # para tener siempre la mínima puntuación:
    # Los que solo piden
    # una cosa caliente, los que solo piden una cosa fria, los que piden
    # varias cosas pero al menos una caliente, los que piden varias
    # cosas y todas frias

    w=0
    malted=False
    for i in request:
        if ((i==0) or (i==-1)):
            w+=i
        if (i==1):
            malted=True

    if (malted):
        return w*2
    else:
        return w
            

    
def main():
    f =open("2008-Rd1A-B.small.input")
    #f =open("2008-Rd1A-B.input")
    f2=open("2008-Rd1A-B.output","w")
    lines=f.readlines()
    ntest=int(lines[0].strip())

    lines=lines[1:]
    t=0
    off=0
    while (t<ntest):
        nflav=int(lines[off])
        batches=[-1 for x in range(nflav)]  # estado final de mis N vasos
        ncost=int(lines[off+1])
        clients=[]   # estado todos los clientes y sus pesos
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
            # Calculo el peso del cliente y lo inserto junto con los demás
            w=client_weight(request)
            client=[w]+[request]
            clients.append(client)
    
        out=prepare(clients,batches)
        t+=1
        off+=2+ncost
       
        print ("Case #"+str(t)+": "+out)
        f2.write("Case #"+str(t)+": "+out+"\n")
        #print (clients)
                




if (__name__=='__main__'):
    main()
