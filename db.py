import json

# File name where the database is stored
FILE_NAME = "./db.json"

data = {}


def load_data():
    # Load data from the JSON file into the global data dictionary.

    global data
    with open(FILE_NAME, "r") as file:
        data = json.load(file)


def write_data():
    # Write the current state of the global data dictionary back to the JSON file.

    with open(FILE_NAME, "w") as file:
        json.dump(data, file)


def add_user(username):
    # Add a new user to the database with default likes and dislikes.

    global data
    data[username] = {"likes": [1], "dislikes": []}

    write_data()


def get_likes_dislikes(username):
    # Retrieve the likes and dislikes of a user. If the user does not exist, add them to the database.

    if username not in data:
        add_user(username)

    return data[username]


def add_like(username, idx):
    # Add an event ID to the user's list of likes if it is not already present.

    global data
    if idx not in data[username]["likes"]:
        data[username]["likes"].append(idx)
    write_data()


def add_dislike(username, idx):
    # Add an event ID to the user's list of dislikes if it is not already present.

    global data
    if idx not in data[username]["dislikes"]:
        data[username]["dislikes"].append(idx)
    write_data()
