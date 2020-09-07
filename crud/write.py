import json
def getData(file):
   with open(file,"r") as connect:
       return json.load(connect)
database=getData("login.json")


def getDataFromUser():
    name =input("Enter name : ")
    surname = input("Enter surname :  ")
    sifre =input("Enter password : ")
    user={
        "name ":name,
        "surname": surname,
        "password":sifre,
    }
    database['users'].append(user)
    with open("login.json", "w") as connect:
          json.dump(database,connect)

getDataFromUser()
