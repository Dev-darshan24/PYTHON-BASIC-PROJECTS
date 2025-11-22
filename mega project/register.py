from data import load_data
from data import save_data
from detail import detail


def reg():
    user = load_data()

    st_id = input("Enter your Student ID: ")

    if st_id in user:
        print("Student Already Exist!")
        return
    pw = input("Enter a password: ")
    user[st_id]={"Password": pw}

    save_data(user)


    detail(st_id)

