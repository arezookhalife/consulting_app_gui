import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from datetime import datetime
import json

def add_appointment():
    def save_appointment():
        name = consultant_var.get().strip()
        consultant_id = consultant_name_to_id.get(name)
        date_input = entry_date.get()
        time_input = entry_time.get()


        if not consultant_id or not date_input or not time_input:
            messagebox.showerror("خطا", "تمام فیلدها باید پر شوند!")
            return
        else:
            try:
                input_date = datetime.strptime(date_input, "%Y-%m-%d").date()
                input_time = datetime.strptime(time_input,"%H:%M").time()
                input_datetime = datetime.combine(input_date, input_time)
                if input_datetime > datetime.now():
                    try:
                        with open("data/appointments.json", "r") as file:
                            appointments = json.load(file)
                    except FileNotFoundError:
                        appointments = []
            
            
                    new_id= appointments[-1]["id"]+ 1 if appointments else 1
                    new_appointment = {
                        "id": new_id,
                        "consultant_id": int(consultant_id),
                        "date": date_input,
                        "time": time_input
                    }

                    appointments.append(new_appointment)

                    with open("data/appointments.json", "w") as file:
                        json.dump(appointments, file, indent=4)

                    messagebox.showinfo("موفقیت", "نوبت با موفقیت ثبت شد!")
                else:
                    messagebox.showerror("خطا", "امکان ثبت نوبت در تاریخ یا ساعت وارد شده وجود ندارد!")
            except ValueError:
                messagebox.showerror("خطا", "فرمت تاریخ یا ساعت وارد شده صحیح نیست!")
                
            
    root = tk.Toplevel()
    root.title("ثبت نوبت")
    root.geometry("400x300")
    root.config(bg="lightblue")
    
    tk.Label(root, text="انتخاب مشاور", bg="lightblue").place(x=250,y=50)

    try:
        with open("data/consultants.json", "r") as file:
            consultants = json.load(file)
    except FileNotFoundError:
        consultants = []

    consultant_names = [c['name'] for c in consultants]
    consultant_name_to_id = {c['name']: c['id'] for c in consultants}
    consultant_var = tk.StringVar(root)

    ttk.Combobox(root, values=consultant_names, textvariable=consultant_var, state="readonly").place(x=100,y=50)

    tk.Label(root, text="تاریخ نوبت", bg="lightblue").place(x=250,y=90)
    entry_date = tk.Entry(root)
    entry_date.place(x=100,y=90)

    tk.Label(root, text="ساعت نوبت", bg="lightblue").place(x=250,y=130)
    entry_time = tk.Entry(root)
    entry_time.place(x=100,y=130)

    tk.Button(root, text="ذخیره نوبت", command=save_appointment, bg="green", fg="white").place(x=200,y=170)
    tk.Button(root, text="بازگشت", command=root.destroy, bg="red", fg="white").place(x=150,y=170)

    root.mainloop()
