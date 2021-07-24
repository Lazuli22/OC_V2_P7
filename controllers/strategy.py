import abc
import time


class Strategy(metaclass=abc.ABCMeta):

    def __init__(self, **kwargs):
        print(kwargs)
        self.data = kwargs
        self.start_time = None

    @abc.abstractmethod
    def run(self):
        """ general all possible combinations of a portfolio """
        self.start_time = time.time()

    def stop(self):
        elapsed_time = time.time() - self.start_time
        print(f"Temps écoulé : {elapsed_time} s")
