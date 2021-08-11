from typing import List
from models.share import Share
from terminaltables import AsciiTable


class Combination:

    def __init__(self, shares: List[Share] = None) -> None:

        """ unicité de la share"""
        self.shares = shares if shares else []
        self.cost = self.total_cost()
        self.benefits = self.total_benefits()

    def total_cost(self):
        return sum([float(share.cost) for share in self.shares])

    def total_benefits(self):
        return sum([float(share.benefits) for share in self.shares])

    @classmethod
    def __gt__(cls, a, b):
        return a.cost > b.cost

    def __repr__(self) -> str:
        """ function that represents a combination"""
        comp = [("Shares", "Cost", "Benefits")]
        for e in self.shares:
            comp.append([e.name,
                        e.cost,
                        e.benefits])
        table_instance = AsciiTable(comp, "Meilleure combinaison")
        print(table_instance.table)
        return (
            f"Cost of the Combination : {self.cost}, "
            f"Benefits of the Combination : {self.benefits} "
            "\n"
        )
