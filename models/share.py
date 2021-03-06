from models.seriable import Serializable


class Share(Serializable):
    """
        Class that represents an enterprise's action
    """
    def __init__(
            self,
            name,
            cost,
            percentage,
            benefits
            ):
        self.name = name
        self.cost = float(cost)
        self.percentage = float(percentage)
        self.benefits = float(benefits)

    def serialize(self):
        """
        function that serialize an object action.
        In output, the function gives a dict of data
        """
        return{
           "name": self.name,
           "cost": self.cost,         "percentage": self.percentage,
           "benefits": self.benefits
        }

    def __repr__(self) -> str:
        """ function that represents a share"""
        return (
            f"[{self.name}, {self.cost}, {self.benefits}]"
        )
