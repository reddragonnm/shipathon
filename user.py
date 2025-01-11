from enum import Enum


class Clubs(Enum):
    PFC = ["Photography", "Films"]
    Design = ["Design"]
    Dance = ["Dance"]
    Music = ["Music"]


class User:
    def __init__(self, idx):
        self.idx = idx
        self.likes = []
        self.dislikes = []

    def get_data(self):
        data = {"likes": self.likes, "dislikes": self.dislikes}
        return data
