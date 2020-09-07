from class_login import *
from functions_login import *

print("""
==========================================================================
==========================================================================
=========================Welcome My Systems ==============================
==========================================================================
==========================================================================
0.Stop system! 
1.Login
2.Search "ov" in surnames 
3.Search e long name
4.Search password long more 8 symvols
5.Enter name and look at user's data
6.Look at users 
==========================================================================
==========================================================================
""")

while True:
    operation=int(input("Enter operation : "))
    if operation==0:
        print("Thanks")
        break
    elif operation==1:
         login()
         with open("login.json", "w") as elaqe:
               json.dump(database,elaqe)
    elif operation==2:
            withOvSearch()
    elif operation==3:
        longNameSearch()
    elif operation==4:
       pass8Search()
    elif operation==5:
        withNameSearch()
    elif operation==6:
          Data()
    else:
        print("Choose 1-6 operations please : ")




