#AGE NEXT YEAR
# Enter your age and displays your age next year
# No data validation - try entering a decimal age or text

#The user is prompted to enter the input
age_input = input("Please enter your age: ")
#The string entered is converted to an integer now that it is confirmed that it is a number
age=int(age_input)
#This statement is printed if the input entered by the user is a number
print(f"You are {str(age)} years old. Next year you will be {str(age+1)}.")
