from  class_login import *
from operations_login import *
#yeni oyuncu yaratmaq
def createUser():
    name_=input("Enter your name : ")
    surname_=input("Enter your surname: ")
    password_=input("Enter your password: ")
    database["users"].append(createDict(name_,surname_,password_))

#qeydiyatdan kecmek
def login():
     num=input("How many users ?")
     for i in range(int(num)):
         i+=1
         print(f" {i}-user login ")
         createUser()


#butun melumatlari gostermek
def Data():
    for x in database["users"]:
        print(x)


#ada gore axtaris
def withNameSearch():
    username= input("Enter user's name : ")
    for user in database["users"]:
         if user['name'] == username:
            print(f" Name: {user['name']} ,surname: {user['surname']},password: {user['password']}")


#ov-a gore axtaris etmek
def withOvSearch():
     for user in database["users"]:
         if "ov" in user['surname']:
          print(f"User's surname is  {user['surname']}")



#uzun adi tapmaq
def longNameSearch():
     longname = []
     longlen=[]
     for x in database['users']:
         l=len(x['name'])
         longlen.append(l)
         longname.append(x['name'])
     longlen.sort()
     for name in longname:
         if len(name) == longlen[-1]:
             print(f"long name  is {name}")

#8 reqemden uzun parolu axtarmaq
def pass8Search():
    for user in database['users']:
        if len(user['password'])>8:
         print(f" kod : {user['password']}")
