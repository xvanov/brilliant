'''
Solution to brilliant problem: https://brilliant.org/daily-problems/tile-left-behind/
"Which Number Doesn't Belong?"
Math and Logic
7/19/20
1 hr 20 min
'''

from itertools import combinations

class Box:
    def __init__(self, t=list):
        self.t = t

class Problem:
    def __init__(self):
        default = [0,0]
        self.Farrah = Box(default)
        self.Kelly = Box(default)
        self.Letoya = Box(default)
        self.Michelle = Box(default)
        self.players = [self.Farrah, self.Letoya, self.Michelle, self.Kelly]
        self.numbers = [1,2,3,4,5,6,7,8,9]

    def go_thru_possibilities(self):
        combos = combinations(self.numbers, 2)
        for c in combos:
            self.Farrah = Box([c[0], c[1]])
            tmp_nums = self.numbers.copy()
            tmp_nums.remove(c[0])
            tmp_nums.remove(c[1])
            combos2 = combinations(tmp_nums, 2)
            for c2 in combos2:
                self.Kelly = Box([c2[0], c2[1]])
                tmp_nums2 = tmp_nums.copy()
                tmp_nums2.remove(c2[0])
                tmp_nums2.remove(c2[1])
                k_p = self._kelly_rule()
                if k_p:
                    combos3 = combinations(tmp_nums2, 2)
                    for c3 in combos3:
                        self.Letoya = Box([c3[0], c3[1]])
                        tmp_nums3 = tmp_nums2.copy()
                        tmp_nums3.remove(c3[0])
                        tmp_nums3.remove(c3[1])
                        l_p = self._letoya_rule()
                        if l_p:
                            combos4 = combinations(tmp_nums3, 2)
                            for c4 in combos4:
                                self.Michelle = Box([c4[0], c4[1]])
                                tmp_nums4 = tmp_nums3.copy()
                                tmp_nums4.remove(c4[0])
                                tmp_nums4.remove(c4[1])
                                passed = self.check_rules()
                                if passed:
                                    print(passed, c, c2, c3,c4)
                                    print('left', tmp_nums4)
    def combine(self, nums):
        combo = combinations(nums, 2)

    def check_rules(self):
        passed = True
        f_p = self._farrah_rule()
        k_p = self._kelly_rule()
        l_p = self._letoya_rule()
        m_p = self._michelle_rule()
        all_Ps = [f_p, k_p, l_p, m_p]
        if False in all_Ps:
            passed = False

        return passed

    def _farrah_rule(self):
        passed = True
        allNums = []
        players = [self.Farrah, self.Kelly, self.Letoya, self.Michelle]
        for p in players:
            allNums.append(p.t[0])
            allNums.append(p.t[1])
        if 0 in allNums:
            passed = False
        if 1 not in allNums:
            passed = False
        return passed

    def _kelly_rule(self):
        passed = False
        minF = min(self.Farrah.t)
        if self.Kelly.t[0] == minF**2 or  self.Kelly.t[1] == minF**2:
            passed = True
        return passed

    def _letoya_rule(self):
        passed = False
        prod = self.Kelly.t[0]*self.Kelly.t[1]
        dig1 = int(prod / 10)
        dig2 = prod % 10
        if self.Letoya.t[0] == dig1 and self.Letoya.t[1] == dig2:
            passed = True
        if self.Letoya.t[1] == dig1 and self.Letoya.t[0] == dig2:
            passed = True

        return passed

    def _michelle_rule(self):
        passed = False
        prod = self.Letoya.t[0]*self.Letoya.t[1]
        dig1 = int(prod / 10)
        dig2 = prod % 10
        if self.Michelle.t[0] == dig1 and self.Michelle.t[1] == dig2:
            passed = True
        if self.Michelle.t[1] == dig1 and self.Michelle.t[0] == dig2:
            passed = True
        return passed

if __name__ == '__main__':
    p = Problem()
    p.go_thru_possibilities()
