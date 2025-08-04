from logic.utils import load_file

USERS_FILE= "data/users.json"


def check_login(username, password):
    
    users = load_file(USERS_FILE)
    return any(user["username"] == username and user["password"] == password for user in users)
