print("hi")

employee = "Johnny"
salary = 50000
sales = int(input("What sales were achieved"))
bonus = 0

if sales >= 100000:
# if sales >= 100000:
    bonus = 2000
    print("congratulations")
elif sales >= 50000:
    bonus = 1000
else:
    bonus = 0

print(employee)
print(salary)
print(bonus)

total_paid = salary + int(bonus)

      print("Total = " + str(total_paid))