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

shopping_list = []
# print(type(shopping_list))
# print(shopping_list)
item = input("Please enter an item for our shopping list(or X to shop): ").strip()
while item.upper() !="X":
    shopping_list.append(item)
    print(shopping_list)
    item = input("Please enter an item for our shopping list(or X to shop): ").strip()
print(“shopping_list”，shopping_list)
print(len(shopping_list))

