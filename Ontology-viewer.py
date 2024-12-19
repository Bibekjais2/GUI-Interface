from owlready2 import get_ontology
from tkinter import *
from tkinter import ttk

# Load the ontology
ontology_file = "English-Grammer.owx"  # Replace with your ontology file path
ontology = get_ontology(ontology_file).load()

# Function to fetch classes
def fetch_classes():
    listbox.delete(0, "end")
    for cls in ontology.classes():
        listbox.insert("end", f"Class: {cls.name}")

# Function to fetch individuals
def fetch_individuals():
    listbox.delete(0, "end")
    for individual in ontology.individuals():
        listbox.insert("end", f"Individual: {individual.name}")

# Function to fetch object properties
def fetch_object_properties():
    listbox.delete(0, "end")
    for prop in ontology.object_properties():
        listbox.insert("end", f"Object Property: {prop.name}")

# Function to fetch data properties
def fetch_data_properties():
    listbox.delete(0, "end")
    for prop in ontology.data_properties():
        listbox.insert("end", f"Data Property: {prop.name}")

# Function to search ontology
def search_ontology():
    query = search_var.get().lower()
    listbox.delete(0, "end")
    for cls in ontology.classes():
        if query in cls.name.lower():
            listbox.insert("end", f"Class: {cls.name}")
    for individual in ontology.individuals():
        if query in individual.name.lower():
            listbox.insert("end", f"Individual: {individual.name}")
    for prop in ontology.object_properties():
        if query in prop.name.lower():
            listbox.insert("end", f"Object Property: {prop.name}")
    for prop in ontology.data_properties():
        if query in prop.name.lower():
            listbox.insert("end", f"Data Property: {prop.name}")

# Initialize Root
root = Tk()
root.title("English-Grammer Ontology Viewer")
root.geometry("800x700")
root.configure(bg="#1c1c1e")  # Dark background

# Gradient Header
canvas = Canvas(root, height=120, bg="#1c1c1e", highlightthickness=0)
canvas.pack(fill=X)
canvas.create_rectangle(0, 0, 800, 120, fill="#4a4e69", outline="")
canvas.create_rectangle(0, 0, 800, 60, fill="#22223b", outline="")

header = Label(root, text="Chemistry Ontology Viewer", font=("Helvetica", 24, "bold"), fg="#f2e9e4", bg="#4a4e69")
header.place(x=200, y=30)

# Search Frame
search_frame = Frame(root, bg="#1c1c1e", pady=10)
search_frame.pack(fill=X)

search_var = StringVar()
search_entry = Entry(search_frame, textvariable=search_var, font=("Arial", 14), width=40, relief="solid", bd=2)
search_entry.pack(side=LEFT, padx=20)

search_button = Button(search_frame, text="Search", font=("Arial", 12, "bold"), bg="#9a8c98", fg="white", relief="flat",
                       activebackground="#c9ada7", activeforeground="black", command=search_ontology)
search_button.pack(side=LEFT, padx=10)

# Button Frame
button_frame = Frame(root, bg="#1c1c1e", pady=10)
button_frame.pack(fill=X)

def create_button(frame, text, command):
    return Button(frame, text=text, font=("Arial", 12, "bold"), bg="#9a8c98", fg="white", relief="raised",
                  activebackground="#c9ada7", activeforeground="black", padx=10, pady=5, command=command)

class_button = create_button(button_frame, "Show Classes", fetch_classes)
class_button.pack(side=LEFT, padx=10, pady=5)

individual_button = create_button(button_frame, "Show Individuals", fetch_individuals)
individual_button.pack(side=LEFT, padx=10)

object_prop_button = create_button(button_frame, "Show Object Properties", fetch_object_properties)
object_prop_button.pack(side=LEFT, padx=10)

data_prop_button = create_button(button_frame, "Show Data Properties", fetch_data_properties)
data_prop_button.pack(side=LEFT, padx=10)

# Listbox Frame with Scrollbar
listbox_frame = Frame(root, bg="#1c1c1e")
listbox_frame.pack(fill=BOTH, expand=True, padx=20, pady=10)

scrollbar = Scrollbar(listbox_frame, orient=VERTICAL)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    listbox_frame, yscrollcommand=scrollbar.set, font=("Courier", 14), bg="#252525",
    fg="#f2e9e4", selectbackground="#c9ada7", selectforeground="#1c1c1e", relief="flat"
)
listbox.pack(fill=BOTH, expand=True)
scrollbar.config(command=listbox.yview)

# Footer
footer = Label(root, text="© 2024 Chemistry Ontology Viewer | Developed with Python", bg="#22223b", fg="#f2e9e4",
               font=("Arial", 10))
footer.pack(fill=X, pady=5)

# Run the Mainloop
root.mainloop()

