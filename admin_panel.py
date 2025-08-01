import tkinter as tk
from forms.add_consultant import add_consultant_form
from forms.view_consultants import view_consultants
from forms.add_appointment import add_appointment
from forms.view_appointments import view_appointments

def open_admin_panel():
    """View admin panel when user login as admin."""
    admin = tk.Tk()
    admin.title("پنل ادمین")
    admin.geometry("400x300")

    tk.Label(admin, text="به پنل مدیریت خوش آمدید", font=("Arial", 14)).pack(pady=20)

    tk.Button(admin, text="افزودن مشاور", width=20, command=add_consultant_form).pack(pady=10)
    tk.Button(admin, text="مشاهده لیست مشاوران", width=20, command=view_consultants).pack(pady=10)
    tk.Button(admin, text="ثبت نوبت", width=20, command=add_appointment).pack(pady=10)
    tk.Button(admin, text=" مشاهده نوبت ها", width=20, command=view_appointments).pack(pady=10)
    tk.Button(admin, text="خروج", width=20, command=admin.destroy).pack(pady=10)

    admin.mainloop()

