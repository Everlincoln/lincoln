# print("Hello World")

# vegetable = input("Please enter your name")

# if vegetable == "apple":
#     print("Your name is apple")
# else:
#     print("Your name is not apple")

# this_is_a_number =int(input("Please enter a number:"))
# #print(type(this_is_a_number))

# if this_is_a_number>5:
#     print("The number you entered is greater than 5")
# else:
#     print("The number you entered was 5 or less")
    
# this_is_a_string_variable = "This is a string"
# print(type(this_is_a_string_variable))
# this_is_a_int_variable = 5
# print(type(this_is_a_int_variable))
# this_is_a_float_variable = 1.8
# print(type(this_is_a_float_variable))
# this_is_a_variable = None
# print(type(this_is_a_variable))

# if this_is_a_int_variable >= this_is_a_float_variable:
#     print("Our int is biger than our folat(or equal) ")
# else:
#     print("Our float is biger than our int ")

# shopping_list = []
# # print(type(shopping_list))
# # print(shopping_list)
# item = input("Please enter an item for our shopping list(or X to shop): ")                                 
# while item.upper() !="X":
# #     qty = int (input("How many would you like to buy?:"))
# #     shopping_list.append((item,qty))
# #     item = input("Please enter an item for our shopping list(or X to shop): ")                                                       
# # print(shopping_list)
# # print(len(shopping_list))

# # for list_item in range(len(shopping_list)):
# #     print(shopping_list[list_item])
# # print("=== SOPPING LIST===")
# # for list_item in shopping_list:
# #     print(f"Please buy {list_item[1]} : {list_item[0](s)}")                                                                                                                                           


# # ddata =[("Adam","Chen","123456")
# #         ("Johnny","Smith","12345678")
# #         ("Mike","Brown","123456789" )      
# # ]
# # print(data[0][1])         
# #


# mysql = """select *
#             from table
#             where id = 1;"""   

# print("hello world")
# print("\nnext line")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          

import datetime     # This module is required for date formatting

# Member data:  (ID, group, name, birth_date, city)
member_data = [
    (1,  "Group 4", "Ella Thompson", datetime.datetime(1995, 1, 15), "Auckland"),    
    (2, "Group 1", "Liam Johnson", datetime.datetime(1998, 3, 22), "Wellington"),
    (4, "Group 3", "Aria Ngata", datetime.datetime(2000, 10, 9), "Rotorua"),
    (5, "Group 1", "Xiao Chen", datetime.datetime(1992, 7, 4), "Christchurch"),
    (7, "Group 2", "Pita Rangi", datetime.datetime(1987, 4, 11), "Gisborne"),
    (8, "Group 4", "Olivia Martin", datetime.datetime(1993, 5, 28), "Hamilton"),
    (10, "Group 1", "Hua Zhang", datetime.datetime(1985, 12, 19), "Dunedin"),
    (11, "Group 2", "Mason Taylor", datetime.datetime(1999, 2, 5), "Tauranga"),
    (13, "Group 4", "Anahera Whiti", datetime.datetime(1994, 8, 21), "Napier"),
    (14, "Group 4", "Wei Li", datetime.datetime(1990, 3, 30), "Christchurch"),
    (16, "Group 3", "Jack Williams", datetime.datetime(1996, 6, 14), "Nelson"),
    (17, "Group 1", "Mia Brown", datetime.datetime(2001, 9, 12), "Invercargill"),
    (19, "Group 3", "Tāne Mahuta", datetime.datetime(1988, 11, 7), "Whangarei"),
    (20, "Group 1", "Sarah Wilson", datetime.datetime(1995, 7, 23), "New Plymouth"),
    (22, "Group 2", "Ethan Moore", datetime.datetime(1997, 4, 3), "Hastings"),
    (23, "Group 1", "Sophie Anderson", datetime.datetime(2002, 1, 29), "Lower Hutt"),
    (25, "Group 4", "Nikau Tui", datetime.datetime(1993, 2, 17), "Queenstown"),
    (26, "Group 2", "Lily Jackson", datetime.datetime(1989, 6, 8), "Blenheim"),
    (28, "Group 1", "James Harris", datetime.datetime(1991, 12, 5), "Timaru"),
    (29, "Group 4", "Aroha Rewa", datetime.datetime(1994, 10, 25), "Taupo")
]
groupone = []
group2 = []
group3 = []
group4 = []

def data_member(group,index):
    print(f"Group {index}")
    print(f"{'Name':<20} {'Birth Date':<12} {'City':<20}")
    print("-----------------------------------------------------")
    for item in group:
        print(f"{item[2]:<20} {item[3].strftime('%d-%m-%Y'):<12} {item[4]:<20}")


#sort by groupname
# member_data.sort( key = lambda x: x[1])
# data_member(member_data,1)

for item in member_data:
    if item[1] == "Group 1":
        groupone.append(item)
    elif item[1] == "Group 2":
        group2.append(item)
    elif item[1] == "Group 3":
        group3.append(item)
    elif item[1] == "Group 4":
        group4.append(item)

for item in group1:
    data_member(group1,1)

for item in group2:
    data_member(group2,2)

for item in group3:
    data_member(group3,3)

for item in group4:
    data_member(group4,4)

# response = input("Please enter the group number(1,2) or Q to quit:")

# while response != "Q":
#     if response == "1":
#         print("Group 1")
#         data_member()
#     elif response == "2":
#         print("Group 2")
#     else:
#         print("Please enter a valid group number")
#     response = input("Please enter the group number(1,2) or Q to quit:")
        





   
    