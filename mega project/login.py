from data import load_data
from show import show   
from update import update   
from delete import delete
from rich import print

def log():
    user = load_data()

    st_id = input("Enter your Student ID: ")
    if st_id not in user:
        print("Student ID doesn't Exist !")
    else:
        pw = input("Enter password: ")
        if user[st_id]["Password"]==pw:
            print("Login Successfully !")
        else:
            print("Incorrect Password !")

        while True:   
            show(st_id)

            print("\n1. Update Details\n2. Logout\n3. Delete ID")
            ch = input("Select option: ")

            if ch == "1":
                update(st_id)

            elif ch == "2":
                print("[red]Logout Successfully ![/red]")
                return   
            elif ch == "3":
                delete(st_id)
                return
            else:
                print("Invalid Input")



