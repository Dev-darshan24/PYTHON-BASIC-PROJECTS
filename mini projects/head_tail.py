from random import choice
from rich import print


a = "Select Head or Tails"
print("[italic blue]{:^60}[/italic blue]".format(a))

you = input("Enter your Choice: ")
if("tail" in you.lower() or "head" in you.lower()):

    computer = choice(["Head","Tail"])
    

    a=computer

    print("[bold red]{:^60}[/bold red]".format(a))
    if a.lower() == you:
        print(f"You Select {you} \n You Win!")

    else: 
        print(f"You Select [underline yellow]{you}[/underline yellow] \n You Lose!")
        

else:
    print("Invalid Input....")
