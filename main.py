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
        if valori.search(keyToInsert) == None:
         valori.insert(nodeToInsert)
    return valori

#funzioni di test liste concatenate
def testInsertListConcGraphA(dimMax, numPerDim):
    testInsertAverageTimes = []
    for i in range (1,dimMax,1):
        totInsertTime = 0
        values = valuesRandomListConc(i)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.insert(element(random.randint(0,i)))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totInsertTime = totInsertTime + iterationTime
            # tolgo l'ultimo elemento inserito
            values.deleteLastElementInserted()
        testInsertAverageTimes.append(totInsertTime/i)
    #plot dei risultati
    x_axis = [i for i in range(1,dimMax,1)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testInsertAverageTimes, label="insert ", color="orange")
    plot1.set_title("Risultati per Insert implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")
    plt.show()
    return testInsertAverageTimes
def testInsertListConcGraphB(dimMax, numPerDim,dimIncrement):
    testInsertAverageTimes = []
    for i in range (1,dimMax,dimIncrement):
        totInsertTime = 0
        values = valuesRandomListConc(i)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.insert(element(random.randint(0,i)))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totInsertTime = totInsertTime + iterationTime
            # tolgo l'ultimo elemento inserito
            values.deleteLastElementInserted()
        testInsertAverageTimes.append(totInsertTime/i)
    #plot dei risultati
    x_axis = [i for i in range(1,dimMax,dimIncrement)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testInsertAverageTimes, label="insert ", color="orange")
    plot1.set_title("Risultati per Insert implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")
    plt.show()
    return testInsertAverageTimes
def testSearchListConcGraphA(dimMax, numPerDim):
    testSearchAverageTimes = []
    for i in range (1,dimMax,1):
        totSearchTime =0
        values = valuesRandomListConc(i)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.search(random.randint(0,i))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totSearchTime = totSearchTime + iterationTime
        testSearchAverageTimes.append(totSearchTime/numPerDim)
    #plot dei risultati
    x_axis = [i for i in range(1,dimMax,1)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis,testSearchAverageTimes, label="search ", color="orange")
    plot1.set_title("Risultati per Search implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")


    plt.show()
    return testSearchAverageTimes
def testSearchListConcGraphB(dimMax, numPerDim, dimIncrement):
    testSearchAverageTimes = []
    # rappresenta la dimensione attuale della lista su cui faccio il test
    # dimIncrement rappresenta di quanto aumento la lista ad ogni iterazione di i (qui la aumento di tanto così ho un grafico più liscio risultante)
    for i in range (1,dimMax,dimIncrement):
        totSearchTime =0
        values = valuesRandomListConc(i)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.search(random.randint(0,i))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totSearchTime = totSearchTime + iterationTime
        testSearchAverageTimes.append(totSearchTime/numPerDim)
    #plot dei risultati
    x_axis = [i for i in range(1,dimMax, dimIncrement)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis,testSearchAverageTimes, label="search ", color="orange")
    plot1.set_title("Risultati per Search implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")


    plt.show()
    return testSearchAverageTimes
def testDeleteListConcGraphA(dimMax, numPerDim):
    testDeleteAverageTimes = []
    for i in range (1,dimMax,1):
        totDeleteTime = 0
        values = valuesRandomListConc(i)
        for j in range (numPerDim):
            startTimeStamp = timer()
            result = values.delete(random.randint(0,i))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totDeleteTime = totDeleteTime + iterationTime
            #se la delete era andata a buon fine, reinserisco un elemento per compensare quello appena tolto
            if result == True:
                values.insert(element(random.randint(0,values.getSize()+1)))
        testDeleteAverageTimes.append(totDeleteTime / numPerDim)
    #plot dei risultati
    x_axis = [i for i in range(1,dimMax,1)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testDeleteAverageTimes, label="delete ", color="orange")
    plot1.set_title("Risultati per Delete implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")
    plt.show()
    return testDeleteAverageTimes
def testDeleteListConcGraphB(dimMax, numPerDim, dimIncrement):
    testDeleteAverageTimes = []
    for i in range (1,dimMax,dimIncrement):
        totDeleteTime = 0
        values = valuesRandomListConc(i)
        for j in range (numPerDim):
            startTimeStamp = timer()
            result = values.delete(random.randint(0,i))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp,8)
            totDeleteTime = totDeleteTime + iterationTime
            #se la delete era andata a buon fine, reinserisco un elemento per compensare quello appena tolto
            if result == True:
                values.insert(element(random.randint(0,values.getSize()+1)))
        testDeleteAverageTimes.append(totDeleteTime / numPerDim)
    #plot dei risultati
    x_axis = [i for i in range(1,dimMax,dimIncrement)]
    graph1, plot1 = plt.subplots()
    plot1.plot(x_axis, testDeleteAverageTimes, label="delete ", color="orange")
    plot1.set_title("Risultati per Delete implementata con Lista Concatenata")
    plot1.set_ylabel("tempo impiegato (secondi)")
    plot1.set_xlabel("dimensione vettore")
    plt.show()
    return testDeleteAverageTimes

