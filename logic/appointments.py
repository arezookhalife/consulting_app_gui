import json

APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"

def load_file(file):
    """This function import/create list."""

    try:
        with open(file, "r", encoding= "utf-8") as g:
            return json.load(g)
    except FileNotFoundError:
        return [] 

def save_file(list,file):
    with open(file, "w", encoding= "utf-8") as g:
        json.dump(list,g,ensure_ascii=False,indent=2)
        
def appointments_count():
    """Returns the number of appointments of each consultant in the JSON file."""
    
      # Import consultants and appointments list.
    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
    new_list=[]
    for c in consultants:
        count=0
        consultant=c
        for a in appointments:
            
            if consultant["id"] == a["consultant_id"]:
                count=count+1
            else:
                continue
        consultant["appointments_count"]=count        
        new_list.append(consultant)
    
    save_file(new_list,CONSULTANTS_FILE)
    