import tkinter as tk
import json
from logic.consultants import search_consultant_by_name
from logic.appointments import appointments_count
from forms.edit_consultant import edit_consultant_form, delete_consultants

def view_consultants():
    """Open a window to display a list of consultants from a JSON file and search consultants by name."""
    appointments_count()

    try:
        with open("data/consultants.json", "r") as file:
            consultants = json.load(file)
    except FileNotFoundError:
        consultants = []    
        
    # Create main window.
    root = tk.Tk()
    root.title("مشاهده مشاوران")
    root.geometry("600x400")
        
    tk.Label(root, text="لیست مشاوران و نوبت‌ها", font=("Arial", 14)).pack(pady=20)
    tk.Label(root, text="جستجوی مشاور بر اساس نام").pack(pady=5)
    
    search_entry = tk.Entry(root) 
    search_entry.pack(pady=5)
    
    
    def display_results(results):
        
        # Clear previous results
        for widget in result_frame.winfo_children():
            widget.destroy()

        if not results:
            tk.Label(result_frame, text="هیچ مشاوری یافت نشد.").pack()
        else:
            tk.Label(result_frame, text="نام مشاور | تخصص | شماره تماس| تعداد نوبت ها").pack()
            for c in results:
                info = f"{c['name']} | {c['specialty']} | {c['phone']} | {c['appointments_count']}"
                tk.Label(result_frame, text=info).pack(pady=2)
                tk.Button(result_frame,text="ویرایش",command= lambda id= c['id']:edit_consultant_form(id)).pack()
                tk.Button(result_frame,text="حذف",command= lambda id= c['id']: delete_consultants(id)).pack()
                
    
    def on_search():  
        
        name = search_entry.get().strip()
        if name:
            results = search_consultant_by_name(name)
        else:
            results= consultants
        display_results(results)
    
    
    tk.Button(root, text="جستجو", command=on_search).pack(pady=5)
    
    
    result_frame = tk.Frame(root)
    result_frame.pack(pady=10)
    
    display_results(consultants)
      
    # Back button to close the window
    tk.Button(root, text="بازگشت", command= root.destroy).pack(pady=20)
    

    root.mainloop()

