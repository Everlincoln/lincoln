# The difference between float and decimal types

# This is optional, for your information.
# Float type can have some rounding issues that can causes at high precision.
# If you work in a field where exact numbers are required (e.g., accounting, fintech, engineering, etc.) 
#    you might want to research this further.

from decimal import Decimal     # import the Decimal module to use the Decimal function below
from datetime import datetime   # this is just used to get the start and end time of the code

# Float does not give exact decimal values, so small errors creep in
x = 1.1
y = 2.2
z = 3.3
# This should = 1.1...
print("Float:  1.1 + 2.2 + 3.3 - 3.3 - 2.2 =", x + y + z - z - y)

# Decimal manages the small errors to return exact values
x = Decimal('1.1')
y = Decimal('2.2')
z = Decimal('3.3')
# This does = 1.1:
print("Decimal:  1.1 + 2.2 + 3.3 - 3.3 - 2.2 =", x + y + z - z - y)

# This code keeps a running total of a and b after adding 10**9 (1 billion) times
# You can see how the error compounds at the end
# IT TAKES AROUND 5 MINS TO RUN!

a = 1.111111111
b = Decimal('1.111111111')

a_running_total = 0
b_running_total = 0

print("Started at: " + str(datetime.now()))

for i in range(10**9):
    a_running_total += a        #this is the same as:  a_running_total = a_running_total + a
    b_running_total += b

print(10**9*a)
print()
print("Float running total:",a_running_total)
print("Decimal running total:",b_running_total)

print("Ended at: " + str(datetime.now()))
