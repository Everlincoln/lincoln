#AGE NEXT YEAR
# Enter your age and displays your age next year
# Checks for non-negative integer value before proceeding.

#Declare a variable validInt which is also considered as flag and set it to false
validEntry = False
#Consider the while condition to be true and prompt the user to enter the input
while not validEntry:
    #The user is prompted to enter the input
    age_input = input("Please enter your age: ")
 	 #The input entered by the user is checked to see if it’s a digit or a number
    if age_input.isdigit():
        #The flag is set to true if the if condition is true
        validEntry = True
        #The string entered is converted to an integer now that it is confirmed that it is a number
        age=int(age_input)
    else:
        print("Not a valid number. Please re-enter a whole number greater than or equal to zero.")
#This statement is printed if the input entered by the user is a number
print(f"You are {str(age)} years old. Next year you will be {str(age+1)}.")