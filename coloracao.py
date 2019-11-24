import copy

def greedycol(listaAdj):

    S = [i for i in range(len(listaAdj))]
    Cores = [i for i in range(len(listaAdj))]

    for u in range(len(listaAdj)):
        CoresPossiveis = Cores.copy()
        for i in Cores:
            for v in range(len(listaAdj[u])):
                if(S[listaAdj[u][v][0]] == i and i in CoresPossiveis):
                    CoresPossiveis.remove(i)

        S[u] = CoresPossiveis[0]

    return S