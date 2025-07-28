import tkinter as tk
from forms.add_consultant import add_consultant_form

def open_admin_panel():
    """View admin panel when user login as admin."""
    admin = tk.Tk()
    admin.title("پنل ادمین")
    admin.geometry("400x300")

    tk.Label(admin, text="به پنل مدیریت خوش آمدید", font=("Arial", 14)).pack(pady=20)

    tk.Button(admin, text="افزودن مشاور", width=20, command=add_consultant_form).pack(pady=10)
    tk.Button(admin, text="مشاهده نوبت‌ها", width=20).pack(pady=10)
    tk.Button(admin, text="خروج", width=20, command=admin.quit).pack(pady=10)

    admin.mainloop()
