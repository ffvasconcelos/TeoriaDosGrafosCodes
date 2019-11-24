import time

def submenuCaminhoMinimo(listaAdj, matAdj, vertices, arestas):

    op = input("Escolha o algoritmo a ser utilizado:\n"+
               "1- Dijkstra\n"+
               "2- Bellman-Ford\n"+
               "3- Floyd-Warshall\n")

    if(op == "1"):
        s = int(input("Origem: "))
        f = int(input("Destino: "))
        print("Processando...")
        Dijkstra(listaAdj, s, f)
    elif(op == "2"):
        s = int(input("Origem: "))
        f = int(input("Destino: "))
        print("Processando...")
        Bellman_Ford(vertices, arestas, s, f)
    elif(op == "3"):
        s = int(input("Origem: "))
        f = int(input("Destino: "))
        print("Processando...")
        Floyd_Warshall(matAdj, s, f)

def Caminho(pred, dist, s, f):

    caminho = []
    custo = 0
    
    caminho.append(f)
    
    erro = 0

    custo = dist[f]

    while(f != s):

        if(pred[f] == 'null'):
            break
            erro = 1

        caminho.insert(0, pred[f])
        f = pred[f]
    
    if(erro == 1):
        print("Nao existe caminho possivel entre " + str(s) + " e " + str(f))
    else:
        print("Caminho: " + str(caminho))
        print("Custo: " + str(custo))
        
def CaminhoMatriz(pred, dist, s, e):
    
    caminho = []
    caminho.append(e)
    custo = dist[s][e]

    while(s != e or pred[s][e] == 'null'):
        e = pred[s][e]
        caminho.insert(0, e)

    if(pred[s][e] == 'null'):
        print("Nao existe caminho possivel entre " + str(s) + " e " + str(e))
    else:
        print("Caminho: " + str(caminho))
        print("Custo: " + str(custo))

def Dijkstra(listaAdj, s, f):

    inicio = time.time()

    dist = [100000 for x in range (len(listaAdj))]
    pred = ['null' for x in range (len(listaAdj))]
    naoProcessados = [i for i in range(len(listaAdj))]

    dist[s] = 0


    while(len(naoProcessados) != 0):
        
        min = 1000000

        #buscar minimo
        for i in range(len(naoProcessados)):
            if(min > dist[naoProcessados[i]]):
                min = dist[naoProcessados[i]]
                u = naoProcessados[i]
                x = i

        naoProcessados.pop(x)

        for i in range(len(listaAdj[u])):
            if(dist[listaAdj[u][i][0]] > dist[u] + listaAdj[u][i][1]):
                dist[listaAdj[u][i][0]] = dist[u] + listaAdj[u][i][1]
                pred[listaAdj[u][i][0]] = u

    fim = time.time()

    Caminho(pred, dist, s, f)
    
    print("Tempo de execucao: %.4fs"%(fim - inicio))

def Bellman_Ford(vertices, arestas, s, e):

    inicio = time.time()

    dist = [10000 for i in range(len(vertices))]
    pred = ['null' for i in range(len(vertices))]

    dist[s] = 0

    for i in range (len(vertices)):
        for j in arestas:
            if (dist[j[1]] > dist[j[0]] + j[2]):
                dist[j[1]] = dist[j[0]] + j[2]
                pred[j[1]] = j[0]

    neg = True
    
    for j in arestas:
        if(dist[j[1]] > dist[j[0]] + j[2]):
            neg = False

    final = time.time()

    if(neg == True):
        Caminho(pred, dist, s, e)
    else:
        print("Nao e possivel encontrar caminho minimo")

    print("Tempo de execucao: %.4fs"%(final - inicio))

def Floyd_Warshall(matAdj, s, f):

    inicio = time.time()

    dist = [[0 for i in range(len(matAdj[0]))] for i in range(len(matAdj[0]))]
    pred = [[0 for i in range(len(matAdj[0]))] for i in range(len(matAdj[0]))]


    for i in range(len(matAdj[0])):
        for j in range(len(matAdj[0])):
            if(i == j):
                dist[i][j] == 0
            elif(matAdj[i][j] != 0):
                dist[i][j] = matAdj[i][j]
                pred[i][j] = i
            else:
                dist[i][j] = 1000000
                pred[i][j] = 'null'

    for k in range(len(matAdj[0])):
        for i in range(len(matAdj[0])):
            for j in range(len(matAdj[0])):
                if(dist[i][j] > dist[i][k] + dist[k][j]):
                    dist[i][j] = dist[i][k] + dist[k][j]
                    pred[i][j] = pred[k][j]
    
    fim = time.time()

    CaminhoMatriz(pred, dist, s, f)

    print("Tempo de execucao: %.4fs"%(fim - inicio))