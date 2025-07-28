import json
import os

file_path = "data/consultants.json"

def save_consultant(name, specialty, phone, email, time):
    """Save a consultant's info to a JSON file."""
    
    # Create a dictionary for the consultant.
    consultant = {
        "name": name,
        "specialty": specialty,
        "phone": phone,
        "email": email,
        "time_submit": time
    }

    # If the file doesn't exist, create it with the consultant as the first entry.
    if not os.path.exists(file_path):
        with open(file_path, "w") as f:
            json.dump([consultant], f, indent=4)
            
    # If a file exists, read current data, add new consultant, and overwrite the file.   
    else:
        with open(file_path, "r+") as f:
            data = json.load(f)
            data.append(consultant)
            f.seek(0)
            json.dump(data, f, indent=4)
