'''
Problem A
To Add or to Multiply
'''


def instructionA(config,output,undo=False): 
    if (undo):
        for i in range(len(output)):
            output[i]-=config['a']
    else:
        for i in range(len(output)):
            output[i]+=config['a']



def instructionM(config,output,undo=False): 
    if (undo):
        for i in range(len(output)):
            output[i]//=config['m']
    else:
        for i in range(len(output)):
            output[i]*=config['m']




def applyIns(config,output,program):
    if ( (min(output)>=config['r']) and (max(output)<=config['s'])): # fin del programa. Éxito
        print ("Exito: "+str(program)+" salida: "+str(output))
        return True
    else:
        instructionM(config,output)
        if (max(output)>config['s']):
            instructionM(config,output,True)# Deshacer mul
            return False     # camino excedido
        else:
            program.append("M")
            if ( (min(output)>=config['r']) and (max(output)<=config['s'])): # Exito
                print ("Exito: "+str(program)+" salida: "+str(output))
                instructionM(config,output,True)# Deshacer mul

        applyIns(config,output,program)

        instructionA(config,output)
        if (max(output)>config['s']):
            instructionA(config,output,True)# Deshacer sum
            return False     # camino excedido
        else:
            program.append("A")
            if ( (min(output)>=config['r']) and (max(output)<=config['s'])): # Exito
                print ("Exito: "+str(program)+" salida: "+str(output))
                instructionA(config,output,True)# Deshacer mul

        applyIns(config,output,program)

          



def main():
    #a m p q r s
    #1 2 2 3 10 20
    config={'a':1,'m':2,'p':2,'q':3,'r':10,'s':20}


    output=[2,3]
    program=[]
    applyIns(config,output,program)

 





if (__name__=='__main__'):
    main()
