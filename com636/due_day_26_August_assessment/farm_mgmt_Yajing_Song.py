# ============== TE WAIHORA FARM MANAGEMENT SYSTEM ==============
# Student Name:Yajing Song
# Student ID : 1162200
# ================================================================
 
from datetime import datetime,timedelta     # datetime module is required for working with dates

import farm_data    # Makes the variables and function in farm_data.py available in this code


# Global variable values that can be referred to throughout your code.  
current_date = datetime(2024,8,26)
# Do not change these values:
pasture_growth_rate = 65    #kg DM/ha/day
stock_growth_rate = 0.7     #kg per day
stock_consumption_rate = 14 #kg DM/animal/day
earliest_birth_date = "1/06/2022"
weight_range = (250,700)

# Collection variables from farm_data.py are available in this code (renamed here to remove the 'farm_data.' prefix).
mobs = farm_data.mobs
paddocks = farm_data.paddocks
stock = farm_data.stock

# Functions from farm_data.py are available in this code (renamed here to remove the 'farm_data.' prefix).
next_id = farm_data.next_id
display_formatted_row = farm_data.display_formatted_row
pasture_levels = farm_data.pasture_levels


def list_all_stock():
    """
    Lists stock details (except birth date).
    This is an example of how to produce basic output."""
    format_str = "{: <5} {: <7} {: <5} {: <5}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
    display_formatted_row(["ID","Mob","Age","Weight"],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
    for animal in stock:
        id = animal[0]
        mob = animal[1]
        age = animal[3]
        weight = animal[4]
        display_formatted_row([id,mob,age,weight],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    input("\nPress Enter to continue.")

def list_stock_by_mob():
    """
    Lists stock details (including birth date), grouped by mob name."""
    # Get the mob names from the mobs dictionary

    mob_keys = mobs.keys()
    # for each mob name, display the stock which belong to that mob
    for mob in mob_keys:
        print("\nMob:", mob)
        format_str = "{: <8} {: <8} {: <5} {: ^10} {: <10}"            # Use the format_str for column headers and rows to ensure consistent spacing. 
        display_formatted_row(["Mob","ID","Birth Date","Age","Weight",],format_str)     # Use the display_formatted_row() function to display the column headers with consistent spacing
        for animal in stock:
            if animal[1] == mob:
                id = animal[0]
                mob = animal[1]
                age = animal[3]
                weight = animal[4]
                birth_date = animal[2].strftime("%d/%m/%Y")
                display_formatted_row([mob,id,birth_date,age,weight],format_str)     # Use the display_formatted_row() function to display each row with consistent spacing
    print("\nStock grouped by mob:", mob_keys)
    input("\nPress Enter to continue.")

def list_paddock_details():
    """
    List the paddock names and all details."""
    for key in sorted(paddocks):
        print(f"\n{key:^50}") 
        print(f"{"area":<5}  {"dm/ha":^10}  {"total dm":<10}  {"mob": ^10}  {"stock num":<5}")
        value = paddocks[key]
        outter_value = value.values()
        # for outter_value in inner_value:
        # conver dic values to list
        outter_value = list(outter_value)
        print(f"{outter_value[0]:<5}  {outter_value[1]:^10}  {outter_value[2]:^8}  {str(outter_value[3]): ^13}  {outter_value[4]:^9}")
    input("\nPress Enter to continue.")


def move_mobs_between_paddocks(paddocks):
    """
    Change which paddock each mob is in. """
    # use while loop to guide our user to input the mob name and paddock name
    # when the user enters X(which is upper case or lower case), the system will exit the loop
    # function to display the mob names
    response = ""
    while response.upper() != "X":
        # firstly we need to display the mob names and paddock names
        mob_keys = mobs.keys()
        paddock_keys = paddocks.keys()
        paddock_keys = list(paddock_keys)
        mob_keys = list(mob_keys)
        # displat them in a better format
        for index,mob in enumerate(mob_keys):
            print(f"\n{index}: {mob}")
        # ask the user to input the mob name
        mob_name = input("\nEnter the mob index to move (or X to exit): ")
        # if the user enters X, exit the loop
        if mob_name.upper() == "X":
            break
        #  incorrect mob_name index, ask the user to enter the mob name again
        if mob_name < "0" or mob_name > str(len(mob_keys)-1):
            print("\n Mob index not found.")
            continue
        # display the paddock names
        for index,paddock in enumerate(paddock_keys):
            # if the paddock is empty mark it as available,if not mark it as occupied
            if paddocks[paddock]['mob'] == None:
                status = "Available"
            else:
                status = "Occupied"
            print(f"\n {index}: {paddock} ({status})")
        # ask the user to input the paddock name
        paddock_name = input("Enter the paddock index to move to (or X to exit): ")
        # if the user enters X, the system will exit the loop
        if paddock_name.upper() == "X":
            break
        #  incorrect paddock index, ask the user to enter the paddock name again
        if paddock_name < "0" or paddock_name > str(len(paddock_keys)-1):
            print("\n Paddock index not found.")
            continue
        
        # if the paddock is occupied, ask the user to enter the paddock name again
        if paddocks[paddock_keys[int(paddock_name)]]['mob'] != None:
            print("\n Paddock is occupied.")
            continue
        # update the stock number in the paddock where the mob was located
        for key in paddocks:
            if paddocks[key]['mob'] == mob_keys[int(mob_name)]:
                paddocks[key]['stock num'] = 0
                paddocks[key]['mob'] = None
        # if the paddock is available, move the mob to the paddock
        paddocks[paddock_keys[int(paddock_name)]]['mob'] = mob_keys[int(mob_name)]
        # update the stock number in the paddock
        paddocks[paddock_keys[int(paddock_name)]]['stock num'] = len(mobs[mob_keys[int(mob_name)]])
        print(f"\nMob {mob_keys[int(mob_name)]} moved to paddock {paddock_keys[int(paddock_name)]}")

   
def add_new_stock(stock):
    """
    Add a new animal to the stock list."""
    # Ask the user to enter details of a new stock animal
    
    response = ""
    while response.upper() != "X":
        # The new cattle ID must be unique (using provided next_id() function)
        new_id = next_id(stock)
        print(f"\nNew animal ID: {new_id}")
        #[816, 'R3', datetime(2022,7,15), 2, 558.2],
        # Birth date should be entered in an appropriate NZ date format and no earlier than the value in earliest_birth_date variable
        birth_date = input(f"\nEnter the birth date (dd/mm/yyyy):")
        # validate is a date
        try:
            datetime.strptime(birth_date, "%d/%m/%Y")
        except ValueError:
            print("\nInvalid date.")
            continue

        # if the birth date is earlier than the earliest_birth_date, ask the user to enter the birth date again
        if datetime.strptime(birth_date, "%d/%m/%Y") < datetime.strptime(earliest_birth_date, "%d/%m/%Y"):
            print(f"\nBirth date too early. must be no earlier than {earliest_birth_date}")
            continue
        # if the birth date is later than the current date, ask the user to enter the birth date again
        if datetime.strptime(birth_date, "%d/%m/%Y") > current_date:
            print("\nBirth date too late. must be no later than the current date")
            continue
        # Age must be calculated from the birth date entered (as whole years as at current_date)
        age = current_date.year - datetime.strptime(birth_date, "%d/%m/%Y").year
        # Adjust if the birthdate has not yet occurred this year
        if (current_date.month, current_date.day) < (datetime.strptime(birth_date, "%d/%m/%Y").month,datetime.strptime(birth_date, "%d/%m/%Y").day):
                age -= 1
        print(f"\nAge: {age}")
        # Animal weight must be between the values in weight_range variable.
        weight = input("\nEnter the weight (kg):")
        # validate is a number
        try:
            weight = float(weight)
        except ValueError:
            print("\nInvalid weight.")
            continue
        if weight < weight_range[0] or weight > weight_range[1]:
            print(f"\nWeight out of range. Must be between {weight_range[0]} and {weight_range[1]}")
            continue
        # After adding each new stock animal, update the stock ID numbers in mobs and the stock_num in each paddock.
        mob_keys = mobs.keys()
        # list mobs and ask the user to enter the mob index to move it to the mob
        for index,mob in enumerate(mob_keys):
            print(f"\n{index}: {mob}")
        mob_name = input("\nEnter the mob index to move to ")
        # if the mob index is not found, ask the user to enter the mob index again
        if mob_name < "0" or mob_name > str(len(mob_keys)-1):
            print("\n Mob index not found.")
            continue
        mob_keys = list(mob_keys)
        # update the mobs
        mobs[mob_keys[int(mob_name)]].append(new_id)
        # update the paddocks
        for key in paddocks:
            if paddocks[key]['mob'] == mob_keys[int(mob_name)]:
                paddocks[key]['stock num'] += 1
        # add the new stock to the stock list
        stock.append([new_id,mob_keys[int(mob_name)],datetime.strptime(birth_date, "%d/%m/%Y"),age,weight])
        # show success message
        print(f"\nNew animal added to stock list with ID: {new_id}")
        # print the stock list
        list_all_stock()
        list_stock_by_mob()
        list_paddock_details()
        response = input("\nPress Enter to continue or X to exit.")


def move_to_next_day(stock, paddocks):
    """
    Increase the current date by one day, making other required changes.
    """
    # Use the function in the line below to return 'total dm' and 'dm/ha' values for each paddock:  
    #     pasture_levels(area,stock,total_dm,pasture_growth_rate,stock_consumption_rate)      
    # moves current_date forward by one day.
    global current_date
    current_date += timedelta(days=1)
    print(f"\nCurrent date: {current_date.strftime('%d/%m/%Y')}")
    #  Stock ages must all be updated for the new date.
    for animal in stock:    
        # compare current date with the birth date
        # update the age by the difference between the current date and the birth date, make it as a whole year
        animal[3] = current_date.year - animal[2].year
        # Adjust if the birthdate has not yet occurred this year
        if (current_date.month, current_date.day) < (animal[2].month, animal[2].day):
             animal[3] -= 1
    #  Paddock pasture levels must be updated for the new date.
    for key in paddocks:
        paddock = paddocks[key]
        area = paddock['area']
        stock = paddock['stock num']
        total_dm = paddock['total dm']
        # get the pasture levels
        result = pasture_levels(area,stock,total_dm,pasture_growth_rate,stock_consumption_rate)
        # update the paddock details
        paddock['total dm'] = result['total dm']
        paddock['dm/ha'] = result['dm/ha']
    print("\nStock ages and paddock pasture levels updated.")
    list_all_stock()
    list_paddock_details()
    input("\nPress Enter to continue.")
    
    




def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TE WAIHORA FARM MANAGEMENT SYSTEM ===")
    print(f"Today is {current_date.strftime('%d/%m/%Y')}")
    print(" 1 - List All Stock")
    print(" 2 - List Stock Grouped by Mob")
    print(" 3 - List Paddock Details")
    print(" 4 - Move Mobs Between Paddocks")
    print(" 5 - Add New Stock")
    print(" 6 - Move to Next Day")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------


# Don't change the menu numbering or function names in this menu.
# Although you can add arguments to the function calls, if you wish.
# Repeat this loop until the user enters an "X" or "x"
response = ""
while response.upper() != "X":
    disp_menu()
    # Display menu for the first time, and ask for response
    response = input("Please enter menu choice: ")    
    if response == "1":
        list_all_stock()
    elif response == "2":
        list_stock_by_mob()
    elif response == "3":
        list_paddock_details()
    elif response == "4":
        move_mobs_between_paddocks(paddocks)
    elif response == "5":
        add_new_stock(stock)
    elif response == "6":
        move_to_next_day(stock,paddocks)
    # The user can enter "X" or "x" to exit the program.
    elif response.upper() == "X":
        print("=== Exiting the program ===")
        break   
    else:
        print("\n*** Invalid response, please try again (enter 1-6 or X)")


print("\n=== Thank you for using Te Waihora Farm Management System! ===\n")