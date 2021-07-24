from models.share import Share
import json


class Portfolio:
    """
    class that groups severals actions
    """

    def __init__(self):
        self.actions_list = []
        self.size = 0

    def serialize(self):
        action_list = []
        for elt in self.actions_list:
            action_list.append(elt.serialize())
        return action_list

    def load_from_json(self, name):
        with open(name) as f:
            data = json.load(f)
        for elt in data:
            self.actions_list.append(Share(**elt))

    def __iter__(self):
        self.size = 0
        return self

    def __next__(self):
        self.size += 1
        if self.size > len(self.actions_list):
            raise StopIteration()
        return self.actions_list[self.size-1]

    def __len__(self):
        return len(self.actions_list)

