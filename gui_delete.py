from tkinter import Tk, messagebox, Toplevel
from tkinter import ttk
from gui_display import tree_view
from db_functions import save_data


def delete_record(database_name, metadata, data, master=None):

    delete_screen = Toplevel(master) if master is not None else Tk()
    delete_screen.title("Delete Record")

    style = ttk.Style()
    style.configure(
        "Custom.TButton",
        background="#F0BB78",
        font=("Arial", 16, "bold"),
        foreground="#131010",
    )
    style.map("Custom.TButton", background=[("active", "#8B5C3B")])

    h2 = ttk.Label(delete_screen, font=("Arial", 16), text="Enter Record ID:")
    h2.pack(pady=10, padx=20)

    input_record = ttk.Entry(delete_screen)
    input_record.pack()

    btn = ttk.Button(
        delete_screen,
        text="Enter",
        style="Custom.TButton",
        command=lambda: get_record(
            delete_screen, input_record, database_name, metadata, data
        ),
    )
    btn.pack(pady=20)

    tree_view(delete_screen, data)

    delete_screen.mainloop()


def get_record(delete_screen, input_record, database_name, metadata, records):
    record_index = input_record.get()
    if not records:
        print("No records to delete.")
    else:
        if record_index.isdigit():
            # because user counting start from  one while indexing is python start from 0
            record_index = int(record_index) - 1
            # checking that record_index should be valid
            if 0 <= record_index < len(records):
                records.pop(record_index)
                # destroying previous treeView
                for child in delete_screen.winfo_children():
                    if isinstance(child, ttk.Treeview):
                        child.destroy()

                tree_view(delete_screen, records)
                save_data(database_name, records)
        else:
            messagebox.showwarning("Must write Integer")


if __name__ == "__main__":
    metadata = [
        {"field name": "name", "field length": 12},
        {"field name": "fname", "field length": 12},
        {"field name": "roll", "field length": 12},
        {"field name": "q1", "field length": 3},
        {"field name": "q2", "field length": 3},
        {"field name": "q2", "field length": 3},
        {"field name": "final", "field length": 3},
    ]
    data = [
        {
            "name": "ukasha",
            "fname": "anwer",
            "roll": "115",
            "q1": "12",
            "q2": "14",
            "final": "111",
        },
        {
            "name": "mueed",
            "fname": "abdul",
            "roll": "112",
            "q1": "12",
            "q2": "14",
            "final": "111",
        },
    ]
    delete_record("falto.txt", metadata, data)
