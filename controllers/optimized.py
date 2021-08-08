from typing import List
from controllers.strategy import Strategy
from models.portfolio import Portfolio
from models.combination import Combination


class Optimized(Strategy):

    def __init__(self, portfolio: Portfolio, max_cost: float):
        super().__init__(portfolio=portfolio)
        self.max_cost = max_cost

    def run(self,) -> List:
        """ Method that generates the best combination of a shares portfolio
            with GK algo
        """
        super().run()
        spent_money = 0
        list_share = []
        actions_list = self.data["portfolio"].actions_list
        sorted_portfolio = sorted(
                            actions_list,
                            key=lambda share: float(share.benefits),
                            reverse=True)
        for share in sorted_portfolio:
            if spent_money + share.cost <= self.max_cost:
                list_share.append(share)
                spent_money += share.cost
        one_comb = Combination(list_share)
        print(f"Meilleure combinaison :{one_comb}")
        self.stop()
        return one_comb
