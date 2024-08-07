staff_name = "Sir,Mike,Jones"

print(staff_name[3:])

print(len(staff_name))

for letter in staff_name:
    print(letter)

print(staff_name.lower())

if "JON" in staff_name.upper():
    print("Found")

print(staff_name.split(','))

print(staff_name.replace(',',' '))

first_name = "Mike"
family_name = "Jones"
num = 123.45678

print("Dear " + first_name + ' ' + family_name + ',' + str(num))

print(f"Dear {first_name} {family_name}, {num:.3f}")
