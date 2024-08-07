
payroll_details = [
    ("John", 55000,85000),
    ("Wei",123000,49000),
    ("Rima",75000,222000),
    ("Linda",33000,50000)
]

def total_pay():
    global bonus
    if sales >= 100000:
        bonus = 2000
    elif sales >= 50000:
        bonus = 1000
    else:
        bonus = 0

for employee in payroll_details:
    bonus = 0
    salary = employee[1]
    sales = employee[2]
    total_pay()
    print(bonus)
    