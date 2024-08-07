# List of employees: (Name, salary, sales)
payroll_details = [
    ("John", 55000,85000),
    ("Wei",123000,49000),
    ("Rima",75000,222000),
    ("Linda",33000,50000)
]

def total_pay_fn(salary,sales):
    if sales >= 100000:
        bonus = 3000
    elif sales >= 50000:
        bonus = 1500
    else:
        bonus = 0
    total_pay = salary + bonus
    return total_pay


# Calculate total pay for each employee
for employee in payroll_details:
    total_pay = total_pay_fn(employee[1],employee[2])
    print("The total pay is: " + str(total_pay))

# Now calculate total pay for values that are typed in
input_salary = input("What is the salary? ")
input_sales = input("What is the sales figure? ")

total_pay = total_pay_fn(int(input_salary),int(input_sales))

print("The total pay is: " + str(total_pay))
