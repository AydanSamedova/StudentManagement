import json
def getData(file):
   with open(file,"r") as connect:
       return json.load(connect)
data=getData("login.json")
print(data)

def prodactPrice(sifre):
 for i in data['users']:
    if i['password']==sifre:
        print(f"{i['name']},{i['surname']} ")

passw=input("Enter your password: ")
prodactPrice(passw)
