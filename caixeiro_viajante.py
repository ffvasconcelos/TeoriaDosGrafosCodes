import time
import copy
import random

def Avalia(S, matAdj):
    custo = 0
    for i in range(len(S)-1):
        u = S[i]
        v = S[i + 1]

        custo += matAdj[u][v]
        
    return custo

def NearestNeighbor(listaAdj):

    s = time.time()
    
    NaoVisitados = [x for x in range(len(listaAdj))]
    u = 0
    S = []
    S.append(0)
    NaoVisitados.remove(u)

    while (len(NaoVisitados) != 0):

        min = 10000000

        for i in range(len(listaAdj[u])):
            if (listaAdj[u][i][1] <= min and listaAdj[u][i][0] in NaoVisitados):
                min = listaAdj[u][i][1]
                v = listaAdj[u][i][0]

        S.append(v)
        NaoVisitados.remove(v)

        u = v

    S.append(S[0])

    e = time.time()

    tempo = e - s

    return (S, tempo)

def twoOpt(S, listaAdj, matAdj, tempoDisponivel):

    s = time.time()

    random.seed()
    
    while(tempoDisponivel > 0):

        inicio = time.time()

        i1 = random.randint(1, len(S) - 2)
        i2 = random.randint(1, len(S) - 2)

        if(i1 != i2):

            Sc = S.copy()

            aux = Sc[i1]
            Sc[i1] = Sc[i2]
            Sc[i2] = aux

            if (Avalia(Sc, matAdj) < Avalia(S, matAdj)):
                S = Sc

        fim = time.time()

        tempoDisponivel -= (fim - inicio)

    e = time.time()

    tempo = e - s

    return (S, tempo)