import json
def getData(file):
   with open(file,"r") as connect:
       return json.load(connect)
database=getData("login.json")


def getDataFromUser():
    sifre = input("Enter password :")
    for user in database['users']:
        if user['password']==sifre:
            database['users'].pop(database['users'].index(user))
    with open("login.json", "w") as connect:
            json.dump(database,connect)
getDataFromUser()
