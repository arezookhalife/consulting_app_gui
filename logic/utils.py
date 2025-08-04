import json
from datetime import datetime


def validate_datetime(date_str,time_str):
    """This function Check if date and time are in correct format and are in the future."""
    
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        input_time = datetime.strptime(time_str,"%H:%M").time()
        input_datetime = datetime.combine(input_date, input_time)

        if input_datetime > datetime.now():
            return "true"
        else:
            return "false"
    except ValueError:
        return "error"
    

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
   
            
