# print("Welcome to the fictional character guessing game.\n")
# print("I'm thinking of a female character from a children's story, have a guess who I am thinking of.")

# guessed = False;
# hint_counter = 0;
# while not guessed:
#     name_guessed = input("Enter your guess or hint if you need some help: ")
#     if (name_guessed.lower().strip() == 'hint'):
#         hint_counter +=1
#         if hint_counter == 1:
#             print("apple\n")
#         elif hint_counter==2:
#             print("seven\n")
#         elif hint_counter==3:   
#             print("dwarf\n")
#         elif hint_counter ==4:
#             print("stepmother\n")
#         else:
#             print("Sorry that is all my hints!")
#     else:
#         if len(name_guessed) < 9:
#             print("I'm thinking of a longer name\n")
#         elif len(name_guessed)> 9:
#             print("That name is too long\n")
#         else:
#             if name_guessed.lower().strip()=='whitesnow':
#                 guessed = True
#                 print("Well Done, you guessed what I was thinking of, just right!")
#             else:
#                 print("That name is the right length, but isn't the one I'm thinking of")

##################################  DEMO CODE  ###################################

import datetime



colTeams = {'TeamID':int,'TeamName':str,'TeamEvent':int}
dbTeams= [(101,"Snowboard",1),
(103,"Freestyle Skiing",3),
(123,"Biathlon",5),
(102,"Alpine Skiing",6),
(125,"Speed Skating",3)]

colEvents = {'EventID':int,'EventName':str,'Sport':str,'NZTeam':int}
dbEvents = [(1,"Slopestyle","Snowboarding",101),
(3,"Big Air","Snowboarding",101),
(5,"Men's Halfpipe","Freestyle Skiing",103),
(6,"Men's 20 km individual biathlon","Biathlon",123)]

colMembers = {'MemberID':int,'TeamID':int,'MemberFirstName':str,'MemberLastName':str,'City':str,'Birthdate':datetime.date}
dbMembers=[(5629,103,"Ben","Barclay","Auckland","2002-02-04"),
(5630,103,"Anja","Barugh","Morrinsville","1999-05-21"),
(5631,103,"Finn","Bilous","Wanaka","1999-09-22"),
(5632,103,"Margaux","Hackett","Wanaka","1999-06-02"),
(5633,103,"Nico","Porteous","Hamilton","2001-11-23"),
(5634,101,"Zoi","Sadowski-Synnott","Wanaka","2001-03-06"),
(5635,101,"Tiarn","Collins","Queenstown","1999-11-09"),
(5636,125,"Peter","Michael","Wellington","1989-05-09"),
(5637,123,"Campbell","Wright","Rotorua","2002-05-25")]

def columnOutput(dbData,cols,formatStr):
# dbData is a list of tuples
# cols is a dictionary with column name as the key and data type as the item
# formatStr uses the following format, with one set of curly braces {} for each column.
# For each column "{: <10}" determines the width of the column, padded with spaces (10 spaces in this example)
#   <, ^ and > determine the alignment of the text: < (left aligned), ^ (centre aligned), > (right aligned)
#   The following example is for 3 columns of output: left-aligned, 5 characters wide; centred, 10 characters; right-aligned 15 characters:
#       formatStr = "{: <5}  {: ^10}  {: >15}"
# Make sure the column is wider than the heading text and the widest entry in that column, otherwise the columns won't align correctly.
# You can also pad with something other than a space and put characters between the columns, 
# e.g. this pads with full stops '.' and separates the columns with the pipe character | :
#       formatStr = "{:.<5} | {:.^10} | {:.>15}"
    print(formatStr.format(*cols))
    for row in dbData:
    
        print(formatStr.format(*row))   

def listEvents():
    print()
    columnOutput(dbEvents,colEvents,"{: >17} | {: <32} | {: ^16}") #example of how to call columnOutput function



    input("\nPress Enter to continue.")     # End function with this line

def listTeams():
    print()
    columnOutput(dbTeams,colTeams,"{: <7}  {: <12}  {: <8}") #example of how to call columnOutput function
    input("\nPress Enter to continue.")     # End function with this line


#function to display the menu
def dispMenu():
    print("==== WELCOME TO NZ WINTER OLYMPICS ===")
    print("1 - List Events")
    print("2 - List Teams")
    print("Q - Quit")

#This is the main program

# Repeat this until user enters a "Q"
dispMenu()
response = input("Please select menu choice: ")


while response != "Q":
    if response == "1":
        listEvents()
    if response == "2":
        listTeams()
    else:
        print("invalid response, please re-enter")

    print("")
    dispMenu()
    response = input("Please select menu choice: ")

print("=== Thank you for using NZ WINTER OLYMPICS ===")

