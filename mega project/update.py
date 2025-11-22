from data import load_data,save_data
from show import show

def update(st_id):
    user = load_data()


    detail = user[st_id]

    print("\n----- Update Your Details -----\n")
    print("What do you want to update?\n")

    # Display all keys
    keys = list(detail.keys())

    for i, key in enumerate(keys, start=1):
        print(f"{i}. {key}")

    try:
        choice = int(input("\nEnter field number to update: "))
        if choice < 1 or choice > len(keys):
            print("Invalid choice!")
            return
    except ValueError:
        print("Invalid input!")
        return

    field = keys[choice - 1]
    print(f"You selected: {field}")

    new_value = input(f"Enter new value for {field}: ")

    # Update the selected field
    user[st_id][field] = new_value

    save_data(user)
    show(st_id)
    print("\n[yellow]✔ Detail updated successfully![]yellow]")
