import json
from tkinter import Tk, messagebox, font, Toplevel, PhotoImage
from tkinter import ttk


def create_db(master=None):
    try:
        with open("DATABASES.txt") as f:
            databases = f.readlines()
            databases = [database.strip() for database in databases]
    except FileNotFoundError:
        databases = []

    create_screen = Toplevel(master) if master is not None else Tk()
    create_screen.title("Create New Database")

    btn_style = ttk.Style()
    btn_style.configure(
        "Create.TButton",
        background="#F0BB78",
        font=("Arial", 16, "bold"),
        foreground="#131010",
    )
    btn_style.map("Create.TButton", background=[("active", "#8B5C3B")])

    # Configure grid layout
    for i in range(6):
        create_screen.grid_rowconfigure(i, weight=1)
    create_screen.grid_columnconfigure(0, weight=1)

    h1_font = font.Font(family="Arial", size=28)
    h2_font = font.Font(family="Arial", size=14)

    h1 = ttk.Label(
        create_screen,
        text="CREATE NEW DATABASE",
        font=h1_font,
        foreground="white",
        background="#131010",
        anchor="center",
    )
    h1.grid(row=0, column=0, pady=10, sticky="ew")

    h2 = ttk.Label(
        create_screen, text="Enter the name of the new database: ", font=h2_font
    )
    h2.grid(row=1, column=0, sticky="ew")

    input_database_name = ttk.Entry(create_screen, width=50)
    input_database_name.grid(row=2, column=0, sticky="ew")

    num_fields_label = ttk.Label(
        create_screen, text="Number of fields to create: ", font=h2_font
    )
    num_fields_label.grid(row=3, column=0, sticky="ew")

    spin_box = ttk.Spinbox(create_screen, from_=1, to=20, width=47)
    spin_box.grid(row=4, column=0, sticky="ew")

    btn = ttk.Button(
        create_screen,
        text="Create",
        style="Create.TButton",
        command=lambda: design_db(
            create_screen, databases, input_database_name, int(spin_box.get())
        ),
    )
    btn.grid(row=5, column=0, pady=30)

    create_screen.mainloop()


def design_db(master, databases, input_name, num_fields):
    database_name = input_name.get()
    hero_min = PhotoImage(file="/home/cyxabima/cs/cep-group-new/hero_min_.png")
    h1_font = font.Font(family="Arial", size=28)

    if not database_name:
        messagebox.showerror("Error", "Database name cannot be empty.")
        return

    if database_name in databases:
        messagebox.showerror("Error", f"Database '{database_name}' already exists.")
        return

    # Destroy current UI
    for child in master.winfo_children():
        child.destroy()

    master.title(f"Design Database: {database_name}")

    h1 = ttk.Label(
        master,
        text="Enter Field Names",
        font=h1_font,
        foreground="white",
        background="#131010",
        anchor="center",
    )
    # h2 = ttk.Label(master, text="Enter Field Names and Max Lengths", font=("Arial", 14))
    h1.pack(pady=10)

    hero = ttk.Label(master, image=hero_min)
    hero.pack()

    fields_frame = ttk.Frame(master)
    fields_frame.pack(pady=10)

    entries = []
    for i in range(num_fields):
        field_label = ttk.Label(fields_frame, text=f"Field {i+1} Name: ")
        field_label.grid(row=i, column=0, padx=5, pady=5)

        field_entry = ttk.Entry(fields_frame, width=20)
        field_entry.grid(row=i, column=1, padx=5, pady=5)

        length_label = ttk.Label(fields_frame, text="Max Length: ")
        length_label.grid(row=i, column=2, padx=5, pady=5)

        length_entry = ttk.Spinbox(fields_frame, width=10, from_=4, to=32)
        length_entry.grid(row=i, column=3, padx=5, pady=5)

        entries.append((field_entry, length_entry))

    btn_style = ttk.Style()
    btn_style.configure(
        "Create.TButton",
        background="#F0BB78",
        font=("Arial", 16, "bold"),
        foreground="#131010",
    )
    btn_style.map("Create.TButton", background=[("active", "#8B5C3B")])
    btn_done = ttk.Button(
        master,
        text="Save",
        style="Create.TButton",
        command=lambda: save_metadata(master, database_name, entries),
    )
    btn_done.pack(pady=20)


def save_metadata(master, database_name, entries):
    metadata = []

    for field_name_entry, field_length_entry in entries:
        field_name = field_name_entry.get()
        field_length = field_length_entry.get()

        if not field_name or not field_length.isdigit():
            messagebox.showerror(
                "Error", "All fields must have valid names and lengths."
            )
            return

        metadata.append({"field name": field_name, "field length": int(field_length)})

    # Save metadata to file
    with open(f"{database_name}_metadata.json", "w") as f:
        json.dump(metadata, f, indent=4)

    # Save database name to the list
    with open("DATABASES.txt", "a") as f:
        f.write(f"{database_name}\n")

    messagebox.showinfo("Success", f"Database '{database_name}' created successfully!")
    master.destroy()


if __name__ == "__main__":
    create_db()
