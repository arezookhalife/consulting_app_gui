import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from logic.utils import load_file, save_file, validate_datetime

# File paths for data storage
APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"
       

def edit_appointment_form(id):
    """Create a form window to edit the selected appointment with validation."""

    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
    
    # Show error if there are no appointments to edit.
    if not appointments:
        messagebox.showerror("خطا", "نوبتی برای ویرایش وجود ندارد.")
    else:
        # Find the appointment with the matching ID.
        appointment =  next((a for a in appointments if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از ویرایش نوبت انتخابی اطمینان دارید؟")
        
        if result:
            # Create form window.
            window = tk.Toplevel()
            window.title("ویرایش نوبت")
            window.geometry("400x400")
            window.config(bg="lightblue")
            
            consultant_names = [c['name'] for c in consultants]
            consultant_id_to_name = {c['id']: c['name'] for c in consultants}
            consultant_name_to_id = {c['name']: c['id'] for c in consultants}

            # Consultant selection.
            tk.Label(window, text="نام مشاور:", bg="lightblue").place(x=250,y=50)
            consultant_var = tk.StringVar()
            consultant_dropdown = ttk.Combobox(window, textvariable=consultant_var, values=consultant_names, state="readonly")
            consultant_dropdown.set(consultant_id_to_name.get(appointment["consultant_id"], ""))
            consultant_dropdown.place(x=100,y=50)
            
            # Date entry.
            tk.Label(window, text="تاریخ نوبت:", bg="lightblue").place(x=250,y=90)
            entry_date = tk.Entry(window)
            entry_date.insert(0, appointment["date"])
            entry_date.place(x=100,y=90)

            # Time entry.
            tk.Label(window, text="ساعت نوبت:", bg="lightblue").place(x=250,y=130)
            entry_time = tk.Entry(window)
            entry_time.insert(0, appointment["time"])
            entry_time.place(x=100,y=130)
            
               
            def submit():
                """Validate and save edited appointment if all inputs are valid."""
                
                name = consultant_var.get().strip()
                date_input = entry_date.get().strip()
                time_input = entry_time.get().strip()
                consultant_id = consultant_name_to_id.get(name)

                if consultant_id is None:
                    messagebox.showerror("خطا", "نوبت انتخاب‌شده معتبر نیست.")
                elif not all([name, date_input, time_input]):
                    messagebox.showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
                    return 
                else:
                    # Validate date and time.
                    valid_datetime = validate_datetime(date_input,time_input)

                    if valid_datetime=="true":
                        new_appointment = {
                        "id": appointment['id'],
                        "consultant_id": int(consultant_id),
                        "date": date_input,
                        "time": time_input
                    }
                        
                        # Replace old appointment with updated one.
                        appointments.remove(appointment)
                        appointments.insert((id-1),new_appointment)
                        save_file(appointments,APPOINTMENTS_FILE)
                        messagebox.showinfo("موفق", "نوبت با موفقیت ویرایش شد")
                        window.destroy()
                    elif valid_datetime=="false":
                        messagebox.showerror("خطا", "امکان ثبت نوبت در تاریخ یا ساعت وارد شده وجود ندارد!")
                    elif valid_datetime=="error":
                        messagebox.showerror("خطا", "فرمت تاریخ یا ساعت وارد شده صحیح نیست!")


            # Buttons.
            tk.Button(window, text="ویرایش نوبت", command=submit, bg="green", fg="white").place(x=200,y=170)
            tk.Button(window, text="لغو", command=window.destroy, bg="red", fg="white").place(x=150,y=170)
            

def delete_appointments(id):
    """Delete the appointment with the given ID after user confirmation."""

    appointments = load_file(APPOINTMENTS_FILE)
    
    if not appointments:
        messagebox.showerror("خطا", "نوبتی برای حذف وجود ندارد.") 
    else:
        appointment =  next((a for a in appointments if a["id"] == id), None)
        result= messagebox.askokcancel("اخطار","آیا از حذف نوبت انتخابی اطمینان دارید؟")
        if result:
            # Remove the selected appointment.
            appointments.remove(appointment)                
            save_file(appointments,APPOINTMENTS_FILE)            
            messagebox.showinfo("موفق", "نوبت با موفقیت حذف شد")



