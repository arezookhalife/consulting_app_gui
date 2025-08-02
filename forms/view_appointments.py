import tkinter as tk
import json
from logic.appointments import search_appointment_by_consultant, search_appointments_by_date
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
    tk.Label(root, text="جستجوی نوبت ").pack(pady=5)
    tk.Label(root, text="بر اساس نام مشاور").pack(pady=5)
    consultant_entry = tk.Entry(root)
    consultant_entry.pack(pady=5)
   
    tk.Label(root, text="بر اساس تاریخ نوبت").pack(pady=5)
    date_entry = tk.Entry(root)
    date_entry.pack(pady=5)
    
    consultant_map={c['id']:c['name'] for c in consultants}

    def display_results(results):
           
        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        if not results:
            tk.Label(result_frame, text="هیچ نوبتی یافت نشد.").pack()
        else:
            tk.Label(result_frame, text="نام مشاور |تاریخ مشاوره| ساعت مشاوره").pack()
            for a in results:
                name = consultant_map.get(int(a['consultant_id']),"مشاور ناشناس")
                info = f"{name} | {a['date']} | {a['time']}"
                tk.Label(result_frame, text=info).pack(pady=2)
                tk.Button(result_frame,text="ویرایش",command= lambda id= a['id']:edit_appointment_form(id)).pack()
                tk.Button(result_frame,text="حذف",command= lambda id= a['id']: delete_appointments(id)).pack()


    def on_search():  
       
        consultant_input = consultant_entry.get().strip()
        date_input = date_entry.get().strip()
        if consultant_input:
            results = search_appointment_by_consultant(consultant_input)
        elif date_input:
            results= search_appointments_by_date(date_input)                
        else:
            results= appointments
        display_results(results)
   
   
    tk.Button(root, text="جستجو", command=on_search).pack(pady=5)

    result_frame = tk.Frame(root)
    result_frame.pack(pady=10)
   
    display_results(appointments)
   
    # Back button to close the window
    tk.Button(root, text="بازگشت", command= root.destroy).pack(pady=20)
   
    root.mainloop()

