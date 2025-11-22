from login import log
from register import reg
from rich import print


greet = "[green ]Welcome to Student Section ![/green]"
print("{:^70}".format(greet))

while True:
    print("""
            1. Register
            2. Login
            3. Exit
          """)
    ch = input("Enter topic: ")
    if ch == "1":
        reg()

    elif ch == "2":
        log()

    elif ch == "3":
        print("Exit Successfully!")
        break 

    else:
        print("Invalid Input")