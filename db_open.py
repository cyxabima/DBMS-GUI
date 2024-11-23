from db_functions import *
import json

def open_db():
        try:
            with open("DATABASES.txt") as f:
                databases = f.readlines()
                databases = [database.strip() for database in databases]

        except FileNotFoundError:
            databases = []



        if databases: # return True if not empty

            display_all_databases(databases)
            database_name = input("Enter the name of the database to open: ")



            if database_name in databases:

                with open(f"{database_name}_metadata.json") as f:
                    metadata = json.load(f)
                
                try:
                    with open(f"{database_name}.json") as f:
                        data = json.load(f)
                except FileNotFoundError:
                    data = []


                print(f"Database '{database_name}' opened successfully.")
                while True:
                    print("""
                    Database Options:
                    1. Add a record
                    2. Edit a record
                    3. Delete a record
                    4. View all records
                    5. Search Record
                    6. Return to the main menu
                    """)
                    
                    db_choice = input("Enter your choice: ")

                    if db_choice == "1":
                        # Adding
                        add_record(metadata,data)
                            

                    elif db_choice == "2":
                        # Editing
                        edit_record(metadata,data)

                    elif db_choice == "3":
                        # Deleting
                        del_record(metadata,data)

                    elif db_choice == "4":
                        # Viewing
                        print("All records:")
                        view_record(metadata,data)
                    elif db_choice == '5':
                        search_record(metadata,data)

                    elif db_choice == "6":
                        # Returning
                        print("Returning to the main menu...")
                        with open(f"{database_name}.json",'w') as f :
                            json.dump(data,f)
                        break

                    else:
                        print("Invalid choice. Please enter 1, 2, 3, 4, or 5.")
            else:
                print("The specified database does not exist.")
        else:
            print("="*80)
            print("No database is created yet!")
            print("Plz Create Database")
            print("="*80)
