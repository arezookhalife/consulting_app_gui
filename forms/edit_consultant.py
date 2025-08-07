import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from logic.utils import load_file, save_file

# File path for consultants data
CONSULTANTS_FILE= "data/consultants.json"


def edit_consultant_form(id,root):
    """Create a form window to edit the selected consultant with input validation."""

    consultants = load_file(CONSULTANTS_FILE)
    
    if not consultants:
        messagebox.showerror("خطا", "مشاوری برای ویرایش وجود ندارد.")
    else:
        # Find the consultant with the matching ID.
        consultant =  next((a for a in consultants if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از ویرایش مشاور انتخابی اطمینان دارید؟")
        
        if result:
            # Create the edit form window.
            window = tk.Toplevel(root)
            window.title("ویرایش مشاور ")
            window.geometry("400x400")
            window.config(bg="lightblue")

            window_frame= tk.Frame(window)
            window_frame.config(width=400,height=400,bg="lightblue")
            window_frame.pack() 
    
            # Labels and corresponding values to populate fields.
            labels = ["نام مشاور", "تخصص", "شماره تماس", "ایمیل"]
            entries = [consultant["name"],consultant["specialty"],consultant["phone"],consultant["email"]]
            new_entries =[]
            
            # Create labels and prefilled entry fields.
            y=10
            for label_text in labels:
                y=y+40
                tk.Label(window_frame, text=label_text,bg="lightblue").place(x=250,y=y)
                entry = tk.Entry(window_frame)
                entry.place(x=100,y=y)
                entry.insert(0, entries[labels.index(label_text)])  
                new_entries.append(entry)
              
                
            def submit():
                """Validate input fields and save consultant if all data is valid."""
                
                name, specialty, phone, email = [e.get().strip() for e in new_entries]
                time= str(datetime.today())
                 
                # Validate non-empty fields.                
                if not all([name, specialty, phone, email]):
                    messagebox.showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
                    return 
                
                # Validate phone number (must be all digits).
                if not phone.isdigit():
                    messagebox.showerror("خطا", "شماره تماس معتبر وارد کنید")
                    return 

                # Basic email format check.
                if "@" not in email or "." not in email:
                    messagebox.showerror("خطا", "ایمیل معتبر وارد کنید")
                    return 

                # Update consultant data.
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

            # Buttons for submit and cancel.
            tk.Button(window_frame, text="ویرایش مشاور", command=submit, bg="green", fg="white").place(x=200,y=220)
            tk.Button(window_frame, text="لغو", command=window.destroy, bg="red", fg="white").place(x=150,y=220)
            root.wait_window(window)

def delete_consultants(id):
    """Delete the consultant with the given ID after user confirmation."""

    consultants = load_file(CONSULTANTS_FILE)
    
    if not consultants:
        messagebox.showerror("خطا", "مشاوری برای حذف وجود ندارد.")
    else:
        consultant =  next((a for a in consultants if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از حذف مشاور انتخابی اطمینان دارید؟")
        
        if result:
            consultants.remove(consultant)                
            save_file(consultants,CONSULTANTS_FILE)
            messagebox.showinfo("موفق", "مشاور با موفقیت حذف شد")



