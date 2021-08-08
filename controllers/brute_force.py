from itertools import combinations
from typing import List
from controllers.strategy import Strategy
from models.portfolio import Portfolio
from models.combination import Combination


class BruteForce(Strategy):

    def __init__(self, portfolio: Portfolio, max_cost: float):
        super().__init__(portfolio=portfolio)
        self.max_cost = max_cost

    def run(self) -> List:
        """ function that generates all combinations of a portfolio"""
        super().run()
        the_comb = Combination()
        for r in range(2, len(self.data['portfolio']) + 1):
            for e in combinations(self.data['portfolio'], r):
                one_comb = Combination(e)
                if (one_comb.cost <= self.max_cost and
                        one_comb.benefits > the_comb.benefits):
                    the_comb = one_comb
        self.stop()
        return the_comb
