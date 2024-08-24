# ============== TE WAIHORA FARM MANAGEMENT SYSTEM ==============
# Student Name: 
# Student ID : 
# ================================================================
 
from datetime import datetime,timedelta


# {mob_name: [list of stock IDs]}
mobs = {
    "R1-2": [932, 343, 786, 801, 878, 947, 951, 901, 789, 899, 888],
    "R3": [816, 810, 802, 800, 833, 777, 798],
    "Bulls": [121, 196]
}
# {paddock_name: {paddock_details}}
paddocks = {
    "Corner": {'area':1.4, 'dm/ha': 1850, 'total dm':2590, 'mob':None, 'stock num': 0},
    "Back": {'area':0.8, 'dm/ha': 2150, 'total dm':1760, 'mob':'R1-2', 'stock num': 11},
    "Front": {'area':1.6, 'dm/ha': 2000, 'total dm':3200, 'mob':'R3', 'stock num': 7},
    "Barn": {'area':0.5, 'dm/ha': 2200, 'total dm':1100, 'mob':'Bulls', 'stock num': 2}
}


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
	[802, 'R3', datetime(2022,8,28), 1, 529.5],  # date corrected from 25/8/2022
	[951, 'R1-2', datetime(2023,7,25), 1, 295.7],
	[901, 'R1-2', datetime(2023,8,4), 1, 288.7],
	[800, 'R3', datetime(2022,9,6), 1, 521.1],
	[789, 'R1-2', datetime(2023,9,14), 0, 260],
	[899, 'R1-2', datetime(2023,8,27), 0, 274.7], # date corrected from 24/8/2023
	[833, 'R3', datetime(2022,9,9), 1, 519],
	[196, 'Bulls', datetime(2023,7,4), 1, 522],
	[777, 'R3', datetime(2022,9,20), 1, 511.3],
	[888, 'R1-2', datetime(2023,9,23), 0, 253.7],
	[798, 'R3', datetime(2022,8,13), 2, 537.9]
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

