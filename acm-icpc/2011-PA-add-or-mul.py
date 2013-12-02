'''
Problem A
To Add or to Multiply
'''

import sys


# Clase para recoger todos las posibles soluciones. Cuando construyo un
# nodo puedo ejecutar su método build. Esto provocará que se construyana
# a su vez sus hijos de forma recursiva.

class Tree():

    def __init__(self,config,output,op):
        self.config=config
        self.output=output
        self.op=op

        self.aChild=None
        self.mChild=None


    # Compruebo limites por exceso
    def isValid(self): 
        if (self.output[1]>self.config['s']):
            return False
        return True


    # Compruebo si es un nodo exitoso
    def isSuccess(self):
        if ( (self.output[0]>=self.config['r']) and (self.output[1]<=self.config['s'])):
            return True
        return False

            
    # Construyo los arboles hijos siempre y cuando estos cumplan
    # el requisito de validez
    def build(self):
        aout=[0,0]
        mout=[0,0]

        aout[0]=self.output[0]+self.config['a']
        aout[1]=self.output[1]+self.config['a']

        mout[0]=self.output[0]*self.config['m']
        mout[1]=self.output[1]*self.config['m']

        self.aChild=Tree(self.config,aout,"A")
        self.mChild=Tree(self.config,mout,"M")

        if (self.aChild.isValid()):
            self.aChild.build()

        if (self.mChild.isValid()):
            self.mChild.build()

          

# Recorro el árbol buscando nodos exitosos. Para cada nodo que recorro
# apunto su codigo de instrucción en el programa, cuando vuelvo a el,
# acabada la exploración de sus hijos y retorno hacia el padre, quito
# ese codigo de operación.
#
# Cuando encuentro un caso de éxito clono el contenido del buffer
# programa en ese momento a la variable pcopy y la adjunto a la lista de
# programas exitosos.

def walkTree(succs,program,tree):

    if (tree==None):
        return

    program.append(tree.op)

    if (not tree.isSuccess()):
        walkTree(succs,program,tree.mChild)
        walkTree(succs,program,tree.aChild)
    else:
        pcopy=program[:]
        succs.append(pcopy)
        #print ("Econtrado nº"+str(len(succs))+": "+str(program)+ "output: "+str(tree.output))

    program.pop()
        



# Comprime el programa en forma de lista de Aes y Mes en un string
# tal y como se indica en el enunciado

def compressProgram(program):
    p=""
    i=0
    m=0
    a=0
    while (i<len(program)):
        if (program[i]=="M"):
            m+=1
            if (a>0):
                p=p+str(a)+"A "
                a=0
            
        if (program[i]=="A"):
            a+=1
            if (m>0):
                p=p+str(m)+"M "
                m=0
        i+=1

    if (a>0):
        p=p+str(a)+"A"
        a=0
    if (m>0):
        p=p+str(m)+"M"
        m=0

    return p
        


def main():
    tests=[]
    finput=open("2011-PA-add-or-mul.input")
    for line in finput.readlines():
        numbers=line.strip().split(" ")
        numbers=list(map(int,numbers))
        if max(numbers)==0:
            break
        config={}
        config['a']=numbers[0]
        config['m']=numbers[1]
        config['p']=numbers[2]
        config['q']=numbers[3]
        config['r']=numbers[4]
        config['s']=numbers[5]
        tests.append(config)

    # Una vez leidos todos los test empeizo a procesar

    ntest=1
    for config in tests:
        output=[config['p'],config['q']]
        program=[]
        success=[]

        tree=Tree(config,output,"")
        tree.build()

        walkTree(success,program,tree)

        # Calculo la longitud mínima
        minlen=sys.maxsize
        for p in success:
            if (len(p)<=minlen):
                minlen=len(p)

        # Solo me quedo con los que tienen esa longitu mínima
        programs=[] 
        for p in success:
            if len(p)==minlen:
                programs.append(compressProgram(p))


        programs.sort()

        #print (programs)

        msg=""
        if (len(programs)==0):
            msg="impossible"
        else:
            best=programs[0]
            if len(best)==0:
                msg="empty"
            else:
                msg=best
        
        print ("Case "+str(ntest)+": "+msg)
        ntest+=1




if (__name__=='__main__'):
    main()
