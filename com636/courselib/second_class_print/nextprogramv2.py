print('hi')

employee = 'Johnny'
salary = 50000
sales = int(input("What sales were achieved? "))

if sales >= 100000:
    bonus = 2000
    print("Congratulations")
elif sales >= 50000:
    bonus = 1000
else:
    bonus = 0

print(employee)
print(salary)
print(bonus)

total_paid = salary + bonus

print("Total = " + str(total_paid))

#print(employee + salary)