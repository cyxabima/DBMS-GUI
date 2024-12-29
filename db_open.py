from db_functions import (
    edit_record,
    load_databases,
    load_data,
    save_data,
)

from gui_add import add_record
from gui_display import display_data
from gui_search import search_record
from gui_delete import delete_record


def open_db(db_choice, database_name, root):
    databases = load_databases()

    if database_name in databases:
        metadata, data = load_data(database_name)

        if db_choice == "1":
            # Adding
            add_record(database_name, metadata, data, root)

        elif db_choice == "2":
            # Editing
            edit_record(database_name, metadata, data, root)

        elif db_choice == "3":
            # Deleting
            delete_record(database_name, metadata, data, root)

        elif db_choice == "4":
            # Viewing
            display_data(data, root)
        elif db_choice == "5":
            search_record(metadata, data, root)

        elif db_choice == "6":
            # Returning
            print(data)
            save_data(database_name, data)
            print("Returning to the main menu...")
