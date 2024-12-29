from tkinter import Tk, ttk, font, Toplevel
from db_functions import save_data


def add_record(database_name, metadata, data, master=None):
    # Create the main window
    add_record_screen = Toplevel(master) if master is not None else Tk()
    add_record_screen.title("Add Record")
    # add_record_screen.geometry("400x500")
    # add_record_screen.resizable(False, False)

    h1_font = font.Font(
        family="Arial",
        size=38,
    )
    # h2_font = font.Font(
    #     family="Arial",
    #     size=14,
    # )

    # Style Configuration
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))
    style.configure(
        "TButton",
        background="#F0BB78",
        font=("Arial", 16, "bold"),
        foreground="#131010",
    )
    style.map("TButton", background=[("active", "#8B5C3B")])

    # Title Label
    title_label = ttk.Label(
        add_record_screen,
        text=f"Add Record to {database_name}",
        background="#131010",
        foreground="white",
        font=h1_font,
        anchor="center",
    )
    title_label.grid(row=0, column=0, columnspan=2, sticky="ew")

    entries = []

    # Generate fields dynamically based on metadata
    for i, field in enumerate(metadata):
        field_name = field["field name"]
        # Field Label
        ttk.Label(add_record_screen, text=field_name).grid(
            row=i + 1, column=0, padx=10, pady=5, sticky="e"
        )
        # Entry Field
        entry = ttk.Entry(add_record_screen, width=30)
        entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="w")
        entries.append(entry)

    # Save and Exit Buttons
    save_btn = ttk.Button(
        add_record_screen,
        text="Save Record",
        command=lambda: save_record(
            add_record_screen, entries, database_name, metadata, data
        ),
    )
    save_btn.grid(
        row=len(metadata) + 1, column=0, pady=10, columnspan=2, padx=12, sticky="ew"
    )

    exit_btn = ttk.Button(
        add_record_screen, text="Exit", command=add_record_screen.destroy
    )
    exit_btn.grid(
        row=len(metadata) + 2, column=0, pady=10, columnspan=2, padx=12, sticky="ew"
    )

    # Start the main event loop
    add_record_screen.mainloop()


def save_record(add_record_screen, entries, database_name, metadata, data):

    # Create a new record dictionary
    new_record = {}

    # Retrieve and store the entered values
    for i, field in enumerate(metadata):
        field_name = field["field name"]
        value = entries[i].get()
        new_record[field_name] = value

    # Append the new record to the data list
    data.append(new_record)
    print("Record added successfully:", data)
    save_data(database_name, data)
    for widget in add_record_screen.winfo_children():
        if isinstance(widget, ttk.Entry):  # Check if the widget is an Entry
            widget.delete(0, "end")  # Clear the text


if __name__ == "__main__":
    data: list = []
    metadata = [
        {"field name": "Name", "field length": 12},
        {"field name": "Father Name", "field length": 12},
        {"field name": "Roll Number", "field length": 12},
        {"field name": "Quiz 1", "field length": 3},
        {"field name": "Quiz 2", "field length": 3},
        {"field name": "Quiz 3", "field length": 3},
        {"field name": "Final", "field length": 3},
    ]

    add_record("TestDatabase", metadata, data)
