import tkinter as tk
from tkinter import ttk
from logic.consultants import search_consultant_by_name
from logic.appointments import appointments_count
from forms.edit_consultant import edit_consultant_form, delete_consultants
from logic.utils import load_file


CONSULTANTS_FILE= "data/consultants.json"


def view_consultants(role):
    """Open a window to display a list of consultants from JSON file and allow searching by name."""
    
    appointments_count()

    consultants = load_file(CONSULTANTS_FILE)  
        
   # Create the main application window with specified appearance.
    root = tk.Tk()
    root.title("مشاهده مشاوران")
    root.geometry("1000x470")
    root.resizable(True, True)
    root.config(bg="lightblue")
        
    tk.Label(root, text="لیست مشاوران ", font=("Arial", 12,"bold"),bg="lightblue").pack(pady=20)
    search_frame = tk.Frame(root)
    search_frame.config(width=350,height=35,bg="lightblue")
    search_frame.pack()    
    tk.Label(search_frame, text="جستجوی مشاور بر اساس نام",bg="lightblue").place(x=250,y=10)
    
    search_entry = tk.Entry(search_frame) 
    search_entry.place(x=70,y=10)
    
    
    def on_search():
        """Search consultants by name if input provided, otherwise display all consultants."""  
        
        name = search_entry.get().strip()
        if name:
            results = search_consultant_by_name(name)
        else:
            results= consultants
        display_results(results)
    
        
    tk.Button(search_frame, text="جستجو", command=on_search,bg="blue", fg="white").place(y=10)
    
    status_label = tk.Label(root, text="",bg="lightblue" ,fg="red", font=("Arial", 10))
    status_label.pack()
    
    result_frame = tk.Frame(root)
    result_frame.pack(pady=20)
    
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("Treeview.Heading", background="lightblue", foreground="black", font=("Arial", 12, "bold"))
    
    columns = ("id","تعداد نوبت","ایمیل","شماره تماس","تخصص",  "نام مشاور" )
    vsb = ttk.Scrollbar(result_frame, orient="vertical")
    hsb = ttk.Scrollbar(result_frame, orient="horizontal")
   
    tree = ttk.Treeview(result_frame, columns=columns, show="headings", height=10)            
    
    vsb.config(command=tree.yview)
    hsb.config(command=tree.xview)
    
    vsb.pack(side="right", fill="y")
    hsb.pack(side="bottom", fill="x")
    tree.pack(side="right", fill="both", expand=True)
    
    for c in columns:
        tree.heading(c, text=c, anchor="e")
        tree.column(c, anchor="e")

    tree.column("id", width=0, stretch=False)
    tree.pack(expand=True, fill="both")   
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)    

    if role=="admin":
        button_frame = tk.Frame(root,bg="lightblue")
        button_frame.pack()
        
        # Store the selected consultant's ID for edit or delete operations.
        selected_consultant_id = tk.StringVar(root)
        

    def on_row_selected(event):
        """Enable or disable edit and delete buttons based on row selection."""
        
        selected = tree.selection()
        if selected:
            selected_id = tree.item(selected[0])["values"][0]
            selected_id = selected_id
            selected_consultant_id.set(selected_id)
            edit_button.config(state="normal")
            delete_button.config(state="normal")
        else:
            selected_consultant_id.set("")
            edit_button.config(state="disabled")
            delete_button.config(state="disabled")   
    
     
    def display_results(results):
        """Display the given list of consultants in the Treeview, or show a 'not found' message."""

        tree.delete(*tree.get_children())

        if not results:
            status_label.config(text="هیچ مشاوری یافت نشد")
        else:
            status_label.config(text="")
            for c in results:
                tree.insert("", tk.END, values=(c["id"],c["appointments_count"],c["email"],c["phone"],c["specialty"],c["name"]))


    def show_edit(id):
        edit_consultant_form(id,root)
        consultants = load_file(CONSULTANTS_FILE)
        display_results(consultants)
    

    def show_delete(id):
        delete_consultants(id)
        consultants = load_file(CONSULTANTS_FILE)
        display_results(consultants)
            
    
    if role=="admin":
        # Edit button to modify the selected consultant
        edit_button = tk.Button(
            button_frame,
            text="ویرایش",
            bg="purple",
            fg="white",
            state="disabled",
            command=lambda : show_edit(int(selected_consultant_id.get()))
            )
        edit_button.pack(side="right", padx=10)

        # Delete button to remove the selected consultant
        delete_button = tk.Button(
            button_frame,
            text="حذف",
            bg="orange",
            fg="white",
            state="disabled",
            command=lambda : show_delete(int(selected_consultant_id.get()))
            )
        delete_button.pack(side="right", padx=10)
        
    display_results(consultants)
        
    if role=="admin":
        # Bind row selection event to update button states.    
        tree.bind("<<TreeviewSelect>>", on_row_selected)
      
    # Back button to close the window.
    tk.Button(root, text="بازگشت", command= root.destroy,bg="red",fg="white").pack(pady=5)
    root.mainloop()

