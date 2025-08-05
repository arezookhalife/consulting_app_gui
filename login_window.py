import tkinter as tk
from tkinter import messagebox
from logic.auth import check_login
from panels import open_admin_panel, open_user_panel
import datetime


def create_login_window():
    """Create a simple login window using Tkinter."""
    
    
    def attempt_login():
        """Check user credentials and handle login result."""

        # Get entered username and password.
        username = entry_username.get()
        password = entry_password.get()
        user= check_login(username, password)
        if user:
            with open("log.txt", "a") as f:
                f.write(str(datetime.datetime.today()) + " | " + username+"\n")  # Record successful login to log.txt.
            root.destroy()  # Close window
            if user["role"]=="admin":
                open_admin_panel() # Go to admin panel
            elif user["role"]=="user":
                open_user_panel() # Go to user panel
        else:
            messagebox.showerror("خطا", "نام کاربری یا رمز عبور اشتباه است")


    # Create the main window and set window size.
    root = tk.Tk()
    root.title("ورود به سیستم")
    root.geometry("350x200")
    root.config(bg="lightblue")

    # Username label and entry
    tk.Label(root, text=":نام کاربری", bg="lightblue").place(x=220,y=50)
    entry_username = tk.Entry(root)
    entry_username.place(x=90,y=50)

    # Password label and entry (with masking)
    tk.Label(root, text=":رمز عبور", bg="lightblue").place(x=220,y=90)
    entry_password = tk.Entry(root, show="*")
    entry_password.place(x=90,y=90)

    # Login and exit button
    tk.Button(root, text="ورود",bg='green', fg="white", command=attempt_login).place(x=180,y=135)
    tk.Button(root, text="خروج",bg='red', fg="white", command=root.quit).place(x=140,y=135)

    # Start the GUI event loop
    root.mainloop()

