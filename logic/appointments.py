from logic.utils import load_file, save_file


APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"
     
 
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

    
def search_appointment_by_consultant(name):
    """This function searches appointments list by consultant name."""
    
    consultants = load_file(CONSULTANTS_FILE)
    appointments= load_file(APPOINTMENTS_FILE)

    # Find matched IDs.
    matched_ids = [c["id"] for c in consultants if name.lower() in c["name"].lower()]

    if not matched_ids:
        return
    else:
        # Find matched appointments.
        results = [a for a in appointments if a["consultant_id"] in matched_ids]
        return results     
    
    
def search_appointments_by_date(date_input):
    """This function searches appointments list by date."""
    
    appointments = load_file(APPOINTMENTS_FILE)
    results = [a for a in appointments if a["date"] == date_input]
    return results
    
    
    