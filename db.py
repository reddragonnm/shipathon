import json
from user import User

DB_PATH = "./database.json"

data = {}


def load_data():
    global data

    with open(DB_PATH, "r") as file:
        data = json.load(file)


def write_data():
    with open(DB_PATH, "w") as file:
        json.dump(data, file, indent=4)


def save_user_data(user: User):
    global data
    data[user.idx] = user.get_data()
    write_data()
