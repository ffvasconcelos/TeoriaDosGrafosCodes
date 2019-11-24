def buscaLargura(listaAdj, s):
    
    visitado = []
    fila = []

    for i in range(len(listaAdj)):
        visitado.append(0)

    visitado[s] = 1

    print("Busca por largura no vertice " + str(s) + ":")

    fila.append(s)
     
    while(len(fila) != 0):
        u = fila.pop(0)
        for i in range (len(listaAdj[u])):
            if(visitado[listaAdj[u][i][0]] == 0):
                visitado[listaAdj[u][i][0]] = 1
                print(str(listaAdj[u][i][0]))
                fila.append(listaAdj[u][i][0])


def buscaProfundidade(listaAdj, s):
    
    visitado = []
    pilha = []

    for i in range(len(listaAdj)):
        visitado.append(0)

    print("Busca por profundidade no vertice " + str(s) + ":")
    visitado[s] = 1

    pilha.append(s)

    while(len(pilha) != 0):
        u = pilha[-1]
        flag = False
        for i in listaAdj[u]:
            v = i[0]
            if(visitado[v] == 0):
                flag = True
                visitado[v] = 1
                print(str(v))
                pilha.append(v)
                break
        
        if(not flag):
            pilha.pop()



def buscaProfRec(listaAdj, u):
    global visitado

    visitado = [0 for x in range (len(listaAdj))]

    prof(listaAdj, u)


def prof(listaAdj, u):
    visitado[u] = 1
    print(str(u))

    for i in listaAdj[u]:
        v = i[0]
        if (visitado[v] == 0):
            prof(listaAdj, v)

def componentesConexas(listaAdj):
    global visitado

    visitado  = [0  for x in range(len(listaAdj))]

    marca = 0

    for i in range(len(listaAdj)):
        if(visitado[i] == 0):
            marca += 1
            profCon(listaAdj, i, marca)

def profCon(listaAdj, u, marca):

    visitado[u] = marca
    print(str(u) + "->" + str(marca))

    for j in listaAdj[u]:
        v = j[0]
        if(visitado[v] == 0):
            profCon(listaAdj, v, marca)

def ordTopologica(listaAdj):
    global visitado
    global ordem

    visitado = [0 for x in range(len(listaAdj))]
    ordem = []

    for i in range(len(listaAdj)):
        if (visitado[i] == 0):
            proford(listaAdj, i)
    print(ordem)

def proford(listaAdj, u):
    visitado[u] = 1

    for j in listaAdj[u]:

        v = j[0]

        if(visitado[v] == 0):
            proford(listaAdj, v)

    ordem.insert(0, u)
