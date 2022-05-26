import random
import sys


class Numeros:
    def __init__(self):
        self.numeros = [[], [], [], [], []]
        for x in range(0, 5):
            for y in range(x * 15 + 1, (x + 1) * 15 + 1):
                self.numeros[x].append(y)


class Cartela:
    def __init__(self, num, chave, b=5, i=5, n=5, g=5, o=5):
        self.pedrasmarcadas = 0
        self.cartela = [[], [], [], [], []]
        self.quantidade = [b, i, n, g, o]
        self.chave = chave
        for x in range(0, 5):
            self.cartela[x] = random.sample(num.numeros[x], self.quantidade[x])
            self.cartela[x].sort()
    def __eq__(self, other):
        return (self.cartela == other.cartela)
    def __str__(self):
        return ("Cartela %s" % (self.chave))

    def exibeCartela(self):
        print("=" * 3 * 5)
        print("Cartela %s" % (self.chave))
        print("=" * 3 * 5)
        print("%3s%3s%3s%3s%3s" % ("B", "I", "N", "G", "O"))
        for x in range(0, 5):
            print("%3d%3d%3d%3d%3d" % (self.cartela[0][x], self.cartela[1][x], \
                                 self.cartela[2][x], self.cartela[3][x], self.cartela[4][x]))
        print("=" * 3 * 5)

    def existePedra(self, pedra):
        col = pedra / 15
        if pedra % 15 == 0:
            col = col - 1
        return ([x for x in self.cartela[col] if pedra == x])


class Bingo:
    def __init__(self):
        self.cartelas = []
        self.restantes = range(1, 76)
        self.pedras = Numeros()

    def removeNumerodosrestantes(self, numero):
        self.restantes = filter(lambda arg: arg != numero, self.restantes)

        # Verificando quais cartelas possuem o numero removido para incrementar
        # o numero de pedras marcadas nas cartelas
        for cartela in self.cartelas:
            if cartela.existePedra(numero):
                cartela.pedrasmarcadas += 1

    def adicionaCartela(self, cartela):
        self.cartelas.append(self.confereCartela(cartela))

    def confereCartela(self, comparar):
        for x in self.cartelas:
            #               if x.cartela == comparar.cartela:
            # Agora usando a implementação de igualdade __eq__ da classe Cartela
            if x == comparar:
                comparar = self.confereCartela(Cartela(self.pedras, comparar.chave))
                break
        return (comparar)

    def sorteaPedra(self):
        return (random.choice(self.restantes))


def inicio():
    b = Bingo()
    for x in range(0, 100):
        b.adicionaCartela(Cartela(b.pedras, x + 1))
        print (b.cartelas[x])

    print
    b.cartelas[0]
    falsa = b.cartelas[0]
    falsa.chave = "Falsa"
    falsa.exibeCartela()
    b.adicionaCartela(falsa)
    b.cartelas[x + 1].exibeCartela()
    b.cartelas[0].exibeCartela()

    while b.restantes:
        pedrasorteada = b.sorteaPedra()
        print(pedrasorteada)
        b.removeNumerodosrestantes(pedrasorteada)
        for cartela in b.cartelas:
            if cartela.pedrasmarcadas == 25:
                print
                print("BATEU")
                print("Faltavam %d" % (len(b.restantes)))
                print(b.restantes)
                cartela.exibeCartela()
                sys.exit()


if __name__ == '__main__':
    inicio()