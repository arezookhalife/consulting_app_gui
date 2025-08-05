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
    admin.config(bg="lightblue")
    tk.Label(admin, text="به پنل مدیریت خوش آمدید", font=("Arial", 12, "bold"),bg="lightblue").pack(pady=20)

    tk.Button(admin, text="افزودن مشاور", width=20, command=add_consultant_form,bg="blue",fg="white").pack(pady=8)
    tk.Button(admin, text="مشاهده لیست مشاوران", width=20, command=lambda :view_consultants("admin"),bg="blue",fg="white").pack(pady=8)
    tk.Button(admin, text="ثبت نوبت", width=20, command=add_appointment,bg="blue",fg="white").pack(pady=8)
    tk.Button(admin, text=" مشاهده نوبت ها", width=20, command=lambda :view_appointments("admin"),bg="blue",fg="white").pack(pady=8)
    tk.Button(admin, text="خروج", width=20, command=admin.destroy,bg="red", fg="white").pack(pady=8)

    admin.mainloop()


def open_user_panel():
    """View admin panel when user login as admin."""
    
    admin = tk.Tk()
    admin.title("پنل کاربر")
    admin.geometry("400x300")
    admin.config(bg="lightblue")
    tk.Label(admin, text="به پنل کاربری خود خوش آمدید", font=("Arial", 12, "bold"),bg="lightblue").pack(pady=20)

    tk.Button(admin, text="مشاهده لیست مشاوران", width=20, command=lambda :view_consultants("user"),bg="blue",fg="white").pack(pady=8)
    tk.Button(admin, text=" مشاهده نوبت ها", width=20, command=lambda :view_appointments("user"),bg="blue",fg="white").pack(pady=8)
    tk.Button(admin, text="خروج", width=20, command=admin.destroy,bg="red", fg="white").pack(pady=8)

    admin.mainloop()

