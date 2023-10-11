def intro():
    print("Welcome to Lagra (TM)")


def validate_user(user_db, username, password):
    if username in user_db and user_db[username] == password:
        return True

    return False


def log_in(user_db):
    username = input("User: ")
    password = input("Password: ")

    if validate_user(user_db, username, password):
        return username

    return None

def list_items(user, items_db):
    print("These are your items\n")

    items = items_db[user]

    if items:
        print(*[f"{i+1}) {item}" for i, item in enumerate(items)], sep='\n')
    else:
        print("No items found")