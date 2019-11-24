def densidade (vertices, arestas):
    
    densidade = len(arestas) / (len(vertices) * (len(vertices) - 1))

    return densidade

def complemento(matAdj):

    matComp = matAdj.copy()

    for i in range (len(matComp)):
        for j in range (len(matComp[i])):
            if(i != j):
                if (matComp[i][j] == 1):
                    matComp[i][j] = 0;
                else:
                    matComp[i][j] = 1;

    return matComp

def completo(matAdj):

    for i in range (len(matAdj)):
        for j in range(len(matAdj[i])):
            if(i != j):
                if(matAdj[i][j] == 0):
                    return False

    return True

def regular(matAdj):

    grauAnterior = -1

    for i in range(len(matAdj)):
        grau = 0
        for j in range(len(matAdj)):
            if matAdj[i][j] != 0:
                grau += 1
        if grauAnterior != -1 and grauAnterior != grau:
            return False

        grauAnterior = grau

    return True

