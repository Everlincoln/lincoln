# ============== TE WAIHORA FARM MANAGEMENT SYSTEM ==============
# Student Name:Yajing Song
# Student ID :
# ================================================================
 
from datetime import datetime,timedelta     # datetime module is required for working with dates

import farm_data    # Makes the variables and function in farm_data.py available in this code

# {mob_name: [list of stock IDs]}
mobs = {
    "R1-2": [932, 343, 786, 801, 878, 947, 951, 901, 789, 899, 888],
    "R3": [816, 810, 802, 800, 833, 777, 798],
    "Bulls": [121, 196]
}

R1 = []
R3 = []
Bulls = []

# [id, mob_name, birth_date, age_yrs ,weight]
stock = [
	[816, 'R3', datetime(2022,7,15), 2, 558.2],
	[932, 'R1-2', datetime(2023,8,10), 1, 284.5],
	[343, 'R1-2', datetime(2023,9,1), 0, 269.1],
	[810, 'R3', datetime(2022,8,12), 2, 538.6],
	[786, 'R1-2', datetime(2023,7,16), 1, 302],
	[801, 'R1-2', datetime(2023,9,12), 0, 261.4],
	[121, 'Bulls', datetime(2022,8,4), 2, 842.3],
	[878, 'R1-2', datetime(2023,9,2), 0, 268.4],
	[947, 'R1-2', datetime(2023,8,30), 0, 270.5],
	[802, 'R3', datetime(2022,8,25), 1, 529.5],
	[951, 'R1-2', datetime(2023,7,25), 1, 295.7],
	[901, 'R1-2', datetime(2023,8,4), 1, 288.7],
	[800, 'R3', datetime(2022,9,6), 1, 521.1],
	[789, 'R1-2', datetime(2023,9,14), 0, 260],
	[899, 'R1-2', datetime(2023,8,24), 0, 274.7],
	[833, 'R3', datetime(2022,9,9), 1, 519],
	[196, 'Bulls', datetime(2023,7,4), 1, 522],
	[777, 'R3', datetime(2022,9,20), 1, 511.3],
	[888, 'R1-2', datetime(2023,9,23), 0, 253.7],
	[798, 'R3', datetime(2022,8,13), 2, 537.9]
]
def stock_group(group,name):
    print(f"{name:^50}")
    print(f"{'ID':<5}  {"mob_name":<10}  {"birth_date":<10}  {"age_yrs":<10}  {"weight":<5}")
    print("--------------------------------------------------")
    for item in group:
        print(f"{item[0]:<5}  {item[1]:<10}  {item[2].strftime('%d-%m-%Y'):<10}  {item[3]:<10}  {item[4]:<5}")


for item in stock:
    if item[1] == "R1-2":
        R1.append(item)
    elif item[1] == "R3":
        R3.append(item)
    elif item[1] == "Bulls":
        Bulls.append(item)

stock_group(R1,"R1-2")
stock_group(R3,"R3")
stock_group(Bulls,"Bulls")

    
# {paddock_name: {paddock_details}}
paddocks = {
    "Corner": {'area':1.4, 'dm/ha': 1850, 'total dm':2590, 'mob':None, 'stock num': 0},
    "Back": {'area':0.8, 'dm/ha': 2150, 'total dm':1760, 'mob':'R1-2', 'stock num': 11},
    "Front": {'area':1.6, 'dm/ha': 2000, 'total dm':3200, 'mob':'R3', 'stock num': 7},
    "Barn": {'area':0.5, 'dm/ha': 2200, 'total dm':1100, 'mob':'Bulls', 'stock num': 2}
}


def paddocks_dictionary():
    for key in sorted(paddocks):
        print(f"{key:^50}")
        print(f"{'area':<5}  {"dm/ha":<10}  {"total dm":<10}  {"mob":<10}  {"stock num":<5}")
        print("-----------------------------------------------------")
        value = paddocks[key]
        outter_value = value.values()
        # for outter_value in inner_value:
        # conver dic values to list
        outter_value = list(outter_value)
        print(f"{outter_value[0]:<5}  {outter_value[1]:<10}  {outter_value[2]:<10}  {str(outter_value[3]):<10}  {outter_value[4]:<5}")

paddocks_dictionary()


    # print(f"{'Paddock Name':<10}  {'Area':<5}  {'DM/ha':<5}  {'Total DM':<5}  {'Mob':<5}  {'Stock Num':<5}")
    # print(f"{key:<10}  {paddocks[key]['area']:<5}  {paddocks[key]['dm/ha']:<5}  {paddocks[key]['total dm']:<5}  {paddocks[key]['mob']:<5}  {paddocks[key]['stock num']:<5}")




# for item in stock:

# sorted_paddocks = sorted(paddocks.items())
# print("Paddock Name  Area  DM/ha  Total DM  Mob  Stock Num")
# print(f"{'Paddock Name':<10}  {'Area':<5}  {'DM/ha':<5}  {'Total DM':<5}  {'Mob':<5}  {'Stock Num':<5}")
# print(sorted_paddocks)


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

