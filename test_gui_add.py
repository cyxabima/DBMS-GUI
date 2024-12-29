from tkinter import Tk, ttk
from db_functions import save_data


def add_record(database_name, metadata, data):
    # Create the main window
    add_record_screen = Tk()
    add_record_screen.title("Add Record")
    add_record_screen.geometry("400x500")
    add_record_screen.resizable(False, False)

    # Style Configuration
    style = ttk.Style()
    style.configure("TLabel", font=("Arial", 12))
    style.configure("TEntry", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12, "bold"))

    # Title Label
    title_label = ttk.Label(
        add_record_screen,
        text=f"Add Record to {database_name}",
        font=("Arial", 16, "bold"),
        anchor="center",
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

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
    save_btn.grid(row=len(metadata) + 1, column=0, pady=20, columnspan=2)

    exit_btn = ttk.Button(
        add_record_screen, text="Exit", command=add_record_screen.destroy
    )
    exit_btn.grid(row=len(metadata) + 2, column=0, pady=10, columnspan=2)

    # Start the main event loop
    add_record_screen.mainloop()


def save_record(add_record_screen, entries, database_name, metadata, data):
    # Create a new record dictionary
    new_record = {}

    # Retrieve and store the entered values
    for i, field in enumerate(metadata):
        field_name = field["field name"]
        value = entries[i].get()  # Get the value from the corresponding entry widget
        new_record[field_name] = value

    # Append the new record to the data list
    data.append(new_record)
    print("Record added successfully:", data)
    save_data(database_name, data)


# Uncomment the below code to test
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























# from tkinter import Tk
# from tkinter import ttk
# from db_functions import save_data


# def add_record(database_name, metadata, data):
#     add_record_screen = Tk()
#     add_record_screen.title("Add Record")
#     add_record_screen.geometry("300x500")

#     entries = []

#     for field in metadata:

#         field_name = field["field name"]
#         field_length = field["field length"]
#         ttk.Label(add_record_screen, text=field_name).pack(pady=10)
#         entry = ttk.Entry(add_record_screen)
#         entry.pack(pady=10)
#         entries.append(entry)

#     save_btn = ttk.Button(
#         add_record_screen,
#         text="Save Record",
#         command=lambda: save_record(
#             add_record_screen, entries, database_name, metadata, data
#         ),
#     )
#     save_btn.pack()
#     exit_btn = ttk.Button(
#         add_record_screen, text="exit", compound=lambda: add_record_screen.destroy()
#     )
#     exit_btn.pack()
#     add_record_screen.mainloop()


# def save_record(add_record_screen, entries, database_name, metadata, data):
#     Create a new record dictionary
#     new_record = {}

#     Retrieve and store the entered values
#     for i, field in enumerate(metadata):
#         field_name = field["field name"]
#         value = entries[i].get()  # Get the value from the corresponding entry widget
#         new_record[field_name] = value

#     Append the new record to the data list
#     data.append(new_record)
#     print("Record added successfully:", data)
#     save_data(database_name, data)


# data: list = []
# metadata = [
#     {"field name": "name", "field length": 12},
#     {"field name": "fname", "field length": 12},
#     {"field name": "roll", "field length": 12},
#     {"field name": "q1", "field length": 3},
#     {"field name": "q2", "field length": 3},
#     {"field name": "q2", "field length": 3},
#     {"field name": "final", "field length": 3},
# ]

# add_record(metadata, data)


