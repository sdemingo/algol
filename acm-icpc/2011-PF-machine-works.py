'''
Problem F
Machine Works
'''

class Machine():

    def __init__(self,p,r,g):
        self.price=p
        self.resoldPrice=r
        self.profit=g



class TreeNode():
    
    def __init__(self,c,d,m):
        self.account=c
        self.day=d
        self.machines=m
        self.childs=[]

    def buy(self,machine):
        c=self.account-machine.price
        d=self.days
        m=self.machines[:]
        m.append(machine)
        return TreeNode(c,d,m)

    def sold(self,machine):
        c=self.account+machine.resoldPrice
        d=self.days
        m=self.machines[:]
        m.remove(machine)
        return TreeNode(c,d,m)
       
    
    def produce(self):
        d=self.day+1
        c=self.account
        m=self.machines[:]
        for m in self.machines:
            c+=m.profit
        return TreeNode(c,d,m)

    def __str__(self):
        return "account:{0} day:{1}".format(self.account,self.day)
        

def main():
    
    tree=TreeNode(10,20,[])




if (__name__=='__main__'):
    main()
