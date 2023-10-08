class node:
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
        self.p = None

class ABR:
    def __init__(self):
            self.root = None
    #ricerca iterativa in albero binario

    def searchABR(self,k):
        x = self.root
        while x != None and k != x.key:
            if k<x.key:
                x = x.left
            else:
                x = x.right
        return x

    def insertABR(self,z):
        x = self.root
        y = None
        while x != None:
            y = x
            if z.key < x.key:
                x = x.left
            else:
                x = x.right
        z.p = y
        if y == None: #l'albero era vuoto, allora z fa da radice
            self.root = z
        elif z.key < y.key:
            y.left = z
        else:
            y.right = z

    def treeTransplant(self,u,v):
        if u.p == None:
            self.root = v
        elif u.p.left == u:
            u.p.left = v
        else:
            u.p.right = v
        if v != None:
            v.p = u.p

    def treeMinimum(self):
        x = self.root
        while x.left != None:
            x = x.left
        return x

    def deleteABR(self,z):
        if z.left == None:
            self.treeTransplant(z,z.right)
        elif z.right == None:
            self.treeTransplant(z,z.left)
        else:
            y = self.treeMinimum(z.right)
            if y.p != z:
                self.treeTransplant(y,y.right)
                y.right = z.right
                y.right.p = y
            self.treeTransplant(z,y)
            y.left = z.left
            y.left.p = y

    def inorderTreeWalk(self,x):
        if x != None:
            self.inorderTreeWalk(x.left)
            print(x.key)
            self.inorderTreeWalk(x.right)

    def altezza(self, nodo):
        # Controllo che l'albero non sia vuoto
        if nodo is None:
            return 0

        # Altrimenti ricalcolo ricorsivamente l'altezza di ogni nodo
        sinistra = self.altezza(nodo.left)
        destra = self.altezza(nodo.right)

        # Ritorno il massimo a ogni iterazione
        return max(sinistra, destra) + 1
