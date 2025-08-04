import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logic.utils import load_file, save_file, validate_datetime


# File paths for data storage
APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"
      
        
def add_appointment():
    """Opens a window to add a new appointment."""
    
    
    def save_appointment():
        """Saves the appointment data to the appointments.json file if valid."""
        
        name = consultant_var.get().strip()
        consultant_id = consultant_name_to_id.get(name)
        date_input = entry_date.get()
        time_input = entry_time.get()

        # Check if all required fields are filled.
        if not consultant_id or not date_input or not time_input:
            messagebox.showerror("خطا", "تمام فیلدها باید پر شوند!")
            return
        else:
            # combine date and time inputs.
            valid_datetime = validate_datetime(date_input,time_input)
            
            # Check if the selected datetime is in the future.
            if valid_datetime=="true":
                appointments=load_file(APPOINTMENTS_FILE)
        
                # Generate a new unique ID.
                new_id= appointments[-1]["id"]+ 1 if appointments else 1
                new_appointment = {
                    "id": new_id,
                    "consultant_id": int(consultant_id),
                    "date": date_input,
                    "time": time_input
                }
                
                # Add the new appointment and save to file.
                appointments.append(new_appointment)
                save_file(appointments,APPOINTMENTS_FILE)
                messagebox.showinfo("موفقیت", "نوبت با موفقیت ثبت شد!")
            elif valid_datetime=="false":
                messagebox.showerror("خطا", "امکان ثبت نوبت در تاریخ یا ساعت وارد شده وجود ندارد!")
            elif valid_datetime=="error":
                # Invalid date/time format.
                messagebox.showerror("خطا", "فرمت تاریخ یا ساعت وارد شده صحیح نیست!")
        
                
    # Create new top-level window for appointment form.            
    root = tk.Toplevel()
    root.title("ثبت نوبت")
    root.geometry("400x300")
    root.config(bg="lightblue")
    
    # Consultant dropdown.
    tk.Label(root, text="انتخاب مشاور", bg="lightblue").place(x=250,y=50)

    consultants = load_file(CONSULTANTS_FILE)

    consultant_names = [c['name'] for c in consultants]
    consultant_name_to_id = {c['name']: c['id'] for c in consultants}
    consultant_var = tk.StringVar(root)

    ttk.Combobox(root, values=consultant_names, textvariable=consultant_var, state="readonly").place(x=100,y=50)
    
    # Date input.
    tk.Label(root, text="تاریخ نوبت", bg="lightblue").place(x=250,y=90)
    entry_date = tk.Entry(root)
    entry_date.place(x=100,y=90)

    # Time input.
    tk.Label(root, text="ساعت نوبت", bg="lightblue").place(x=250,y=130)
    entry_time = tk.Entry(root)
    entry_time.place(x=100,y=130)

    # Buttons for saving and canceling.
    tk.Button(root, text="ذخیره نوبت", command=save_appointment, bg="green", fg="white").place(x=200,y=170)
    tk.Button(root, text="بازگشت", command=root.destroy, bg="red", fg="white").place(x=150,y=170)

    root.mainloop()
