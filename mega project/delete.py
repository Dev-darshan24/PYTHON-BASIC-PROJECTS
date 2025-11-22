from data import load_data, save_data


def delete(st_id):
    user = load_data()
    confirm = input("Are you sure want to delete? (Yes/No): ")

    if confirm.lower() == "yes":
        del user[st_id]
        save_data(user)
        print("Delete Successfully!")
        return

    elif confirm.lower() == "no":
        print("Deletion Cancelled!")
        return
    
    else:
        print("Invalid Input")