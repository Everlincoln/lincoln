# ============== TE WAIHORA FARM MANAGEMENT SYSTEM ==============
# Alternative data file for testing.
# This file is the same structure, with the same type of data, but the mobs, paddocks and stock are different.
# Your code should work with this file too.

# Rename the other file to something else, then rename me to farm_data.py.

# ===============================================================
 
from datetime import datetime,timedelta


# {mob_name: [list of stock IDs]}
mobs = {
    "Mob 1": [1003,1001,1004,1007,1002,1005,1006,1008],
    "Mob 2": [1013,1009,1014,1010,1012,1011],
    "Mob 3": [1017,1020,1016,1019,1015,1018],
    "Mob 4": [1023,1022,1026,1024,1021,1025]
}


# {paddock_name: {paddock_details}}
paddocks = {
    "P1": {'area':1.1, 'dm/ha': 2350, 'total dm':2585, 'mob': 'Mob 3', 'stock num': 6},
    "P2": {'area':1.3, 'dm/ha': 2220, 'total dm':2886, 'mob': None, 'stock num': 0},
    "P3": {'area':1.3, 'dm/ha': 2130, 'total dm':2769, 'mob': None, 'stock num': 0},
    "P4": {'area':1.3, 'dm/ha': 1850, 'total dm':2405, 'mob': 'Mob 1', 'stock num': 8},
    "P5": {'area':1, 'dm/ha': 1980, 'total dm':1980, 'mob': 'Mob 4', 'stock num': 6},
    "P6": {'area':0.8, 'dm/ha': 1500, 'total dm':1200, 'mob': 'Mob 2', 'stock num': 6}
}


# [id, mob_name, birth_date, age_yrs ,weight]
stock = [
    [1017, 'Mob 3', datetime(2023,7,15), 1, 522],
    [1023, 'Mob 4', datetime(2023,7,15), 1, 522],
    [1020, 'Mob 3', datetime(2022,8,27), 1, 533.7],
    [1016, 'Mob 3', datetime(2022,9,30), 1, 509.9],
    [1022, 'Mob 4', datetime(2022,9,30), 1, 509.9],
    [1003, 'Mob 1', datetime(2023,9,17), 0, 263.5],
    [1013, 'Mob 2', datetime(2022,9,14), 1, 521.1],
    [1009, 'Mob 2', datetime(2023,9,24), 0, 258.6],
    [1026, 'Mob 4', datetime(2023,9,24), 0, 258.6],
    [1014, 'Mob 2', datetime(2023,9,20), 0, 261.4],
    [1001, 'Mob 1', datetime(2022,7,25), 2, 556.8],
    [1010, 'Mob 2', datetime(2022,9,9), 1, 524.6],
    [1004, 'Mob 1', datetime(2022,8,16), 2, 541.4],
    [1019, 'Mob 3', datetime(2023,10,6), 0, 250.2],
    [1007, 'Mob 1', datetime(2022,8,24), 2, 842.3],
    [1024, 'Mob 4', datetime(2022,8,24), 2, 842.3],
    [1002, 'Mob 1', datetime(2023,8,22), 1, 281.7],
    [1005, 'Mob 1', datetime(2023,7,29), 1, 298.5],
    [1015, 'Mob 3', datetime(2023,9,10), 0, 268.4],
    [1021, 'Mob 4', datetime(2023,9,10), 0, 268.4],
    [1006, 'Mob 1', datetime(2023,9,26), 0, 257.2],
    [1018, 'Mob 3', datetime(2022,10,15), 1, 499.4],
    [1008, 'Mob 1', datetime(2023,9,3), 0, 273.3],
    [1025, 'Mob 4', datetime(2023,9,3), 0, 273.3],
    [1012, 'Mob 2', datetime(2023,8,13), 1, 288],
    [1011, 'Mob 2', datetime(2023,8,7), 1, 292.2]
]

def next_id(stock):
    """
    Pass in the stock list and this will return the next available ID as a new integer value
    that is one higher than the current maximum ID number in the list."""
    max_id = 0
    # Loop through all stock setting max_id to find the highest id value
    for animal in stock:
        id = animal[0]
        if id > max_id:     # max_id stores the highest value of id found so far
            max_id = id
    # Add 1 to max_id to return an unused ID
    return max_id + 1


def display_formatted_row(row, format_str):
    """
    row is a list or tuple containing the items in a single row.
    format_str uses the following format, with one set of curly braces {} for each column:
       eg, "{: <10}" determines the width of each column, padded with spaces (10 spaces in this example)
       <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
    The following example is for 3 columns of output: left-aligned 5 characters wide; centred 10 characters; right-aligned 15 characters:
        format_str = "{: <5}  {: ^10}  {: >15}"
    Make sure the column is wider than the heading text and the widest entry in that column,
        otherwise the columns won't align correctly.
    You can also pad with something other than a space and put characters between the columns, 
        eg, this pads with full stops '.' and separates the columns with the pipe character '|' :
           format_str = "{:.<5} | {:.^10} | {:.>15}"
    """
    # Convert a tuple to a list, to allow updating of values
    if type(row) == tuple: 
        row = list(row)
    # Loop through each item in the row, changing to "" (empty string) if value is None and converting all other values to string
    #   (Extra info:  enumerate() places a loop counter value in index to allow updating of the correct item in row)
    for index,item in enumerate(row):
        if item is None:      # Removes any None values from the row_list, which would cause the print(*row_list) to fail
            row[index] = ""       
        else:    
            row[index] = str(item)
    # Apply the formatting in format_str to all items in row
    print(format_str.format(*row))


def pasture_levels(area,stock_num,total_dm,pasture_growth_rate,stock_consumption_rate):
    """
    Calculate total pasture (in kg DM) for a paddock based on area, growth rate and stock number.
    Arguments: area (ha), stock number, total DM (kg), pasture growth rate (kg DM/ha/day), stock_consumption rate (kg DM/animal/day) """
    growth = area * pasture_growth_rate
    consumption = stock_num * stock_consumption_rate
    total_dm = total_dm + growth - consumption
    dm_per_ha = round(total_dm / area,2)
    return {'total dm':total_dm, 'dm/ha':dm_per_ha}

