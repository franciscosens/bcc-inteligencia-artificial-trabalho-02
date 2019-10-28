import random
import math
import numpy


class A:
    def __init__(self):
        self.matriz = []
        self.gerar_matriz()
        for i in range(10):
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

                x = random.uniform(0, 19)
                y = random.uniform(0, 19)
                interno = Interno(x, y)
                linha.append(interno)
            matriz_distancia.append(linha)

        copia = []
        copia_distancia = []
        for i in range(len(self.matriz)):
            copia.append(self.matriz[i][0])
            copia_distancia.append(matriz_distancia[i][0])

        for i in range(len(self.matriz)):
            soma = 0
            for j in range(len(self.matriz)):
                atual = matriz_distancia[i][j]
                if(j + 1 == len(matriz_distancia)):
                    proximo = copia_distancia[i]
                else:
                    proximo = matriz_distancia[i][j + 1]
                distancia = math.sqrt(
                    math.pow(proximo.x - atual.x, 2) + math.pow(proximo.y - atual.y, 2))
                soma = soma + distancia
            self.matriz[i].append(soma)

        matriz_numpy = numpy.asarray(self.matriz)
        mat_sort = matriz_numpy[matriz_numpy[:, 20].argsort()[::-1]]
        self.matriz = []
        for i in range(20):
            linha = []
            for j in range(20):
                linha.append(int(mat_sort[i][j]))
            self.matriz.append(linha)

        self.matriz = self.matriz[0:10]

        roleta = []
        indice = 1
        for i in range(9, -1, -1):
            for j in range(0, indice):
                roleta.append(i)

        indices_pais = self.gerar_indice_pais(roleta)
        indices_maes = self.gerar_indice_pais(roleta, indices_pais)
        pais = self.gerar_pais(indices_pais)
        maes = self.gerar_pais(indices_maes)
        indice_troca_aleatoria_anterior = 0
        for i in range(len(pais)):
            indice_troca_aleatoria = random.randint(0, 1)
            while indice_troca_aleatoria == indice_troca_aleatoria_anterior:
                indice_troca_aleatoria = random.randint(0, 1)
            indice_troca_aleatoria_anterior = indice_troca_aleatoria

            valor_pai = pais[i][indice_troca_aleatoria]
            valor_mae = maes[i][indice_troca_aleatoria]
            pais[i][indice_troca_aleatoria] = valor_mae
            maes[i][indice_troca_aleatoria] = valor_pai

        # detectar colisão
        pais_maes = self.detecatar_colisao(pais, maes)
        pais = pais_maes[0]
        maes = pais_maes[1]

        nova_polucacao = self.recombinacao(pais, maes)
        self.apresentar_matriz(self.matriz, '\t')
        for i in range(len(nova_polucacao)):
            self.matriz.append(nova_polucacao[i])
        self.apresentar_matriz(self.matriz, '\t')

    def recombinacao(self, pais, maes):
        nova_populacao = []
        for i in range(len(pais)):
            primeira_posicao = random.randint(0, 19)
            segunda_posicao = random.randint(0, 19)
            aux = pais[i][primeira_posicao]
            pais[i][primeira_posicao] = pais[i][segunda_posicao]
            pais[i][segunda_posicao] = aux
            nova_populacao.append(pais[i])

            primeira_posicao = random.randint(0, 19)
            segunda_posicao = random.randint(0, 19)
            aux = maes[i][primeira_posicao]
            maes[i][primeira_posicao] = maes[i][segunda_posicao]
            maes[i][segunda_posicao] = aux
            nova_populacao.append(maes[i])
        return nova_populacao

    def detecatar_colisao(self, pais, maes):
        for i in range(len(pais)):
            for j in range(len(pais)):
                for k in range(j + 1, len(pais)):
                    pai = pais[i][j]
                    mae = maes[i][j]
                    pai_proximo = pais[i][k]
                    mae_proximo = maes[i][k]
                    if pai == pai_proximo and mae == mae_proximo:
                        pais[i][j] = mae
                        maes[i][j] = pai
                        return self.detecatar_colisao(pais, maes)
        return [pais, maes]

    def apresentar_matriz(self, matriz, espaco=''):
        for i in range(len(matriz)):
            print(espaco, matriz[i])

    def apresentar_matriz_pais_maes(self, pais, maes, espaco=''):
        for i in range(len(pais)):
            print(espaco, pais[i])
            print(espaco, maes[i])

    def gerar_pais(self, indices):
        pais = []
        for i in range(len(indices)):
            indice = int(indices[i])
            pais.append(self.matriz[indice])
        return pais

    def gerar_indice_pais(self, roleta, pai=[]):
        elementos = []
        for i in range(0, 5):
            indice = self.obter_indice_atraves_roleta(roleta, elementos, pai)
            elementos.append(indice)
        return elementos

    def obter_indice_atraves_roleta(self, roleta, elementos, pai):
        indice_roleta = random.choice(roleta)
        if indice_roleta not in elementos and indice_roleta not in pai:
            return indice_roleta
        else:
            return self.obter_indice_atraves_roleta(roleta, elementos, pai)


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
