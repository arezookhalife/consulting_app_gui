import tkinter as tk
import json

def view_appointments():
    """Open a window to display a list of consultants from a JSON file."""
    
    # Create main window.
    root = tk.Tk()
    root.title("مشاهده نوبت‌ها")
    root.geometry("600x400")

    tk.Label(root, text="لیست مشاوران و نوبت‌ها", font=("Arial", 14)).pack(pady=20)

    # Try to load consultants data from JSON file.
    try:
        with open("data/consultants.json", "r") as file:
            consultants = json.load(file)
    except FileNotFoundError:
        consultants = []

    # Display message if no consultants are found.
    if not consultants:
        tk.Label(root, text="هیچ مشاوری ثبت نشده است.").pack()
    else:
         # Header for consultant info.
        tk.Label(root, text="نام مشاور | تخصص | شماره تماس").pack(pady=10)

        # Display each consultant's info.
        for consultant in consultants:
            consultant_info = f"{consultant['name']} | {consultant['specialty']} | {consultant['phone']}"
            tk.Label(root, text=consultant_info).pack(pady=2)

    # Back button to close the window
    tk.Button(root, text="بازگشت", command=root.destroy).pack(pady=20)

    root.mainloop()
