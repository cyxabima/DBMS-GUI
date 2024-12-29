from tkinter import Tk, ttk, Toplevel


def display_data(data, master=None):
    # Create the main Tkinter window
    root = Toplevel(master) if master is not None else Tk()
    root.title("ALL RECORDS")
    root.geometry("600x400")
    tree_view(root, data)
    # Start the Tkinter main loop
    root.mainloop()


def tree_view(master, data):

    style = ttk.Style()
    # Define a custom style for the Treeview heading
    style.configure(
        "Custom.Treeview.Heading",
        font=("Arial", 12, "bold"),
        background="#F0BB78",
        foreground="#131010",
    )
    style.map(
        "Custom.Treeview.Heading",
        background=[("active", "#8B5C3B")], 
    )

    style.configure(
        "Custom.Treeview",
        rowheight=25,  # Set row height
        font=("Arial", 10),  # Font for the rows
    )

    # Create a Treeview widget
    tree = ttk.Treeview(master, show="headings", style="Custom.Treeview")
    tree.pack(fill="both", expand=True)

    if data:  # data  is a list data will only return false if data is empty
        # here we are column names from the dictionary keys
        column_names = data[0].keys()
        column_names_id = list(column_names)
        column_names_id.insert(0, "ID")

        # Configure columns in the Treeview
        tree["columns"] = list(column_names_id)

        # Define column headings
        for col in column_names_id:
            tree.heading(col, text=col)  # Set the heading
            tree.column(col, width=100, anchor="center")  # Set column properties

        # Insert rows into the Treeview
        for index, row in enumerate(data, start=1):
            # Extract values for each column
            values = [row[col] for col in column_names]
            values.insert(0, index)
            tree.insert("", "end", values=values)


if __name__ == "__main__":
    # Sample data (list of dictionaries)
    data = [
        {"Name": "Alice", "Grade": 90},
        {"Name": "Bob", "Grade": 85},
        {"Name": "Charlie", "Grade": 88},
        {"Name": "David", "Grade": 92},
    ]

    # Display the data
    display_data(data)
