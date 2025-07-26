import json

def check_login(username, password):
    with open("data/users.json", "r") as f:
        users = json.load(f)
    return any(user["username"] == username and user["password"] == password for user in users)
