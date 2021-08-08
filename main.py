#from controllers.brute_force import BruteForce
from controllers.optimized import Optimized
from models.portfolio import Portfolio


def main():
    one_library = Portfolio()
    one_library.load_from_csv("dataset1.csv")
    library_two = Portfolio()
    library_two.load_from_csv("dataset2.csv")
    strategy_optimised_one = Optimized(one_library, 500.0)
    strategy_optimised_two = Optimized(library_two, 500.0)
    #strategy_brute_force = BruteForce(one_library, 500.0)
    strategy_optimised_one.run()
    strategy_optimised_two.run()
    #print(strategy_brute_force.run())


if __name__ == "__main__":
    main()
