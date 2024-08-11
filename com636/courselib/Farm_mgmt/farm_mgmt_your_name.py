# ============== TE WAIHORA FARM MANAGEMENT SYSTEM ==============
# Student Name: 
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
    input("\nPress Enter to continue.")

def list_paddock_details():
    """
    List the paddock names and all details."""
    input("\nPress Enter to continue.")

def move_mobs_between_paddocks(paddocks):
    """
    Change which paddock each mob is in. """
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
while response != "X":
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
    elif response != "X":
        print("\n*** Invalid response, please try again (enter 1-6 or X)")

    print("")

print("\n=== Thank you for using Te Waihora Farm Management System! ===\n")

