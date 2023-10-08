# This is a sample Python script.

# Press Maiusc+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

from ListaConcatenata import element
from ListaConcatenata import listConc
from ABR import node
from ABR import ABR
from timeit import default_timer as timer
import random
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline




def valuesRandomListConc(keyMax):
    # Creo lista con i valori randomici
    valori = listConc()
    for k in range(keyMax):
        valori.insert(element(random.randint(0,keyMax)))
    return valori

def valuesRandomTree(dimTree,keyMax):
    # Creo lista con i valori randomici
    valori = ABR()
    for k in range(dimTree):
        keyToInsert = random.randint(0, keyMax)
        nodeToInsert = node(keyToInsert)
        if valori.searchABR(keyToInsert) == None:
         valori.insertABR(nodeToInsert)
    return valori

def testInsertListConc(numVolte, numPerDim):
    dimList = 1
    testInsertAverageTimes = []
    for i in range (numVolte):
        totInsertTime = 0
        values = valuesRandomListConc(dimList)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.insert(element(random.randint(0,dimList)))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totInsertTime = totInsertTime + iterationTime
            # tolgo l'ultimo elemento inserito
            values.deleteLastElementInserted()
        testInsertAverageTimes.append(totInsertTime/dimList)
        dimList = dimList + 1
    #plot dei risultati
    x_axis = [i for i in range(numVolte)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testInsertAverageTimes, label="insert ", color="orange")
    plot1.set_title("Risultati per Insert implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")
    plt.show()
    return testInsertAverageTimes

def testInsertABR(numVolte, numPerDim):
    dimTree = 1
    testInsertAverageTimes = []
    testInsertTreeHeights = []
    for i in range (numVolte):
        totInsertTime = 0
        values = valuesRandomTree(dimTree,dimTree+10000)
        for j in range (numPerDim):
            startTimeStamp = timer()
            nodeToInsert = node(random.randint(0,numVolte+10000))
            values.insertABR(nodeToInsert)#incremento lo spazio delle chiavi in modo tale da diminuire la probabilità che in inserimento fallisca per colpa della generazione di una chiave uguale ad una già presente nell'albero
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totInsertTime = totInsertTime + iterationTime
            #tolgo l'ultimo nodo inserito
            values.deleteABR(nodeToInsert)
        testInsertAverageTimes.append(totInsertTime/numPerDim)
        testInsertTreeHeights.append(values.altezza(values.root))
        dimTree = dimTree + 1
    #plot dei risultati
    x_axis = [i for i in testInsertTreeHeights]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testInsertAverageTimes, label="search ", color="orange")
    plot1.set_title("Risultati per Insert implementata con ABR")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione albero in altezza")

    x_axis = [i for i in range(numVolte)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, testInsertAverageTimes, label="search ", color="blue")
    plot2.set_title("Risultati per Insert implementata con ABR")
    plot2.set_ylabel("tempo impiegato (secondi)")
    plot2.set_xlabel("dimensione albero in numero di nodi")
    plt.show()
    return testInsertAverageTimes
def testSearchListConc(numVolte, numPerDim):
    dimList = 1
    testSearchAverageTimes = []
    for i in range (numVolte):
        totSearchTime =0
        values = valuesRandomListConc(dimList)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.search(random.randint(0,dimList))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totSearchTime = totSearchTime + iterationTime
        testSearchAverageTimes.append(totSearchTime/numPerDim)
        dimList = dimList + 1
    #plot dei risultati
    x_axis = [i for i in range(numVolte)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testSearchAverageTimes, label="search ", color="orange")
    plot1.set_title("Risultati per Search implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")


    plt.show()
    return testSearchAverageTimes

def testDeleteListConc(numVolte,numPerDim):
    dimList = 1
    testDeleteAverageTimes = []
    for i in range (numVolte):
        totDeleteTime = 0
        values = valuesRandomListConc(dimList)
        for j in range (numPerDim):
            startTimeStamp = timer()
            result = values.delete(random.randint(0,dimList))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totDeleteTime = totDeleteTime + iterationTime
            #se la delete era andata a buon fine, reinserisco un elemento per compensare quello appena tolto
            if result == True:
                values.insert(element(random.randint(0,values.getSize()+1)))
        testDeleteAverageTimes.append(totDeleteTime / numPerDim)
        dimList = dimList + 1
    #plot dei risultati
    x_axis = [i for i in range(numVolte)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testDeleteAverageTimes, label="delete ", color="orange")
    plot1.set_title("Risultati per Delete implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")
    plt.show()
    return testDeleteAverageTimes


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
   #dimensione massima della lista su cui si fanno le operazioni
   numVolte = 1000
   #numero di volte in cui si fa la stessa operazione (insert,delete o search) per una lista di una certa dimensione n
   numPerDim = 100

   #test per operazioni di dizionario implementate con Lista Concatenata
   testSearchListConc(numVolte,numPerDim)
   #testDeleteListConc(numVolte,numPerDim)
   #testInsertListConc(numVolte,numPerDim)

   #test funzionamento alberi
   #testInsertABR(numVolte,numPerDim)

   #dimTree = 10000
   #tree1 = valuesRandomTree(dimTree,1000000)

   #tree1.inorderTreeWalk(tree1.root)
   #print("l'altezza è "+str(tree1.altezza(tree1.root)))
   #print(testInsertABR(numVolte,numPerDim))