from models.share import Share
import json
import csv


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

    def load_from_csv(self, name):
        f = open(name)
        myReader = csv.reader(f, delimiter=";")
        myReader.__next__()
        for row in myReader:
            if(float(row[1]) > 0.0):
                self.actions_list.append(
                    Share(row[0], row[1], row[2], row[3]))
        #print(self.actions_list)

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

