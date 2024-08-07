#AREA OF A ROOM
# No validation - try entering a text value or negative value

#The user is prompted to enter the inputs
length_input = input("Please enter length of the room in metres: ")
width_input = input("Please enter width of the room in metres: ")

#The entry strings are converted to float
length=float(length_input)
width=float(width_input)

#Calculate the area of the room - will only exit while loop once both numbers are numeric
area=length*width

#This statement is printed if the input entered by the user is a number
print(f"The room is {length} m long x {width} m wide.\nThe area of the room is {str(area)} sq. m.")
