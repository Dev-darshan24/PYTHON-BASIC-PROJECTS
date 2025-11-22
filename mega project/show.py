from data import load_data
from data import save_data

def show(st_id):
    user = load_data()

    detail = user[st_id]
    title = "Student Details:"
    
    print("{:^70}".format(title))

    for key, value in detail.items():
        print(f"{key} : {value}")