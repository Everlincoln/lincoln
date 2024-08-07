

data = ["apple","pear","persimmon","carrot"]

#print(data)

for item in data:            # 'item' gets the value of each item in data, one at a time for each loop
    if(item[0] == 'p'):      # only print the items in data that start with 'p'
        print(item)


nested = [
    ("Adam","Chen",1234567),
    ("Johnny","Smith",1234568),
    ("Mike","Li",1234569)
]
#row = nested[0]

for row in nested:          # each 'row' is one of the tuples in nested
    print(row)
    for item in row:        # each 'item' is one of the items in the current tuple 
        print(item)
