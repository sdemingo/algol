'''
Problem A
To Add or to Multiply
'''


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
        
        


def main():
    #a m p q r s
    #1 2 2 3 10 20
    config={'a':1,'m':2,'p':2,'q':3,'r':10,'s':20}


    output=[2,3]
    program=[]
    success=[]

    tree=Tree(config,output,"")
    tree.build()
    print ("Arbol construido")

    walkTree(success,program,tree)

    # comprimo los programas de success en strings y los ordeno
    programs=[]
    for p in success:
        programs.append(" ".join(p))

    print (programs)
 





if (__name__=='__main__'):
    main()
