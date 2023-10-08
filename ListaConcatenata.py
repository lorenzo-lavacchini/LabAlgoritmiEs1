
#creo la classe dell'elemento della lista

import array
class element:
    def __init__(self,key):
        self.key = key
        self.prev = None
        self.next = None

#creo la classe della lista (la lista viene create vuota)
class listConc:
    def __init__(self):
        self.head=None


    #inserimento elemento in testa alla lista
    def insert(self,x):
        x.next = self.head
        if self.head != None:
            self.head.prev = x
        self.head = x
        x.prev = None

    #ricerca di un elemento nella lista
    def search(self,k):
        #utilizzo x per scorrere la lista
        x = self.head
        while x != None and x.key != k:
            x = x.next
        return x #ritorna None se non trova l'elemento

    #cancellazione di un elemento dalla lista data la chiave
    def delete(self,k):
        x = self.search(k)
        if(x != None):
            if x.prev != None:
                x.prev.next = x.next
            else:
                self.head = x.next
            if x.next != None:
                x.next.prev = x.prev
            return True
        else:
            return False

    #METODI DI SERVIZIO AI FINI DEI TEST
    #cancellazione di un elemento dalla testa dala lista (siccome l'inserimento è fatto in testa
    # questo metodo assume il significato di cancellazione dell'ultimo elemento inserito)
    def deleteLastElementInserted(self):
        x = self.head.next
        self.head = x
        x.prev = None

    #stampa tutte le chiavi degli elementi nella lista
    def printAll(self):
        keys=[] #array con le chiavi da stampare
        if self.head == None:
            print("Lista vuota")
        else:
            x = self.head
            while x != None:
                keys.append(x.key)
                x = x.next
        print(keys)

    #restituisce il numero di elementi nella lista
    def getSize(self):
        count = 0
        x = self.head
        while(x != None):
            count = count + 1
            x = x.next
        return count




