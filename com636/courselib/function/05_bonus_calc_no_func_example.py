# List of employees: (Name, salary, sales)
payroll_details = [
    ("John", 55000,85000),
    ("Wei",123000,49000),
    ("Rima",75000,222000),
    ("Linda",33000,50000)
]
# Calculate total pay for each employee
for employee in payroll_details:
    salary = employee[1]
    sales = employee[2]
    if sales >= 100000:
        bonus = 3000
    elif sales >= 50000:
        bonus = 1500
    else:
        bonus = 0
    total_pay = salary + bonus
    
    print("The total pay is: " + str(total_pay))

# Now calculate total pay for values that are typed in
input_salary = input("What is the salary? ")
input_sales = input("What is the sales figure? ")

salary = int(input_salary)
sales = int(input_sales)

if sales >= 100000:
    bonus = 3000
elif sales >= 50000:
    bonus = 1500
else:
    bonus = 0
total_pay = salary + bonus

print("The total pay is: " + str(total_pay))
