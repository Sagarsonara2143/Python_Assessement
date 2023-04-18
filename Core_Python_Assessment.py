import datetime
import re

'''
file = open("Assessment.txt","w")
file.write("Example")
file.close()

file = open("Assessment.txt","r")
print(file.read()) 
file.close()
'''

while True:
    print("\n\t\tPress 1 for generate Note")
    print("\t\tPress 2 for review Note")
    print("\t\tPress 4 for Exit\n")

    #choice = int(input("Enter your Choice : "))
    try:
        choice = int(input("Enter your Choice : "))
        print("\n-----------------------------------------------------------")
    except:
        print("Error : Invalid Input")
        continue
    
    if choice == 1:
        while True:
            e_generator=input("Enter Python E-Note Generator Name : ")
            if e_generator.isalpha() or "":
                e_title=input("Enter Python E-Note Title : ")
                e_content=input("Enter E-Note Content : ")
                break
            else:
                print("Error : Invalid Input")
                continue
                
        file = open("Assessment.txt","a")
        time=datetime.datetime.now()
        
        file.write(str(time))
        file.write("\nE-Note Title : ")
        file.write(e_title)
        file.write("\nE-Note Description : ")
        file.write(e_content)
        file.write("\n\t\tNote Generator : ")                
        file.write(e_generator)
        file.write("\n\n-----------------------------------------------------------\n")
        file.close()
        
    elif choice==2:
        file=open("Assessment.txt","r")
        #file.seek(0)
        print(file.read())
        file.close()

    elif choice == 4:
        print("Thank you for using our application")
        break

    else:
        print("Choice from above options")
        

