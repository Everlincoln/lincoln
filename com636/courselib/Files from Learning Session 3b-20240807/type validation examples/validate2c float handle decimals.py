#AREA OF A ROOM
# Use function to remove any leading negative sign '-' and the first decimal point '.'
# Then use isdigit() to check if what is left is a non-negative whole number

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
        if length > 0 and width > 0:    #Need to check that both are numbers before checking these conditions
            #The flag is set to true if the both entries are numbers and greater than zero
            validEntry = True
    #Display an error message if validEntry is still false. (IF statements could be used to provide more specific error messages.)
    if not validEntry:
        print("Invalid number entered. Both height and width must be numbers greater than zero.")

#Calculate the area of the room - will only exit while loop once both numbers are numeric
area=length*width

#This statement is printed if the input entered by the user is a number
print(f"The room is {str(length)} m long x {str(width)} m wide.\nThe area of the room is {str(area)} sq. m.")