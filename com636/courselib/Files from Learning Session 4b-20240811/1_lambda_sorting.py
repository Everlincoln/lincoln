my_list = [
    ('cat',2,'rabbit',600),
    ('cat',1,'zebra',300),
    ('mouse',1,'horse',400),
    ('aardvark',1,'cow',10)
]

for row in my_list:
    print(row)

print()

for row in sorted(my_list):
    print(row)

print()

for row in sorted(my_list,key = lambda x:x[2]):
    print(row)
# x[1] is the second element in the tuple. x[3] is the fourth element in the tuple
# The - in front of x[3] is to sort in descending order
for row in sorted(my_list,key= lambda x:(x[1],-x[3])):
    print(row)

for row in sorted(my_list,reverse=True):
    print(row)

