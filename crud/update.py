import json

def getDataFromFile(_filename):
    with open(_filename, "r") as connect:
        return json.load(connect)

database = getDataFromFile("login.json")
def getDataFromUser():
    password =input("Enter password:")
    new_name=input("Enter new name :")
    for product in database['users']:
        if product['password']== password:
            product['name']=new_name
    with open("login.json", "w") as connect:
        json.dump(database,connect)
getDataFromUser()

