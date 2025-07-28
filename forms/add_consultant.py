import tkinter as tk
from tkinter import messagebox
from logic.consultants import save_consultant

def add_consultant_form():
    """Create a form window to add a new consultant with input validation."""
    
    # Create a new top-level window.
    window = tk.Toplevel()
    window.title("افزودن مشاور جدید")
    window.geometry("400x400")

    # Field a labels &  # list of entry widgets.
    labels = ["نام مشاور", "تخصص", "شماره تماس", "ایمیل"]
    entries = []

    # Create label and entry for each field.
    for label_text in labels:
        tk.Label(window, text=label_text).pack(pady=5)
        entry = tk.Entry(window)
        entry.pack()
        entries.append(entry)

    def submit():
        """Validate input fields and save consultant if all data is valid."""
        
        name, specialty, phone, email = [e.get().strip() for e in entries]
        
        # Ensure all fields are filled.                
        if not all([name, specialty, phone, email]):
            messagebox.showerror("خطا", "لطفاً تمام فیلدها را پر کنید")
            return 

        # Simple email format validation.
        if "@" not in email or "." not in email:
            messagebox.showerror("خطا", "ایمیل معتبر وارد کنید")
            return 

        # Save consultant data.
        save_consultant(name, specialty, phone, email)
        messagebox.showinfo("موفق", "مشاور با موفقیت ذخیره شد")
        window.destroy()

    # Submit button to trigger validation and saving.
    tk.Button(window, text="ذخیره مشاور", command=submit).pack(pady=20)
