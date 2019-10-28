import random
import math
import numpy

class A:
    def __init__(self):
        self.matriz = []
        self.gerar_matriz()
        self.fitness()

    def gerar_matriz(self):
        for i in range(20):
            linha = []
            for j in range(20):
                numero = self.gerar_numero(linha)
                linha.append(numero)
            self.matriz.append(linha)


    def gerar_numero(self, linha):
        numero = random.randint(1, 20)
        if(numero not in linha):
            return numero
        return self.gerar_numero(linha)

    def fitness(self):
        matriz_distancia = []
        for i in range(len(self.matriz)):
            linha = []
            for j in range(len(self.matriz)):

                x = random.uniform(0, 1)
                y = random.uniform(0, 1)
                interno = Interno(x, y)
                linha.append(interno)
            matriz_distancia.append(linha)

        copia = []
        copia_distancia = []
        for i in range(len(self.matriz)):
            copia.append(self.matriz[i][0])
            copia_distancia.append(matriz_distancia[i][0])

        vetor_lista = []
        for i in range(len(self.matriz)):
            soma = 0
            for j in range(len(self.matriz)):
                atual = matriz_distancia[i][j]
                if(j + 1 == len(matriz_distancia)):
                    proximo = copia_distancia[i]
                else:
                    proximo = matriz_distancia[i][j + 1]
                distancia = math.sqrt(math.pow(proximo.x - atual.x, 2) + math.pow(proximo.y - atual.y, 2))
                soma = soma + distancia
            vetor_lista.append(soma)
            self.matriz[i].append(soma)
            

        matriz_numpy = numpy.asarray(self.matriz)
        mat_sort = matriz_numpy[matriz_numpy[:,20].argsort()[::-1]]
        self.matriz = mat_sort.tolist()
        for i in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                self.matriz[i][j] = int(self.matriz[i][j])

        for i in range(len(self.matriz)):
            self.matriz[i].pop()

        print(self.matriz)
        vetor_lista.sort(reverse=True)
            
        nova_populacao = self.matriz[0:10]    
        vetor_lista = vetor_lista[0:10]    

        roleta = []
        indice = 1
        for i in range(9, -1, -1):
            for j in range(0, indice):
                roleta.append(i)

        
            
        

        # print(self.matriz)
        # print(copia)
        # print(matriz_distancia)
        # print(vetor_lista)


class Interno:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x} {self.y}"

    def __repr__(self):
        return str(self)


if __name__ == "__main__":
    a = A()
