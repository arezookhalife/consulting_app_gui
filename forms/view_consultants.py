import tkinter as tk
from tkinter import ttk
import json
from logic.consultants import search_consultant_by_name
from logic.appointments import appointments_count
from forms.edit_consultant import edit_consultant_form, delete_consultants

def view_consultants():
    """Open a window to display a list of consultants from a JSON file and search consultants by name."""
    appointments_count()

    try:
        with open("data/consultants.json", "r") as file:
            consultants = json.load(file)
    except FileNotFoundError:
        consultants = []    
        
    # Create main window.
    root = tk.Tk()
    root.title("مشاهده مشاوران")
    root.geometry("600x450")
    root.resizable(True, True)
    root.config(bg="lightblue")
        
    
    tk.Label(root, text="لیست مشاوران ", font=("Arial", 12,"bold"),bg="lightblue").pack(pady=20)
    tk.Label(root, text="جستجوی مشاور بر اساس نام",bg="lightblue").place(x=400,y=60)
    
    search_entry = tk.Entry(root) 
    search_entry.place(x=260,y=60)
    
    
    def on_search():  
        
        name = search_entry.get().strip()
        if name:
            results = search_consultant_by_name(name)
        else:
            results= consultants
        display_results(results)
    
        
    tk.Button(root, text="جستجو", command=on_search,bg="blue", fg="white").place(x=200,y=60)
    
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
    tree.pack(side="left", fill="both", expand=True)
    
   
    for c in columns:
        tree.heading(c, text=c, anchor="e")
        tree.column(c, anchor="e")

    tree.column("id", width=0, stretch=False)
    tree.pack(expand=True, fill="both")   
    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)    

    button_frame = tk.Frame(root,bg="lightblue")
    button_frame.place(x=270,y=400)
    selected_consultant_id = tk.StringVar(root)
    

    def on_row_selected(event):
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
    
    edit_button = tk.Button(button_frame, text="ویرایش",bg="purple",fg="white",state="disabled", command=lambda : edit_consultant_form(int(selected_consultant_id.get())))
    edit_button.pack(side="right", padx=10)


    delete_button = tk.Button(button_frame, text="حذف",bg="orange",fg="white",state="disabled", command=lambda : delete_consultants(int(selected_consultant_id.get())))
    delete_button.pack(side="right", padx=10)
    
    status_label = tk.Label(root, text="",bg="lightblue" ,fg="red", font=("Arial", 10))
    status_label.place(x=250,y=350)
    
     
    def display_results(results):
        
        tree.delete(*tree.get_children())

        if not results:
            status_label.config(text="هیچ مشاوری یافت نشد")

        else:
            status_label.config(text="")
            for c in results:
                tree.insert("", tk.END, values=(c["id"],c["appointments_count"],c["email"],c["phone"],c["specialty"],c["name"]))

    
    display_results(consultants)
    
    tree.bind("<<TreeviewSelect>>", on_row_selected)
      
    # Back button to close the window
    tk.Button(root, text="بازگشت", command= root.destroy,bg="red",fg="white").place(x=220,y=400)
    

    root.mainloop()

