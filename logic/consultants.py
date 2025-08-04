from logic.utils import load_file

# File path for consultants data
CONSULTANTS_FILE= "data/consultants.json"
       

def search_consultant_by_name(name):
    """This function searches consultant by name."""

    consultants=load_file(CONSULTANTS_FILE)
            
    # Find matched names.
    matched_names = [c["name"] for c in consultants if name.lower() in c["name"].lower()]
    consultants = [a for a in consultants if a["name"] in matched_names]
    return consultants      
            