#funzioni di test ABR
def testInsertABRGraphA(dimMax, numPerDim):
    testInsertAverageTimes = []
    for i in range (1,dimMax,1):
        totInsertTime = 0
        values = valuesRandomTree(i,i+10000000)
        values.inorderTreeWalk(values.root)
        for j in range (numPerDim):
            keyToInsert = random.randint(0, dimMax + 10000000)
            if values.searchABR(keyToInsert) == None:
                startTimeStamp = timer()
                nodeInserted = values.insertABR(node(keyToInsert))
                finishTimeStamp = timer()
                iterationTime = round(finishTimeStamp - startTimeStamp, 8)
                totInsertTime = totInsertTime + iterationTime
                # tolgo l'ultimo nodo inserito
                values.deleteABR(nodeInserted)
            else:
                if j == 0:
                    iterationTime = 0
                else:
                    iterationTime = round(totInsertTime / j, 8)
                totInsertTime = totInsertTime + iterationTime
        testInsertAverageTimes.append(totInsertTime/numPerDim)

    x_axis = [i for i in range(1,dimMax,1)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, testInsertAverageTimes, label="search ", color="blue")
    plot2.set_title("Risultati per Insert implementata con ABR")
    plot2.set_ylabel("tempo impiegato (secondi)")
    plot2.set_xlabel("dimensione albero in numero di nodi")
    plt.show()
    return testInsertAverageTimes

def testInsertABRGraphB(dimMax, numPerDim, dimIncrement):
    testInsertAverageTimes = []
    count = 0
    for i in range (1,dimMax,dimIncrement):
        totInsertTime = 0
        values = valuesRandomTree(i,i+10000000)
        values.inorderTreeWalk(values.root)
        for j in range (numPerDim):
            keyToInsert = random.randint(0, dimMax + 10000000)
            if values.searchABR(keyToInsert) == None:
                startTimeStamp = timer()
                nodeInserted = values.insertABR(node(keyToInsert))
                finishTimeStamp = timer()
                iterationTime = round(finishTimeStamp - startTimeStamp, 8)
                totInsertTime = totInsertTime + iterationTime
                # tolgo l'ultimo nodo inserito
                values.deleteABR(nodeInserted)
            else:
                count = count + 1
                if j == 0:
                    iterationTime = 0
                else:
                    iterationTime = round(totInsertTime / j, 8)
                totInsertTime = totInsertTime + iterationTime
        testInsertAverageTimes.append(totInsertTime/numPerDim)

    print(count)

    x_axis = [i for i in range(1,dimMax,dimIncrement)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, testInsertAverageTimes, label="search ", color="blue")
    plot2.set_title("Risultati per Insert implementata con ABR")
    plot2.set_ylabel("tempo impiegato (secondi)")
    plot2.set_xlabel("dimensione albero in numero di nodi")
    plt.show()
    return testInsertAverageTimes

def testSearchABRGraphA(dimMax, numPerDim):
    testSearchAverageTimes = []
    for i in range (1,dimMax,1):
        totInsertTime = 0
        values = valuesRandomTree(i,i+10000000)
        values.inorderTreeWalk(values.root)
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.search(random.randint(0,i))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp, 8)
            totInsertTime = totInsertTime + iterationTime
        testSearchAverageTimes.append(totInsertTime/numPerDim)

    x_axis = [i for i in range(1,dimMax,1)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, testSearchAverageTimes, label="search", color="blue")
    plot2.set_title("Risultati per Search implementata con ABR")
    plot2.set_ylabel("tempo impiegato (secondi)")
    plot2.set_xlabel("dimensione albero in numero di nodi")
    plt.show()
    return testSearchAverageTimes

def testSearchABRGraphB(dimMax, numPerDim, dimIncrement):
    testSearchAverageTimes = []
    for i in range (1,dimMax,dimIncrement):
        totInsertTime = 0
        values = valuesRandomTree(i,i+10000000)
        print("inizio albero")
        values.inorderTreeWalk(values.root)
        print("fine albero")
        for j in range (numPerDim):
            startTimeStamp = timer()
            values.search(random.randint(0, i))
            finishTimeStamp = timer()
            iterationTime = round(finishTimeStamp - startTimeStamp, 8)
            totInsertTime = totInsertTime + iterationTime
        testSearchAverageTimes.append(totInsertTime/numPerDim)
    x_axis = [i for i in range(1,dimMax,dimIncrement)]
    graph2, plot2 = plt.subplots()
    plot2.plot(x_axis, testSearchAverageTimes, label="search ", color="blue")
    plot2.set_title("Risultati per Search implementata con ABR")
    plot2.set_ylabel("tempo impiegato (secondi)")
    plot2.set_xlabel("dimensione albero in numero di nodi")
    plt.show()
    return testSearchAverageTimes



if __name__ == '__main__':
   #dimensione massima della lista su cui si fanno le operazioni
   dimMax = 50000
   #numero di volte in cui si fa la stessa operazione (insert,delete o search) per una lista di una certa dimensione n
   numPerDim = 100000
   #incremento dimensione struttura dati per ogni ciclo esterno delle funzioni dei test
   dimIncrement = 350

   #test per operazioni di dizionario implementate con Lista Concatenata GraphA
               #testInsertListConcGraphA(dimMax,numPerDim)
               #testSearchListConcGraphA(dimMax, numPerDim)
               #testDeleteListConcGraphA(dimMax,numPerDim)

   #test per operazioni di dizionario implementate con Lista Concatenata GraphB
               #testInsertListConcGraphB(dimMax, numPerDim, dimIncrement)
               #testSearchListConcGraphB(dimMax ,numPerDim, dimIncrement)
               #testDeleteListConcGraphB(dimMax, numPerDim, dimIncrement)

   #----------------------------------------------------------------------------#

   #test per operazioni di dizionario implementate con ABR GraphA
   testInsertABRGraphA(dimMax, numPerDim, dimIncrement)
   testSearchABRGraphB(dimMax, numPerDim)

   #test per operazioni di dizionario implementate con ABR GraphB
   testInsertABRGraphA(dimMax, numPerDim)
   testSearchABRGraphB(dimMax, numPerDim, dimIncrement)
