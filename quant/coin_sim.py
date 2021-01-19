import random

class Coin():
    def __init__(self, t='fair'):
        pass

    def fair(self):
        i = random.random()
        if i >0.5:
            return 'H'
        else:
            return 'T'
    def unfair(self, pT):
        i = randpT
        if i >= pT:
            return 'H'
        else:
            return 'T'

class Coins():
    def __init__(self, N, T):
        allTosses = []
        for i in range(N):
            c = Coin()
            tosses = []
            for j in range(T):
                tosses.append(c.flip())
            self.allTosses = allTosses

    def run_sim(self):
        pass


if __name__ == '__main__':
    coins = Coins()

