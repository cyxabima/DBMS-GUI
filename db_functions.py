def add_record(metadata, data):
    '''Takes list of dict named metadata(conatin data about the data) and list of dict named data(containing the actual data) and retrives field name and field length from metadata and uses these to add records in a data'''

    while True:
        new_record = {}
        print("*" * 100)
        for field in metadata: #metadata is a list of dict so field  containe dictionery
            field_name = field['field name']
            field_length = field['field length']

            

            #here we are using while True because we want user to keep on entring the value unless it is a correct value meaning it should not be greater than provided length
            while True:
                    field_value = input(f"'{field_name}' : ")
                    if len(field_value) > field_length:
                        print(f"Value exceeds the maximum length of {field_length} characters. Please enter a shorter value.")
                        #continue
                    else:
                        new_record[field_name] = field_value #new record is a dictionery which was initilized when outer while loop start
                        break
                    
        
        data.append(new_record) #data is a list and dict named new_record is appanended to the list
        print("Record added successfully.")
        print("*" * 100)

        # asking user if he wants to enter more or not
        choice = input("Do You want to add Another Record [Y\\n] ? :")
        if choice.lower() == 'n':
            break


def edit_record(metadata, data):
    records = data
    view_record(metadata, data)
    
    if not records:
        print("No records to edit.")
    else:
        record_index = input("Enter the record number to edit (or press enter to cancel): ")
        if record_index.isdigit():
            record_index = int(record_index) - 1

            if 0 <= record_index < len(records):
                record = records[record_index]

                for field in metadata:
                    field_name = field['field name']
                    field_length = field['field length']
                    current_value = record[field_name]

                    while True:
                        new_value = input(
                            f"Current '{field_name}': {current_value}. Enter new value (max length {field_length}): ")
                        if new_value and len(new_value) > field_length:
                            print(
                                f"Value exceeds the maximum length of {field_length} characters. Please enter a shorter value.")
                        else:
                            if new_value:
                                record[field_name] = new_value
                            print("Record updated successfully.")
                            break
            else:
                print("Invalid record number.")



def del_record(metadata, data):
    '''Display All record and ask user to enter record no which he want to delete and pop that record from list if record no doesnot exist show message that Invalid record'''

    records = data
    view_record(metadata, data) # calling view record function

    if not records: # because the empty list/string/tuple/dict return false or evaluate on false
        print("No records to delete.")
    else:
        record_index = input("Enter the record number to delete (or press Enter to cancel): ")
        if record_index.isdigit():
            record_index = int(record_index) - 1 #because user counting start from  one while indexing is python start from 0
            if 0 <= record_index < len(records): #checking that record_index should be valid 
                records.pop(record_index)
                print("Record deleted successfully.")
            else:
                print("Invalid record number.")



def view_record(metadata, data):
    '''Take data and metadata as input use metadata to extract field and lenght by using these two arguments create a list of string with padding(get from length) in it then insert another element sno in the list and then use .join method to make a string separated by | (pipe) and print that header   '''

    # printing header
    # Extracting headers and their lengths
    headers = [field['field name'] for field in metadata]
    lengths = [field['field length'] for field in metadata]

    list_headerContent= [f"{header:<{length}}" for header, length in zip(headers, lengths)] #using list comprehension to make a list of strings with padding(field and length)
    list_headerContent.insert(0,f'{"S.No":<7}') #adding s.no with padding of 7 to list 0th index 

    header_row = "| " + " | ".join(list_headerContent) + " |"
    print("-" * len(header_row))
    print(header_row)
    print("-" * len(header_row))

    # body printing
    count = 0
    for record in data: #here data is list of dict so record contain a dict
        count += 1
        list_rowContent  = [f"{record[header]:<{length}}" for header, length in zip(headers, lengths)]
        list_rowContent.insert(0,f"{count:<7}")
        row = "| " + " | ".join(list_rowContent) + " |"
        print(row)
    print("-" * len(header_row))



def search_record(metadata,data):

    records = data
    print("On Which attritude you want to find the record: ")

    dic_choice={}
    
    for index,dic in enumerate(metadata,start=1):
        dic_choice.update({index:f'{dic['field name']}'})  #making a dictionery with key is the serial no of fields in string form so that user can type only no of field not the field name 
        print(f"{index} : {dic['field name']}")

    choice = input("Enter you choice: ")

    
# here i am first checking that choice is digit or not if it is digt convert it into interger now check weather that integer is less than or eqal to len of dic_choice(which is a dict containing key as number and value as name of field extracted from metadata). then we are looping over that dictionery if user choice matches with the key in that field. ask user to enter the value he wnat to find in that field which he selected through his choice.
# now if the value which he wnat to find in that field is found print the entire record 


    
    print('*'*100)
    if choice.isdigit():
        choice  = int(choice)    
        if 0 < choice <= len(dic_choice):
            
            for keys,values in dic_choice.items():
                    
                    if choice == keys:
                        finding = input(f"Enter The value you want to find in field of {values}: ")
                        is_record_found = False # inintially no record found therefore Flase but if found make it True otherwaise it will remains False
                        serial_no = 0 #for serial no 
                        for dic in records: #dic conatine the dict of each record
                                
                                serial_no +=1 #incrementing the value of serial no for each iteration
                                
                                if dic[values] == finding: #here value contain that field name which is chosen by user so for every dic in records f
                                    print("="*70)
                                    print("Record is found.............")
                                    print(f'S No.{serial_no}')
                                    is_record_found = True
                                    for key,value in dic.items():
                                        print(f"{key} : {value}")
                                    print("="*70)
                                    

                        if not is_record_found:
                            print("Sorry! Record Not Found.............")        
        else:
            print("Invalid Choice")
    else:
        print("Plz write integer value")
        
    print('*'*100)



def display_all_databases(databases):
    print("="*80)

    for index,database in enumerate(databases,start=1):
        print("Avaliable DataBases are :")
        print(f"{index}:{database}")

        



