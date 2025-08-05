from logic.utils import load_file

USERS_FILE= "data/users.json"


def check_login(username, password):
    
    users = load_file(USERS_FILE)
    if any(user["username"] == username and user["password"] == password for user in users):
        return next(user for user in users if user["username"] == username and user["password"] == password)
    else:
        return False
