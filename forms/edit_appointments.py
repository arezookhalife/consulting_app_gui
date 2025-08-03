import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime,date
import json


APPOINTMENTS_FILE= "data/appointments.json"
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
        

def edit_appointment_form(id):
    """Create a form window to edit selected appointment with input validation."""

    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
    
    # If the file doesn't exist, create it with the appointment as the first entry.
    if not appointments:
        messagebox.showerror("خطا", "نوبتی برای ویرایش وجود ندارد.")
            
    # If a file exists, read current data, edit appointment, and overwrite the file.   
    else:
        # Find matched appointment.
        appointment =  next((a for a in appointments if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از ویرایش نوبت انتخابی اطمینان دارید؟")
        
        if result:
            # Create a new top-level window.
            window = tk.Toplevel()
            window.title("ویرایش نوبت")
            window.geometry("400x400")
            window.config(bg="lightblue")
            
            consultant_names = [c['name'] for c in consultants]
            consultant_id_to_name = {c['id']: c['name'] for c in consultants}
            consultant_name_to_id = {c['name']: c['id'] for c in consultants}

            # Field a labels &  # list of entry widgets.
            tk.Label(window, text="نام مشاور:", bg="lightblue").place(x=250,y=50)
            consultant_var = tk.StringVar()
            consultant_dropdown = ttk.Combobox(window, textvariable=consultant_var, values=consultant_names, state="readonly")
            consultant_dropdown.set(consultant_id_to_name.get(appointment["consultant_id"], ""))
            consultant_dropdown.place(x=100,y=50)
            
            tk.Label(window, text="تاریخ نوبت:", bg="lightblue").place(x=250,y=90)
            entry_date = tk.Entry(window)
            entry_date.insert(0, appointment["date"])
            entry_date.place(x=100,y=90)

            tk.Label(window, text="ساعت نوبت:", bg="lightblue").place(x=250,y=130)
            entry_time = tk.Entry(window)
            entry_time.insert(0, appointment["time"])
            entry_time.place(x=100,y=130)
            
            
               
            def submit():
                """Validate input fields and save appointment if all data is valid."""
                name = consultant_var.get().strip()
                date_input = entry_date.get().strip()
                time_input = entry_time.get().strip()
                consultant_id = consultant_name_to_id.get(name)

                if consultant_id is None:
                    messagebox.showerror("خطا", "نوبت انتخاب‌شده معتبر نیست.")
                    
                # Ensure all fields are filled.                
                elif not all([name, date_input, time_input]):
                    messagebox.showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
                    return 
                else:
                    # Validate date & time .
                    try:
                        input_date = datetime.strptime(date_input, "%Y-%m-%d").date()
                        input_time = datetime.strptime(time_input,"%H:%M").time()
                        input_datetime = datetime.combine(input_date, input_time)
                        if input_datetime > datetime.now():
                            new_appointment = {
                            "id": appointment['id'],
                            "consultant_id": int(consultant_id),
                            "date": date_input,
                            "time": time_input
                        }
                            appointments.remove(appointment)
                            appointments.insert((id-1),new_appointment)
                            save_file(appointments,APPOINTMENTS_FILE)
                            messagebox.showinfo("موفق", "نوبت با موفقیت ویرایش شد")
                            window.destroy()
                        else:
                            messagebox.showerror("خطا", "امکان ثبت نوبت در تاریخ یا ساعت وارد شده وجود ندارد!")
                    except ValueError:
                        messagebox.showerror("خطا", "فرمت تاریخ یا ساعت وارد شده صحیح نیست!")


            # Edit button to trigger validation and saving.
            tk.Button(window, text="ویرایش نوبت", command=submit, bg="green", fg="white").place(x=200,y=170)

            # Cancel button to abort validation and data saving.
            tk.Button(window, text="لغو", command=window.destroy, bg="red", fg="white").place(x=150,y=170)
            

def delete_appointments(id):
    """This function delete selected appointment."""

    appointments = load_file(APPOINTMENTS_FILE)
    
    # If the file doesn't exist, create it with the appointment as the first entry.
    if not appointments:
        messagebox.showerror("خطا", "نوبتی برای حذف وجود ندارد.")
            
    # If a file exists, read current data.   
    else:
        # Find matched appointment.
        appointment =  next((a for a in appointments if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از حذف نوبت انتخابی اطمینان دارید؟")
        if result:
            # Delete matched appointment.
            appointments.remove(appointment)                
            with open(APPOINTMENTS_FILE, "w", encoding= "utf-8") as g:
                json.dump(appointments,g,ensure_ascii=False,indent=2)
            messagebox.showinfo("موفق", "نوبت با موفقیت حذف شد")



