# Tuple unpacking allows multiple variables to be assigned in one line

# (tuples don't always have to have brackets, unless it's ambiguous what it is)

first, middle, last = "John", "Horatio", "Smith"

print(first)
print(middle)
print(last)

# This applies in FOR loops too:

my_list1 = [
    ('row 1',10,'abc',42.45),
    ('row 2',20,'def',19.15),
    ('row 3',30,'ghi',56.22)
]

for row in my_list1:
    print(row[0],row[1],row[2],row[3])

for a,b,c,d in my_list1:
    print(a,b,c,d)

# There are two common cases where each loop can have two variables:

# 1. Looping through a dictionary

my_dict = {'key1':'value1','key2':'value2','key3':'value3','key4':'value4'}

# One option:
for key in my_dict:
    print(f"{key}:{my_dict[key]}")

# Alternative:
print(my_dict.items())      # A list of tuples

for key,value in my_dict.items():
    print(f"{key}:{value}")


# 2. enumerate() function

my_list2 = ['a','b','c','d']

# enumerate adds a counter for index position in the list
print(list(enumerate(['a','b','c','d'])))

for index,item in enumerate(my_list2):
    print(index, item, my_list2[index])
