from enum import Enum


class Interests(Enum):
    dance = 0
    music = 1
    writing = 2
    design = 3
    photography = 4


class User:
    def __init__(self, idx):
        self.idx = idx
        self.likes = []
        self.dislikes = []

        self.clubs_subscribed = []

    def get_data(self):
        data = {"likes": self.likes, "dislikes": self.dislikes}
        return data
