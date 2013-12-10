'''

'''

MAX_I=20
MAX_J=20


class TreeNode():
    
    def __init__(self,i,j):
        self.i=i
        self.j=j
        self.i_child=None
        self.j_child=None
        #print (self.i,self.j)


    def build(self,paths):
        if (self.i==MAX_I) and (self.j==MAX_J):
            return paths+1
            
        n_i=self.i+1
        n_j=self.j+1
        if (n_i<=MAX_I):
            self.i_child=TreeNode(n_i,self.j)
            paths=self.i_child.build(paths)
        if (n_j<=MAX_J):
            self.j_child=TreeNode(self.i,n_j)
            paths=self.j_child.build(paths)

        return paths


def main():

    paths=0

    t=TreeNode(1,0)
    paths=t.build(paths)

    print (paths)






if (__name__=='__main__'):
    main()
