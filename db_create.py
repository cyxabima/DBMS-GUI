import json
def create_db():
        try:
            with open("DATABASES.txt") as f :
                databases = f.readlines()
                databases = [database.strip() for database in databases]
        except FileNotFoundError:
             databases = []

        #databases = [database.strip() for database in databases]

        
        database_name = input("Enter the name of the new database: ")
        if database_name in databases:
            print("A database with this name already exists. Please try a different name.")
        else:
            #database = {}
            metadata = []
            while True:
                field_name = input("Enter field name (or press 'enter' to finish): ")
                if field_name == '':
                    break
                while True: #we using this while loop to take input from user again if the length enter by use is not integer
                    field_length = input("Enter length for this field (integer): ")
                    if field_length.isdigit():
                        metadata.append({'field name': field_name, 'field length': int(field_length)})
                        break
                    print("Please enter a valid integer for length.")

            #database[database_name] = {'metadata': metadata, 'records': []}

            print(f"Database '{database_name}' created successfully.")

            with open(f"{database_name}_metadata.json",'w') as f :
                 json.dump(metadata,f)

            with open("DATABASES.txt","a") as f:
                 f.write(f"{database_name}\n")
            
                 
