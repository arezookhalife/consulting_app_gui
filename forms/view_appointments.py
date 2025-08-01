import tkinter as tk
import json
from logic.appointments import appointments_count
from forms.edit_appointments import edit_appointment_form, delete_appointments

APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"

def load_file(file):
    """This function import/create list."""

    try:
        with open(file, "r", encoding= "utf-8") as g:
            return json.load(g)
    except FileNotFoundError:
        return [] 

        
def view_appointments():
    """Open a window to display a list of appointments from a JSON file ."""
    
    # Import consultants and appointments list.
    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
        
    # Create main window.
    root = tk.Tk()
    root.title("مشاهده نوبت ها")
    root.geometry("600x400")
        
    tk.Label(root, text="لیست نوبت‌ها", font=("Arial", 14)).pack(pady=20)
    
        
    consultant_map={c['id']:c['name'] for c in consultants}

    if not appointments:
        tk.Label(root, text="هیچ نوبتی یافت نشد.").pack()

    else:
        tk.Label(root, text="نام مشاور |تاریخ مشاوره| ساعت مشاوره").pack()
        for a in appointments:
            name = consultant_map.get(int(a['consultant_id']),"مشاور ناشناس")
            info = f"{name} | {a['date']} | {a['time']}"
            tk.Label(root, text=info).pack(pady=2)
            tk.Button(root,text="ویرایش",command= lambda id= a['id']:edit_appointment_form(id)).pack()
            tk.Button(root,text="حذف",command= lambda id= a['id']: delete_appointments(id)).pack()

    
   
    # Back button to close the window
    tk.Button(root, text="بازگشت", command= root.destroy).pack(pady=20)
    

    root.mainloop()

