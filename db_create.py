import json
from tkinter import Tk, messagebox, font, Toplevel
from tkinter import ttk


def save_metadata(database_name, entries):
    metadata = []

    for field_name_entry, field_length_entry in entries:
        field_name = field_name_entry.get()
        field_length = field_length_entry.get()
        metadata.append({"field name": field_name, "field length": int(field_length)})

    print(f"Database '{database_name}' created successfully.")

    with open(f"{database_name}_metadata.json", "w") as f:
        json.dump(metadata, f)

    with open("DATABASES.txt", "a") as f:
        f.write(f"{database_name}\n")


def design_db(master, databases, input_name, spin_box):
    database_name = input_name.get()
    num_fields = spin_box.get()

    if database_name in databases:
        messagebox.showerror("Error", message="Data Base Already Exist")

    else:
        # database = {}
        entries = []

        for child in master.winfo_children():
            child.destroy()

        h2 = ttk.Label(master, text="ENTER FIELD NAME AND MAX LENGTH")
        h2.pack()

        fields_Frame = ttk.Frame(master)
        for i in range(1, int(num_fields) + 1):
            field_name = ttk.Label(fields_Frame, text="Enter field name ")
            field_name.pack()

            entry_name = ttk.Entry(fields_Frame)
            entry_name.pack()

            field_length = ttk.Label(fields_Frame, text="Enter field length ")
            field_length.pack()

            entry_length = ttk.Entry(fields_Frame)
            entry_length.pack()

            entries.append((entry_name, entry_length))

            # for child in master.winfo_children():
            #     child.destroy()

        fields_Frame.pack()
        btn_done = ttk.Button(
            master,
            text="Done",
            command=lambda: save_metadata(database_name, entries),
        )
        btn_done.pack()


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
    btn_style.map("Custom.TButton", background=[("active", "#8B5C3B")])

    # making grids
    for i in range(6):
        create_screen.grid_rowconfigure(i, weight=1)
    create_screen.grid_columnconfigure(0, weight=1)

    h1_font = font.Font(
        family="Arial",
        size=28,
    )
    h2_font = font.Font(
        family="Arial",
        size=14,
    )

    h1 = ttk.Label(
        create_screen,
        text="CREATE NEW DATABASE",
        font=h1_font,
        foreground="white",
        background="#131010",
        anchor="center",
    )

    h1.grid(row=0, column=0, pady=1, sticky="ew")

    h2 = ttk.Label(
        create_screen, text="Enter the name of the new database: ", font=h2_font
    )
    h2.grid(row=1, column=0, sticky="ew")

    input_database_name = ttk.Entry(create_screen, width=50)
    input_database_name.grid(row=2, column=0, sticky="ew")

    num_fields = ttk.Label(
        create_screen, text="No of fields you want to Create: ", font=h2_font
    )
    num_fields.grid(row=3, column=0, sticky="ew")
    spin_box = ttk.Spinbox(create_screen, from_=1, to=20, width=47)
    spin_box.grid(row=4, column=0, sticky="ew")

    btn = ttk.Button(
        create_screen,
        text="Create",
        style="Create.TButton",
        command=lambda: design_db(
            create_screen, databases, input_database_name, spin_box
        ),
    )
    btn.grid(row=5, column=0, pady=30)

    create_screen.mainloop()


if __name__ == "__main__":
    create_db()
