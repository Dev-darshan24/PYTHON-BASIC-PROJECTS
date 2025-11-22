from data import load_data
from data import save_data
from rich import print


def detail(st_id):
    user = load_data()

    print("Fill all details below..\n")

    name = input("Enter your Name: ")
    age = input("Enter your Age: ")
    gamil = input("Enter your Gmail: ")
    branch = input("Enter your Branch: ")
    num = input("Enter your Number: ")
    cet = input("Enter your CET %: ")
    per12 = input("Enter your 12th %: ")
    per10 = input("Enter your 10th %: ")
    address = input("Enter your Address: ")
    taluka = input("Enter your Taluka: ")
    dist = input("Enter your District: ")
    state= input("Enter your State: ")

    user[st_id].update({
    "Name": name,
    "Age": age,
    "Gmail": gamil,
    "Branch": branch,
    "Number": num,
    "CET %": cet,
    "12th %": per12,
    "10th %": per10,
    "Address": address,
    "Taluka": taluka,
    "District": dist,
    "State": state
    })

    save_data(user)

    print("[green]Register Successfully![/green]")