import random

class Coin():
    def __init__(self, pT=0.5):
        self.pT = pT

    def flip(self):
        pT = self.pT
        i = random.random()
        if i >= pT:
            return 'H'
        else:
            return 'T'

class Coins():
    def __init__(self, N, T):
        self.allTosses = []
        for i in range(N):
            c = Coin()
            tosses = []
            for j in range(T):
                tosses.append(c.flip())
            self.allTosses.append(tosses)

    def run_sim(self):
        pass

    def coin_payout(self):
        superlist = self.allTosses
        flattened = [item for sublist in superlist for item in sublist ]
        payout = 0
        for i in range(1, len(flattened)):
            if flattened[i] == flattened[i-1] and flattened[i]== 'H':
                payout +=1
        return payout

if __name__ == '__main__':
    N = 10
    T = 1
    S = 10000
    payouts = []
    for i in range(S):
        coins = Coins(N,T)
        payout = coins.coin_payout()
        payouts.append(payout)

    expectedValue = sum(payouts)/len(payouts)
    print(expectedValue)
