import tkinter as tk
from tkinter import messagebox
from logic.consultants import save_consultant
from datetime import datetime
def add_consultant_form():
    """Create a form window to add a new consultant with input validation."""
    
    # Create a new top-level window.
    window = tk.Toplevel()
    window.title("افزودن مشاور جدید")
    window.geometry("400x300")
    window.config(bg="lightblue")
    
    # Field a labels &  # list of entry widgets.
    labels = ["نام مشاور", "تخصص", "شماره تماس", "ایمیل"]
    entries = []

    # Create label and entry for each field.
    y=10
    for label_text in labels:
        y=y+40
        tk.Label(window, text=label_text, bg="lightblue").place(x=250,y=y)
        entry = tk.Entry(window)
        entry.place(x=100,y=y)
        entries.append(entry)

    def submit():
        """Validate input fields and save consultant if all data is valid."""
        
        name, specialty, phone, email = [e.get().strip() for e in entries]
        time= str(datetime.today())
        
        
        # Ensure all fields are filled.                
        if not all([name, specialty, phone, email]):
            messagebox.showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
            return 
        
       # Validate phone number (digits only).
        if not phone.isdigit():
            messagebox.showerror("خطا", "شماره تماس معتبر وارد کنید")
            return 

        # Simple email format validation.
        if "@" not in email or "." not in email:
            messagebox.showerror("خطا", "ایمیل معتبر وارد کنید")
            return 

        # Save consultant data.
        save_consultant(name, specialty, phone, email, time)
        messagebox.showinfo("موفق", "مشاور با موفقیت ذخیره شد")
        window.destroy()

    # Submit button to trigger validation and saving.
    tk.Button(window, text="ذخیره مشاور", command=submit, bg="green", fg="white").place(x=200,y=220)

    # Cancel button to abort validation and data saving.
    tk.Button(window, text="لغو", command=window.destroy, bg="red", fg="white").place(x=150,y=220)