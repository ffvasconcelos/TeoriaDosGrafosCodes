import info
import busca
import caminho_minimo
import arvores_geradoras
import coloracao

#Leitura do arquivo fonte do grafo 

fileName = input("Arquivo do grafo: ")
file = open(fileName)
str = file.readline()
str = str.split(" ")

numVertices = int(str[0])
numArestas = int(str[1])

#Preenchimento das estruturas de dados
print("Processando grafo...")

listaAdj = [[] for x in range (numVertices)]
matAdj = [[0 for x in range (numVertices)] for x in range (numVertices)]
vertices = [x for x in range (numVertices)]
arestas = []

for i in range(numArestas):
    str = file.readline()
    str = str.split(" ")
    origem = int(str[0])
    destino = int(str[1])
    peso = int(str[2])
    listaAdj[origem].append((destino, peso))
    matAdj[origem][destino] = peso
    arestas.append((origem, destino, peso))

print("Grafo totalmente processado!")

#print(listaAdj)
#print(matAdj)

#Operacoes
op = input("Operacao: \n"
          + "1 Densidade \n" 
          + "2 Complemento \n" 
          + "3 Completo \n" 
          + "4 Regular \n" 
          + "5 Busca por largura \n" 
          + "6 Busca por profundidade \n" 
          + "7 Busca por profundidade recursiva\n" 
          + "8 Componteste conexas\n" 
          + "9 Ordem topologica\n"
          + "10 Caminho minimo\n"
          + "11 Algoritmo de Prim\n"
          + "12 Algoritmo de Kruskal\n"
          + "13 GreedyCol\n")

if(op == "1"):
    densidade = info.densidade(vertices, arestas)
    print("Densidade = %.2f" % densidade)
elif(op == "2"):
    print(info.complemento(matAdj))
elif(op == "3"):
    print(info.completo(matAdj))
elif(op == "4"):
    print(info.regular(matAdj))
elif(op == "5"):
    v = int(input("Vertice de busca: "))
    busca.buscaLargura(listaAdj, v)
elif(op == "6"):
    v = int(input("Vertice de busca: "))
    busca.buscaProfundidade(listaAdj, v)
elif(op == "7"):
    v = int(input("Vertice de busca: "))
    busca.buscaProfRec(listaAdj, v)
elif(op == "8"):
    busca.componentesConexas(listaAdj)
elif(op == "9"):
    busca.ordTopologica(listaAdj)
elif(op == "10"):
    caminho_minimo.submenuCaminhoMinimo(listaAdj, matAdj, vertices, arestas)
elif(op == "11"):
    arvores_geradoras.Prim(listaAdj)
elif(op == "12"):
    arvores_geradoras.Kruskal(arestas, vertices)
elif(op == "13"):
    S = coloracao.greedycol(listaAdj)
    print(S)