import time

def Prim(listaAdj):

    inicio =  time.time()

    s = 0

    custo = 0

    A = []

    dist = [1000000 for i in range (len(listaAdj))]
    pai = ['null' for i in range (len(listaAdj))]
    interligado = [False for i in range (len(listaAdj))]

    dist[s] = 0

    interligado[s] = True

    Q = [i for i in range(len(listaAdj))]
    Q.remove(s)

    for i in range(len(listaAdj[s])):
        if(dist[listaAdj[s][i][0]] > listaAdj[s][i][1]):
            dist[listaAdj[s][i][0]] = listaAdj[s][i][1]
            pai[listaAdj[s][i][0]] = s

    while (len(Q) != 0):

        min = 100000000
        u = -1

        for i in Q:
            if(dist[i] < min):
                u = i
                min = dist[i]
               
        Q.remove(u)
        interligado[u] = True

        for i in range (len(listaAdj[u])):
            if(dist[listaAdj[u][i][0]] > listaAdj[u][i][1]):
                dist[listaAdj[u][i][0]] = listaAdj[u][i][1]
                pai[listaAdj[u][i][0]] = u

        A.append((pai[u], u, dist[u]))
        custo += dist[u]

    print("Arvore geradora minima: " + str(A) + "\nCusto = " + str(custo))

    fim = time.time()
    print("Tempo de execucao: " + str(fim - inicio))

def Kruskal(arestas, vertices):
    inicio = time.time()

    A = []
    custo = 0
    C = [i for i in range (len(vertices))]

    arestas.sort(key = lambda tup: tup[2])

    for (u, v, w) in arestas:
        
        if(C[u] != C[v]):
            
            A.append((u,v,w))
            
            custo += w

            if(len(A) == len(vertices) - 1):
                break;

            k = C[u]

            for i in range(len(C)):
                if(C[i] == k):
                    C[i] = C[v]

    print("Arvore geradora minima: " + str(A))
    print("Custo: " + str(custo))

    fim = time.time()

    print("Tempo de execucao: " + str(fim - inicio))