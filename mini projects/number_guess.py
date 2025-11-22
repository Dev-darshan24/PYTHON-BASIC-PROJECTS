import random
from rich import print
s = "== Welcome to Number Guessing Game =="
print("[underline green]{:^60}[/underline green]".format(s))

n= random.randint(1,100)
a=-1
guesses =1

while(a != n):
    a = int(input("Guess the number:"))
    if(a>n):
        print("Lower number please!")
        guesses += 1
    elif(a<n):
        print("Higher number please!")
        guesses += 1

print(f"[yellow]You have guessed the number[/yellow] {n} [yellow]correctly in[/yellow] {guesses} [yellow]attempt.[/yellow]")