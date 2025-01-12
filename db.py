import json

FILE_NAME = "./db.json"

data = {}


def load_data():
    global data
    with open(FILE_NAME, "r") as file:
        data = json.load(file)


def write_data():
    with open(FILE_NAME, "w") as file:
        json.dump(data, file)


def add_user(username):
    global data
    data[username] = {"likes": [1], "dislikes": []}

    write_data()


def get_likes_dislikes(username):
    if username not in data:
        add_user(username)

    return data[username]


def add_like(username, idx):
    global data
    if idx not in data[username]["likes"]:
        data[username]["likes"].append(idx)
    write_data()


def add_dislike(username, idx):
    global data
    if idx not in data[username]["dislikes"]:
        data[username]["dislikes"].append(idx)
    write_data()
