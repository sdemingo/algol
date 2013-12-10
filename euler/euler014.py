'''
Problem 14

The following iterative sequence is defined for the set of positive
integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following
sequence: 13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1

It can be seen that this sequence (starting at 13 and finishing at 1)
contains 10 terms. Although it has not been proved yet (Collatz
Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?
'''



#
#Aproximación recursiva sencilla. 
#

def secuencia2(n):
    if (n==1):
        return 1
    else:
        if (n%2)==0:
            return 1+secuencia2(n//2)
        else:
            return 1+secuencia2((3*n)+1)



#
# Aproximación recursiva más optima guardando un vector de longitudes de
# series. Antes de calcular la serie de un número miramos si
# tengo la longitud de su serie de Collatz ya calculada, pues esta
# distancia es lo único que nos interesa. En ese caso la retorno para
# evitar no calcularla otra vez.
#

def secuencia(n,tabla):
    if (n==1):
        return 1
    else:
        if ((n<len(tabla) and (tabla[n]!=0))):
            return tabla[n]  # La distancia de Collatz de n ya está calculada
        else:
            r=0
            if (n%2)==0:
                r=1+secuencia(n//2,tabla)
            else:
                r=1+secuencia((3*n)+1,tabla)
            if (n<len(tabla)):
                tabla[n]=r
            return r




def main():
    
    tabla=[0]*1000000
    max=0
    number=0
    for n in list(reversed(range(500000,1000000))):
        l=secuencia(n,tabla)
        if (l>=max):
            max=l
            number=n


    print ("Número: "+str(number)+" con una longitud de serie de: "+str(max))





if (__name__=='__main__'):
    main()
