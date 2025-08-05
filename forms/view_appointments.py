import tkinter as tk
from tkinter import ttk
from logic.appointments import search_appointment_by_consultant, search_appointments_by_date
from forms.edit_appointments import edit_appointment_form, delete_appointments
from logic.utils import load_file


APPOINTMENTS_FILE= "data/appointments.json"
CONSULTANTS_FILE= "data/consultants.json"

 
def view_appointments(role):
    """Open a window to display and manage a list of appointments."""
   
    # Load consultants and appointments data from JSON files.
    appointments = load_file(APPOINTMENTS_FILE)
    consultants = load_file(CONSULTANTS_FILE)
       
    # Create main window.
    root = tk.Tk()
    root.title("مشاهده نوبت ها")
    root.geometry("600x450")
    root.resizable(True, True)
    root.config(bg="lightblue")  
     
    tk.Label(root, text="لیست نوبت‌ها",  font=("Arial", 12,"bold"),bg="lightblue").pack(pady=20)
    tk.Label(root, text="جستجوی نوبت ",bg="lightblue").place(x=450,y=70)
    tk.Label(root, text="نام مشاور",bg="lightblue").place(x=370,y=60)
    consultant_entry = tk.Entry(root)
    consultant_entry.place(x=240,y=60)
   
    tk.Label(root, text="تاریخ نوبت",bg="lightblue").place(x=370,y=80)
    date_entry = tk.Entry(root)
    date_entry.place(x=240,y=80)
    
    consultant_map={c['id']:c['name'] for c in consultants}

    
    def on_search():  
        """Filter appointments based on consultant name or date."""
        
        consultant_input = consultant_entry.get().strip()
        date_input = date_entry.get().strip()
        if consultant_input:
            results = search_appointment_by_consultant(consultant_input)
        elif date_input:
            results= search_appointments_by_date(date_input)                
        else:
            results= appointments
        display_results(results)
       
        
    tk.Button(root, text="جستجو", command=on_search,bg="blue", fg="white").place(x=170,y=70)
    
    result_frame = tk.Frame(root)
    result_frame.pack(pady=40)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="lightblue", foreground="black", font=("Arial", 12, "bold"))
    
    columns = ("id","ساعت مشاوره ","تاریخ مشاوره",  "نام مشاور" )
    vsb = ttk.Scrollbar(result_frame, orient="vertical")
    hsb = ttk.Scrollbar(result_frame, orient="horizontal")
   
    tree = ttk.Treeview(result_frame, columns=columns, show="headings", height=10)            
    
    vsb.config(command=tree.yview)
    hsb.config(command=tree.xview)
    
    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(side="left", fill="both", expand=True)
    
    for c in columns:
        tree.heading(c, text=c, anchor="e")
        tree.column(c, anchor="e")

    tree.column("id", width=0, stretch=False)
    tree.pack(expand=True, fill="both")   
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set) 
       
    if role=="admin":
        button_frame = tk.Frame(root,bg="lightblue")
        button_frame.place(x=270,y=400)
        selected_appointment_id = tk.StringVar(root)
    
    
    def on_row_selected(event):
        """Handle selection of an appointment from the table."""
        
        selected = tree.selection()
        if selected:
            selected_id = tree.item(selected[0])["values"][0]
            selected_id = selected_id
            selected_appointment_id.set(selected_id)
            edit_button.config(state="normal")
            delete_button.config(state="normal")
        else:
            selected_appointment_id.set("")
            edit_button.config(state="disabled")
            delete_button.config(state="disabled")
    
    if role=="admin":
        edit_button = tk.Button(
            button_frame,
            text="ویرایش",
            bg="purple",
            fg="white",
            state="disabled",
            command=lambda : edit_appointment_form(int(selected_appointment_id.get()))
            )
        edit_button.pack(side="right", padx=10)

        delete_button = tk.Button(
            button_frame,
            text="حذف",
            bg="orange",
            fg="white",
            state="disabled",
            command=lambda : delete_appointments(int(selected_appointment_id.get()))
            )
        delete_button.pack(side="right", padx=10)
        
    status_label = tk.Label(root, text="",bg="lightblue" ,fg="red", font=("Arial", 10))
    status_label.place(x=250,y=350)
    
    
    def display_results(results):
        """Show filtered or full appointment list in the treeview."""
        
        tree.delete(*tree.get_children())

        if not results:
            status_label.config(text="هیچ نوبتی یافت نشد")
        else:
            status_label.config(text="")
            for a in results:
                name=consultant_map.get(int(a['consultant_id']),"مشاور ناشناس")
                tree.insert("", tk.END, values=(a["id"],a["time"],a["date"],name))


    display_results(appointments)
    
    if role=="admin":
        tree.bind("<<TreeviewSelect>>", on_row_selected)
   
    # Button to close the appointment viewer window.
    tk.Button(root, text="بازگشت", command= root.destroy,bg="red",fg="white").place(x=220,y=400)
   
    root.mainloop()

