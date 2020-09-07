import json
#dict classini yaratmaq
class dictGeneratior(dict):
    def _init_(self):
        self=dict()
    def addKeyValue(self,key,value):
     self[key]=value

database=dictGeneratior()
database.addKeyValue("users",[])
database["users"]=[]

#obyektin dictini yaratmaq
def createDict(_name, _surname,_password):
   inDict=dictGeneratior()
   inDict.addKeyValue("name",_name )
   inDict.addKeyValue("surname",_surname )
   inDict.addKeyValue("password",_password)
   return inDict
