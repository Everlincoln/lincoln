# print("How's thing?")

# print("Great thanks.")
# print("What about you")

# staff_name = "Mike Jones"
# print(staff_name.split())

# staff_name = "Sir,Mike,Jones"
# print(staff_name.split(','))
# print(staff_name.replace(',',''))

# first_name = "Mike"
# family_name = "Jones"
# print("Dear" + ' ' + first_name + ' ' + family_name + ',')
# print("Dear " + first_name + ' ' + family_name + ',')

# num = 1.23456789
# print(f"{num:.3f}") 

#AREA OF A ROOM
# Uses isnumeric() to check if values are numbers
# BUT isnumeric() can't handle decimal points (or negative signs)

#Declare a validInt Boolean flag and set it to false to satisfy the while clause condition for the first iteration
# validEntry = False
# while not validEntry:
#     #The user is prompted to enter the inputs
#     length_input = input("Please enter length of the room in metres: ")
#     width_input = input("Please enter width of the room in metres: ")
#  	#Checking that both inputs are numeric - BUT NOTE: isnumeric() returns false if string contains '.' or '-' characters
#     if length_input.isnumeric() and width_input.isnumeric():
#         #The entry strings are converted to float now that it is confirmed that they are both numbers
#         length=float(length_input)
#         width=float(width_input)
#         if length > 0 and width > 0:    #Need to check that both are numbers before checking these conditions
#             #The flag is set to true if the both entries are numbers and greater than zero
#             validEntry = True
#     #Display an error message if validEntry is still false. (IF statements could be used to provide more specific error messages.)
#     if not validEntry:
#         print("Invalid number entered. Both height and width must be numbers greater than zero.")

# #Calculate the area of the room - will only exit while loop once both numbers are numeric
# area = length * width
# #This statement is printed if the input entered by the user is a number
# print(f"The room is {str(length)} m long x {str(width)} m wide.\nThe area of the room is {str(area)} sq. m.")


# #Comparing isdigit(), isnumeric() and isdecimal() - they are mostly the same, apart from unusual characters like fractions ⅔ or exponents 2²
# '''
# numbers=["0","1","10","999","-1","1.2","1.1.1",".1","abc","a1","⅔","2²","D"]

# #Notice how the output from each method is the same for normal numbers
# for n in numbers:
#     print(f'{n}.isdigit(): {n.isdigit()}')    
#     print(f'{n}.isnumeric(): {n.isnumeric()}')    
#     print(f'{n}.isdecimal(): {n.isdecimal()}')
#     print()
#     '''

#AREA OF A ROOM
# Use function to remove any leading negative sign '-' and the first decimal point '.'
# Then use isdigit() to check if what is left is a non-negative whole number

# numbers=["0","1","10","999","-1","1.2","1.1.1",".1","abc","a1","⅔","2²","D"]

# for n in numbers:
#     print(f'{n}.isdigit(): {n.isdigit()}')    
#     print(f'{n}.isnumeric(): {n.isnumeric()}')    
#     print(f'{n}.isdecimal(): {n.isdecimal()}')
#     print()

def stripDecNeg(number_string):
    if number_string[0]=='-':
        stripped=number_string[1:]
    else:
        stripped=number_string
    #Or shorter than the above:   stripped=number_string.lstrip('-')
    stripped=stripped.replace('.','',1)
    return stripped

#Declare a validInt Boolean flag and set it to false to satisfy the while clause condition for the first iteration
validEntry = False
while not validEntry:
    #The user is prompted to enter the inputs
    length_input = input("Please enter length of the room in metres: ")
    width_input = input("Please enter width of the room in metres: ")
 	#Checking that both inputs are numeric - BUT NOTE: isnumeric() returns false if string contains '.' or '-' characters


    if stripDecNeg(length_input).isdigit() and stripDecNeg(width_input).isdigit():
        #The entry strings are converted to float now that it is confirmed that they are both numbers
        length=float(length_input)
        width=float(width_input)
           #Need to check that both are numbers before checking these conditions
            #The flag is set to true if the both entries are numbers and greater than zero
        validEntry = True
    #Display an error message if if length > 0 and width > 0: validEntry is still false. (IF statements could be used to provide more specific error messages.)
    if not validEntry:
        print("Invalid number entered. Both height and width must be numbers greater than zero.")

#Calculate the area of the room - will only exit while loop once both numbers are numeric
area=length*width

#This statement is printed if the input entered by the user is a number
print(f"The room is {str(length)} m long x {str(width)} m wide.\nThe area of the room is {str(area)} sq. m.")
print()