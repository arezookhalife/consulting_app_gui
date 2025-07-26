import tkinter as tk
from tkinter import messagebox
from logic.auth import check_login
import json
import datetime

def create_login_window():
    """Create a simple login window using Tkinter."""
    
    def attempt_login():
        """Check user credentials and handle login result."""

        # Get entered username and password.
        username = entry_username.get()
        password = entry_password.get()
        if check_login(username, password):
            messagebox.showinfo("ورود موفق", "!عزیز خوش آمدید"+ username)
            root.destroy()  # Close window (or go to next panel)
        else:
            messagebox.showerror("خطا", "نام کاربری یا رمز عبور اشتباه است")


    # Create the main window and set window size.
    root = tk.Tk()
    root.title("ورود به سیستم")
    root.geometry("350x200")

    # Username label and entry
    tk.Label(root, text=":نام کاربری").place(x=220,y=50)
    entry_username = tk.Entry(root)
    entry_username.place(x=90,y=50)

    # Password label and entry (with masking)
    tk.Label(root, text=":رمز عبور").place(x=220,y=90)
    entry_password = tk.Entry(root, show="*")
    entry_password.place(x=90,y=90)

    # Login and exit button
    tk.Button(root, text="ورود",bg='green', command=attempt_login).place(x=180,y=135)
    tk.Button(root, text="خروج",bg='red', command=root.quit).place(x=140,y=135)

    # Start the GUI event loop
    root.mainloop()

