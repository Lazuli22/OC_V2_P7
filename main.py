from controllers.brute_force import BruteForce
# from controllers.optimized import Optimized
from models.portfolio import Portfolio


def main():

    # Exemple de la force brute
    one_library = Portfolio()
    one_library.load_from_json("actions_library.json")
    strategy_brute_force = BruteForce(one_library, 500.0)
    print(strategy_brute_force.run())

    # Exemple de l'algo optimisé
    # one_library = Portfolio()
    # one_library.load_from_json("actions_library.json")
    # optimised_strategy = Optimized(one_library, 500.0)
    # optimised_strategy.run()

    # Exemples de comparaison avec les résultats SIENNA
    # one_library = Portfolio()
    # one_library.load_from_csv("dataset1.csv")
    # library_two = Portfolio()
    # library_two.load_from_csv("dataset2.csv")
    # strategy_optimised_one = Optimized(one_library, 500.0)
    # strategy_optimised_two = Optimized(library_two, 500.0)
    # strategy_optimised_one.run()
    # strategy_optimised_two.run()


if __name__ == "__main__":
    main()
