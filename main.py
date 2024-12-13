from db_create import create_db
from db_open import open_db

menu = """
    ================================================
    | Welcome to the Database Management System :) |
    | Please select an option:                     |
    | 1. Create a new database                     |
    | 2. Open an existing database                 |
    | 3. Exit                                      |
    ================================================
"""

# main menu
while True:
    print(menu)

    choice = input("Enter your choice: ")

    if choice == "1":
        create_db()

    elif choice == "2":
        open_db()
    elif choice == "3":
        # 3) Exiting
        print("Thank you for using this database management system :)")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
