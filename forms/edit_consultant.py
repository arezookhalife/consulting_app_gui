import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import json

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
        

def edit_consultant_form(id):
    """Create a form window to edit selected consultant with input validation."""

    consultants = load_file(CONSULTANTS_FILE)
    # If the file doesn't exist, create it with the consultant as the first entry.
    if not consultants:
        messagebox.showerror("خطا", "مشاوری برای ویرایش وجود ندارد.")
            
    # If a file exists, read current data, edit consultant, and overwrite the file.   
    else:
        # Find matched consultant.
        consultant =  next((a for a in consultants if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از ویرایش مشاور انتخابی اطمینان دارید؟")
        
        if result:
            # Create a new top-level window.
            window = tk.Toplevel()
            window.title("ویرایش مشاور ")
            window.geometry("400x400")

            # Field a labels &  # list of entry widgets.
            labels = ["نام مشاور", "تخصص", "شماره تماس", "ایمیل"]
            entries = [consultant["name"],consultant["specialty"],consultant["phone"],consultant["email"]]
            new_entries =[]
            
            # Create label and entry for each field.
            for label_text in labels:
                tk.Label(window, text=label_text).pack(pady=5)
                entry = tk.Entry(window)
                entry.pack()
                entry.insert(0, entries[labels.index(label_text)])  
                new_entries.append(entry)
                
            def submit():
                """Validate input fields and save consultant if all data is valid."""
                
                name, specialty, phone, email = [e.get().strip() for e in new_entries]
                time= str(datetime.today())
                
                
                # Ensure all fields are filled.                
                if not all([name, specialty, phone, email]):
                    messagebox.showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
                    return 
                
                # Validate phone number (digits only).
                if not phone.isdigit():
                    messagebox.showerror("خطا", "شماره تماس معتبر وارد کنید")
                    return 

                # Simple email format validation.
                if "@" not in email or "." not in email:
                    messagebox.showerror("خطا", "ایمیل معتبر وارد کنید")
                    return 

                # edit consultant data.
                new_consultant={
                    "id":consultant['id'],
                    "name": name,
                    "specialty": specialty,
                    "phone": phone,
                    "email": email,
                    "time_submit": time,
                    "appointments_count":consultant['appointments_count']
                }
                consultants.remove(consultant)
                consultants.insert((id-1),new_consultant)
                save_file(consultants,CONSULTANTS_FILE)
                messagebox.showinfo("موفق", "مشاور با موفقیت ویرایش شد")
                window.destroy()

            # Edit button to trigger validation and saving.
            tk.Button(window, text="ویرایش مشاور", command=submit).pack(pady=20)

            # Cancel button to abort validation and data saving.
            tk.Button(window, text="لغو", command=window.destroy).pack()
            

def delete_consultants(id):
    """This function delete selected consultant."""

    consultants = load_file(CONSULTANTS_FILE)
    
    # If the file doesn't exist, create it with the consultant as the first entry.
    if not consultants:
        messagebox.showerror("خطا", "مشاوری برای حذف وجود ندارد.")
            
    # If a file exists, read current data.   
    else:
        # Find matched consultant.
        consultant =  next((a for a in consultants if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از حذف مشاور انتخابی اطمینان دارید؟")
        if result:
            # Delete matched consultant.
            consultants.remove(consultant)                
            with open(CONSULTANTS_FILE, "w", encoding= "utf-8") as g:
                json.dump(consultants,g,ensure_ascii=False,indent=2)
            messagebox.showinfo("موفق", "مشاور با موفقیت حذف شد")



