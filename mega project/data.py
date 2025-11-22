import json
file = "system.json"

def load_data():
    try:
        with open(file,"r") as f:
            return json.load(f)
        
    except FileNotFoundError:
        return {}
    
def save_data(user):
    with open(file,"w") as f:
        json.dump(user,f,indent=4)

