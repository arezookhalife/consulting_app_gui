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
    consultants = load_file(CONSULTANTS_FILE)
       
    # Create main window.
    root = tk.Tk()
    root.title("مشاهده نوبت ها")
    root.geometry("600x470")
    root.resizable(True, True)
    root.config(bg="lightblue")  
     
    tk.Label(root, text="لیست نوبت‌ها",  font=("Arial", 12,"bold"),bg="lightblue").pack(pady=20)
    
    search_frame = tk.Frame(root)
    search_frame.config(width=350,height=50,bg="lightblue")
    search_frame.pack()
    tk.Label(search_frame, text="جستجوی نوبت ",bg="lightblue").place(x=270,y=20)
    tk.Label(search_frame, text="نام مشاور",bg="lightblue").place(x=200,y=10)
    consultant_entry = tk.Entry(search_frame)
    consultant_entry.place(x=70,y=10)
   
    tk.Label(search_frame, text="تاریخ نوبت",bg="lightblue").place(x=200,y=30)
    date_entry = tk.Entry(search_frame)
    date_entry.place(x=70,y=30)
    
    consultant_map={c['id']:c['name'] for c in consultants}

    
    def on_search():  
        """Filter appointments based on consultant name or date."""
        
        appointments = load_file(APPOINTMENTS_FILE)
        consultant_input = consultant_entry.get().strip()
        date_input = date_entry.get().strip()
        if consultant_input:
            results = search_appointment_by_consultant(consultant_input)
        elif date_input:
            results= search_appointments_by_date(date_input)                
        else:
            results= appointments
        display_results(results)
       
        
    tk.Button(search_frame, text="جستجو", command=on_search,bg="blue", fg="white").place(y=20)

    status_label = tk.Label(root, text="",bg="lightblue" ,fg="red", font=("Arial", 10))
    status_label.pack()
        
    result_frame = tk.Frame(root)
    result_frame.pack(pady=10)
    
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
        button_frame.pack()
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


    def show_edit(id):
        edit_appointment_form(id,root)
        appointments = load_file(APPOINTMENTS_FILE)
        display_results(appointments)
    
    
    def show_delete(id):
        delete_appointments(id)
        appointments = load_file(APPOINTMENTS_FILE)
        display_results(appointments)
     
        
    if role=="admin":
        edit_button = tk.Button(
            button_frame,
            text="ویرایش",
            bg="purple",
            fg="white",
            state="disabled",
            command=lambda : show_edit(int(selected_appointment_id.get()))
            )
        edit_button.pack(side="right", padx=10)

        delete_button = tk.Button(
            button_frame,
            text="حذف",
            bg="orange",
            fg="white",
            state="disabled",
            command=lambda : show_delete(int(selected_appointment_id.get()))
            )
        delete_button.pack(side="right", padx=10)
       
       
    appointments = load_file(APPOINTMENTS_FILE)
    display_results(appointments)
    
    if role=="admin":
        tree.bind("<<TreeviewSelect>>", on_row_selected)
   
    # Button to close the appointment viewer window.
    tk.Button(root, text="بازگشت", command= root.destroy,bg="red",fg="white").pack(pady=5)
   
    root.mainloop()

