sales# # data =["a","b","c"]

# # ctr =0
# # while ctr<=len(data)-1:
# #  print(data[ctr])    
# # ctr+= 1

# response = input(" Enter a menu number:")

# while response != "X":
#     if response == "1":
#         print("response")
#     if response == "2":
#         print("response")
# response = input(" Enter a menu number:")


# print("Goodbye")

# data = ["apple","pear","persimmon","carrot"]

# for item in data:
#     print(item)
# for ctr in range(1,6,2):
#         print(ctr)

# data = ["apple","pear","persimmon","carrot"]

# ctr = 0
# while ctr < len(data)-1:
#     print(data[ctr])
#     ctr+=1
# pass
# def my_function():
#     print("This is my function")

# my_function()

# def my_function(parmeter):
#     changed_parmeter =  parmeter.upper()
#     return changed_parmeter

# arguement = "Value passed to the function"
# returned_value = my_function(argument)

# print(returned_value)

# def myfunc():
#   x = 300
#   def myinnerfunc():
#     print(x)
#   myinnerfunc()

# myfunc()

# def my_function(parameter):
#    changed_parameter = parameter.upper()
#    return changed_parameter

# argument = "Value passed to the function"
# returned_value = my_function(argument)
# print(returned_value)

# payroll_details = [
#     ("john",55000,85000),
#     ("Wei",123000,49000),
#     ("Rima",75000,222000),
#     ("Linda",33000,50000)
#     ]

# def total_pay_fn(salary,):
#     if sales >= 100000:
#         bonus = 2000
#     elif sales >= 50000:
#         bonus = 1000
#     else:
#         bonus = 0
#     total_pay = salary + bonus
#     return total_pay

# for employee in payroll_details:
#     total_pay = total_pay_fn(employee[1],employee[2])
#     print("The total pay is:" + str(total_pay))

# input_salary = input("What is your salary?")
# input_sales = input("What is the sales figure?")

# total_pay = total_pay_fn(int(input_salary),int(input_sales))
# print("The total pay is:" + str(total_pay))


# my_string = 'Hello world!'
# another_string = "123" 

# mysql = """selct * 
#             from my_table 
#             where id = 1;""" 解释

# ptint("\nnext line")解释

# staff_name = "Mike Jones"

# print(staff_name[3:])

# print(len(staff_name))

# for letter in staff_name:
#     print(letter)

# print(staff_name.lower())

# if "JON" in staff_name.upper():
#     print("Found")

# print(staff_name.split('.'))解释

# print(staff_name.replace('.',','))解释

# first_name = "Mike"
# family_name = "Jones"

# # print("Dear" + first_name +''+ family_name +",")没空格

# # print(f"Dear {first_name} {family_name},")有空格

# print(f"Dear {first_name} {family_name},(num:.3f)")用于将 num 变量格式化为浮点数，小数点后保留三位

# length = input("What is the length in meters?")
# width = input ("What is the width in meters?")

# area = int(length) * int(width)

# print(area)

# try:
#     print("a"+1)
# except:
#     print("This produces an error ")


# Function from: https://www.geeksforgeeks.org/introduction-to-levenshtein-distance/

# def levenshteinRecursive(str1, str2, m, n):
#     #print(m,n)
#     # str1 is empty
#     if m == 0:
#         return n
#     # str2 is empty
#     if n == 0:
#         return m
#     if str1[m - 1] == str2[n - 1]:
#         return levenshteinRecursive(str1, str2, m - 1, n - 1)
#     return 1 + min(
#           # Insert     
#         levenshteinRecursive(str1, str2, m, n - 1),
#         min(
#               # Remove
#             levenshteinRecursive(str1, str2, m - 1, n),
#           # Replace
#             levenshteinRecursive(str1, str2, m - 1, n - 1))
#     )
 
# # Drivers code
# str1 = "bad"
# str2 = "bid"
# distance = levenshteinRecursive(str1, str2, len(str1), len(str2))
# print("Levenshtein Distance:", distance)

# my_string = "The quick brown fox jumps over the lazy dog."
# split_string = my_string.split()
# for ctr in range(1,len(split_string)):
#     str1 = split_string[ctr - 1]
#     str2 = split_string[ctr + 0]
#     distance = levenshteinRecursive(str1, str2, len(str1), len(str2))
#     print(str1 + ' vs ' + str2,'=', distance)




print("\n------- Usual (and safest) way to use a function: pass value & return value -------")

def x_pass_value(a):
    a = 333         # a only exists inside this function
    return a

x = 10
y = x_pass_value(x)
print("Value passed:",x)
print("Value returned:",y)

print("\n------- Refer to global variable in function -------")

def x_global():
    print("In x_global():",x)       # prints the global x variable
    return x                        # also returns the value of x

x = 10
print("Main, before function:",x)
y = x_global()                  # y gets the value returned from the function
print("Main, after function:", y)

print("\n-------- Create new version of x in function ----------------------------")

def x_local():
    # print("Global x in function:",x)      # Causes an error because x is defined locally below
    x = 400                     # assigning a value locally creates a new x available only inside the function
    print("In x_local:",x)

x = 10
print("Main, before function:",x)
x_local()
print("Main, after function:",x)           # the global value of x hasn't changed (= 10)

print("\n--------- Change global x in function---------------------------")

def x_change_global():
    global x                    # same as above, but this time we say we are using the global x
    x = 400                     # this changes the global x
    print("In x_change_global:",x)

x = 10
print("Main, before function:",x)
x_change_global()
print("Main, after function:",x)    # now x = 400 from change to global variable in the function

print("")





