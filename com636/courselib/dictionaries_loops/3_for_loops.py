data = ["apple","pear","persimmon","carrot"]

#print(data)

for item in data:
    if item[0] == "p":            # 'item' gets the value of each item in data, one at a time for each loop
        break
    print(item)
else:
    print("Loop is finished")

# for ctr in range(6):
#     new_num = ctr * 100
#     print(ctr)

