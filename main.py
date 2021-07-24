
from models.portfolio import Portfolio
from controllers.brute_force import BruteForce


def main():
    one_library = Portfolio()
    one_library.load_from_json("actions_library.json")
    one_strategy = BruteForce(one_library, 500)
    print(one_strategy.run())


if __name__ == "__main__":
    main()
