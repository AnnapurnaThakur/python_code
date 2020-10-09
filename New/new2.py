import json

def login(usr):
    uN = input("Name: ")
    pW = input("Password: ")

    if uN in usr.keys():
        if pW == usr[uN]:
            print("Welcome back.")
        else:
            print("Incorrect password.")
            return False
    else:
        print("Hello, new person.")
        usr[uN] = pW

    writeUsers(usr)
    return True

def readUsers():
    try:
        with open("users.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def writeUsers(usr):
    with open("users.json", "w+") as f:
            json.dump(usr, f)

users = readUsers()
success = login(users)

while not success:
    success = login(users)