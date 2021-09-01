from random import randint

class Problem():
    def __init__(self, url, draws, fish):
        self.url = url
        self.draws = draws
        self.fish = fish

    def ana_solve(self):
        solution = 0
        solution = self.fish*((self.fish-1)/self.fish)**self.draws
        print('analytical solution = ', solution)

    def sim_solve(self):
        solution = 0
        Nsims = 10000
        nfish = []
        for n in range(Nsims):
            simdraws = []
            for i in range(draws):
                newfish = randint(1,fish)
                if newfish not in simdraws:
                    simdraws.append(newfish)
            nfish.append(len(simdraws))
        solution = fish - sum(nfish)/Nsims
        print('simulation solution = ', solution)

    def prg_solve(self):
        solution = 0
        print('programmatic solution = ', solution)

if __name__ == '__main__':
    url = 'https://brilliant.org/daily-problems/fish-aquarium/'
    # define problem inputs
    draws = 7
    fish = 10
    p = Problem(url, draws, fish)
    p.ana_solve()
    p.sim_solve()
    p.prg_solve()


