# ============== TE WAIHORA FARM MANAGEMENT SYSTEM ==============
# Student Name:Yajing Song
# Student ID : 
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
        format_str = "{: <8} {: <8} {: <5} {: ^10} {: <10}"            # Use the same format_str for column headers and rows to ensure consistent spacing. 
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
    # Let the user choose a mob from "mobs" dictionary(user can input number/letter to choose their choice) and to move to a new paddock from "paddocks" dictionary which is not have any mob in it.
    # If the paddock has a mob in it, the user should be informed and asked to choose another paddock.
    mobs_keys = mobs.keys()
    paddocks_keys = paddocks.keys()
    #user can choose a number which is related to the mob name to move the mob to a new paddock
    print ("\nPlease choose a number of the mob to move to a new paddock:")
    print("* * * This is a paddock manu * * *")
    print("1 : R1-2")
    print("2 : R3")
    print("3 : Bulls")
    mob_choice = input("Enter the number of the mob you want to move: ")
    #user can choose a number which is related to the paddock name to move the mob to a new paddock
    print("\n* * * This is a paddock manu * * *")
    # find all the paddocks that do not have a mob in it
    print("\nPlease choose a number of the paddock to move the mob to:")
    for index,key in enumerate(paddocks_keys):
        if paddocks[key]['mob'] == None:
            print(f"{index + 1} : {key}")
    paddock_choice = input("Enter the number of the paddock you want to move the mob to: ")
    # CHange the target paddock to the mob
    paddock_choice = int(paddock_choice)
    mob_choice = int(mob_choice)
    paddock_choice = paddock_choice - 1
    mob_choice = mob_choice - 1
    paddock_key = paddocks_keys[paddock_choice]
    mob_key = list(mobs_keys)[mob_choice]
    # excute the move action
    paddocks[paddock_key]['mob'] = mob_key
    print(f"\nMob {mob_key} has been moved to paddock {paddock_key}")

    input("\nPress Enter to continue.")

   

   
   

    

    





   
   

   
   
    

     

    
   
    
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def add_new_stock(stock):
    """
    Add a new animal to the stock list."""

    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)

def move_to_next_day(stock, paddocks):
    """
    Increase the current date by one day, making other required changes.
    """
    # Use the function in the line below to return 'total dm' and 'dm/ha' values for each paddock:  
    #     pasture_levels(area,stock,total_dm,pasture_growth_rate,stock_consumption_rate)      
    pass  # REMOVE this line once you have some function code (a function must have one line of code, so this temporary line keeps Python happy so you can run the code)


def disp_menu():
    """
    Displays the menu and current date.  No parameters required.
    """
    print("==== WELCOME TE WAIHORA FARM MANAGEMENT SYSTEM ===")
    print("Today is [* * * show current_date here * * *]")
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
    # The user can enter "X" to exit the program.
    elif response.upper() == "X":
        print("=== Exiting the program ===")
        break   
    elif response.upper() != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)")

    print("")


print("\n=== Thank you for using Te Waihora Farm Management System! ===\n")