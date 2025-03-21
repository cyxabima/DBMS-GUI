from tkinter import Tk, Toplevel, PhotoImage
from tkinter import ttk, font
from db_open import open_db
from gui_create import create_db
from db_functions import load_databases

root = Tk()
h1_font = font.Font(
    family="Arial",
    size=38,
)
h2_font = font.Font(
    family="Arial",
    size=14,
)

btn_style = ttk.Style()
btn_style.configure(
    "Custom.TButton",
    background="#F0BB78",
    font=("Arial", 16, "bold"),
    foreground="#131010",
)
btn_style.map("Custom.TButton", background=[("active", "#8B5C3B")])

combo_box = ttk.Style()
combo_box.configure(
    "TCombobox",
    fieldbackground="#F0BB78",  # Background color of the entry field
    background="gray",  # Background color of the dropdown
    foreground="black",  # Text color
    borderwidth=2,  # Width of the border
)

hero = PhotoImage(file="./dbms_resources/database.png")
hero_min = PhotoImage(file="./hero_min_.png")
img1 = PhotoImage(file="./dbms_resources/img-add.png")
img2 = PhotoImage(file="./dbms_resources/img-edit.png")
img3 = PhotoImage(file="./dbms_resources/img-delete.png")
img4 = PhotoImage(file="./dbms_resources/img-view.png")
img5 = PhotoImage(file="./dbms_resources/img-search.png")
img6 = PhotoImage(file="./dbms_resources/img-back.png")

root.title("DATABASE MANAGEMENT SYSTEM")
root.geometry("1280x832")
# frm = ttk.Frame(root, padding=10)
# frm.grid()
# ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)


def main():
    # main_frame = ttk.Frame(root, padding=10)
    # main_frame.grid(row=5, column=5)

    # Configure the grid for 5x5 layout
    for i in range(2):
        root.grid_rowconfigure(i, weight=1)  # Make rows stretchable
        root.grid_columnconfigure(i, weight=1)  # Make columns stretchable

    h1 = ttk.Label(
        root,
        text="WELCOME TO DBMS",
        background="#131010",
        foreground="white",
        anchor="center",
        font=h1_font,
    )
    h1.grid(row=0, column=0, columnspan=2, sticky="ew")

    left = ttk.Frame(root)
    hero_label = ttk.Label(master=left, image=hero)
    hero_label.grid(row=1, column=2)
    left.grid(row=1, column=0)

    right = ttk.Frame(root)
    btn1 = ttk.Button(
        right,
        text="Create New",
        style="Custom.TButton",
        width=50,
        command=lambda: create_db(root),
    )
    btn1.grid(row=1, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)
    btn2 = ttk.Button(
        right, text="Open Existing", style="Custom.TButton", command=select_existing
    )
    btn2.grid(row=2, column=1, columnspan=1, sticky="ew", ipady=10, pady=15)
    btn3 = ttk.Button(right, text="Exit", style="Custom.TButton", command=root.destroy)
    btn3.grid(row=3, column=1, columnspan=1, sticky="ew", ipady=10, pady=15)
    right.grid(row=1, column=1)

    root.mainloop()


def show_new_content():
    # Clear the window by destroying existing widgets
    for widget in root.winfo_children():
        widget.destroy()


def select_existing():
    selection_window = Toplevel(root)  # Create a new window
    hero_label = ttk.Label(selection_window, image=hero_min, width=30)
    hero_label.pack(padx=12)

    selection_window.title("Select Data base to Open")
    selection_window.geometry("300x500")

    # Create a combobox (dropdown menu) with options
    combo = ttk.Combobox(
        selection_window,
        style="TCombobox",
        width="30",
        height="14",
        state="readonly",
        font=h2_font,
        values=load_databases(),
    )
    combo.set("Select an option")  # Set a default value
    combo.pack(pady=19)

    # creating btn
    button = ttk.Button(
        selection_window,
        text="Done",
        style="Custom.TButton",
        width=20,
        command=lambda: open_existing(combo),
    )
    button.pack(pady=60)


def open_existing(combo):

    database_name = combo.get()
    print(database_name)
    show_new_content()
    h1 = ttk.Label(
        root,
        text="SELECT YOUR OPERATION:",
        background="#131010",
        foreground="white",
        anchor="center",
        font=h1_font,
    )
    h1.grid(row=0, column=0, columnspan=2, sticky="ew")
    photo_frame = ttk.Frame(root)
    hero_label = ttk.Label(photo_frame, image=hero)
    hero_label.grid(row=0, column=0)
    photo_frame.grid(row=1, column=0)
    frame_curd = ttk.Frame(root)
    frame_curd.grid(row=1, column=1)

    btn_add = ttk.Button(
        frame_curd,
        text="Add Record",
        style="Custom.TButton",
        image=img1,
        compound="left",
        command=lambda: open_db("1", database_name, root),
    )
    btn_add.grid(row=1, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)
    # btn_add.pack()
    btn_edit = ttk.Button(
        frame_curd,
        text="Edit Record",
        style="Custom.TButton",
        image=img2,
        compound="left",
        command=lambda: open_db("2", database_name, root),
    )
    # btn_edit.pack()
    btn_edit.grid(row=2, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)

    btn_delete = ttk.Button(
        frame_curd,
        text="Delete Record",
        style="Custom.TButton",
        image=img3,
        compound="left",
        command=lambda: open_db("3", database_name, root),
    )
    # btn_delete.pack()
    btn_delete.grid(row=3, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)

    btn_view = ttk.Button(
        frame_curd,
        text="Display Record",
        style="Custom.TButton",
        image=img4,
        compound="left",
        command=lambda: open_db("4", database_name, root),
    )
    # btn_view.pack()
    btn_view.grid(row=4, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)
    btn_search = ttk.Button(
        frame_curd,
        text="Search Record",
        style="Custom.TButton",
        image=img5,
        compound="left",
        command=lambda: open_db("5", database_name, root),
    )
    # btn_search.pack()
    btn_search.grid(row=5, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)

    btn_save = ttk.Button(
        frame_curd,
        text="BACK TO MAIN MENU",
        style="Custom.TButton",
        image=img6,
        compound="left",
        command=lambda: [show_new_content(), main()],
    )
    btn_save.grid(row=6, column=1, rowspan=1, sticky="ew", ipady=10, pady=15)
    # btn_save.pack()


main()
