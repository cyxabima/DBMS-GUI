from tkinter import Tk, IntVar, Toplevel
from tkinter import ttk
from gui_display import tree_view


def search_record(metadata, data, master=None):
    search_record_screen = Toplevel(master) if master is not None else Tk()
    attribute_Frame = ttk.Frame(search_record_screen)
    attribute_Frame.pack()
    search_entry = ttk.Entry(attribute_Frame)
    search_entry.pack()

    h2 = ttk.Label(
        attribute_Frame, text="On Which attribute you want to find the record:"
    )
    h2.pack()

    dic_choice = {}
    option = IntVar(attribute_Frame, value=0)

    for index, dic in enumerate(metadata, start=1):

        selection = ttk.Radiobutton(
            attribute_Frame, text=f"{dic['field name']}", variable=option, value=index
        )
        selection.pack()

        dic_choice.update({index: f"{dic['field name']}"})

    btn_search = ttk.Button(
        attribute_Frame,
        text="Select",
        command=lambda: get_choice(
            search_record_screen, option, search_entry, dic_choice, data
        ),
    )
    btn_search.pack()

    btn_exit = ttk.Button(
        attribute_Frame, text="Exit", command=lambda: search_record_screen.destroy()
    )
    btn_exit.pack()
    search_record_screen.mainloop()


def get_choice(master, e, search, dic_choice, records):
    choice = e.get()
    search_value = search.get()

    for keys, values in dic_choice.items():

        if choice == keys:
            finding = search_value
            list_found_records = []
            for dic in records:  # dic contain the dict of each record

                if dic[values] == finding:
                    list_found_records.append(dic)

    tree_view(master, list_found_records)
