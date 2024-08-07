data = ["banana","apple","tomato","cherry"]     # sorting only works if all items are the same type

print("data",data)

data_pointer = data
print("data_pointer",data_pointer)

data_copy = data.copy()

data[0] = "New value"

print("data",data)
print("data_pointer",data_pointer)
print("data_copy",data_copy)

