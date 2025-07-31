import tkinter as tk
from tkinter import messagebox
import json

def add_appointment():
    def save_appointment():
        consultant_id = consultant_var.get()
        date = entry_date.get()
        time = entry_time.get()

        if not consultant_id or not date or not time:
            messagebox.showerror("خطا", "تمام فیلدها باید پر شوند!")
            return
        
        try:
            with open("data/appointments.json", "r") as file:
                appointments = json.load(file)
        except FileNotFoundError:
            appointments = []
            
            
        new_id= appointments[-1]["id"]+ 1 if appointments else 1
        new_appointment = {
            "id": new_id,
            "consultant_id": int(consultant_id),
            "date": date,
            "time": time
        }

        appointments.append(new_appointment)

        with open("data/appointments.json", "w") as file:
            json.dump(appointments, file, indent=4)

        messagebox.showinfo("موفقیت", "نوبت با موفقیت ثبت شد!")

    root = tk.Tk()
    root.title("ثبت نوبت")
    root.geometry("400x300")

    tk.Label(root, text="انتخاب مشاور:").pack(pady=5)

    try:
        with open("data/consultants.json", "r") as file:
            consultants = json.load(file)
    except FileNotFoundError:
        consultants = []

    consultant_var = tk.StringVar(root)

    for consultant in consultants:
        tk.Radiobutton(root, text=consultant['name'], value=consultant['id'], variable=consultant_var).pack()

    tk.Label(root, text="تاریخ نوبت:").pack(pady=5)
    entry_date = tk.Entry(root)
    entry_date.pack(pady=5)

    tk.Label(root, text="ساعت نوبت:").pack(pady=5)
    entry_time = tk.Entry(root)
    entry_time.pack(pady=5)

    tk.Button(root, text="ذخیره نوبت", command=save_appointment).pack(pady=20)
    tk.Button(root, text="بازگشت", command=root.destroy).pack()

    root.mainloop()
