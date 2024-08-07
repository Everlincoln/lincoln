data = ["banana","apple","tomato","cherry"]     # sorting only works if all items are the same type

print(data)
print(data[0])      # First item in list

print(sorted(data))     # sorted() only sorts the output, but the list doesn't change
data.sort(reverse=True) # .sort() changes the list so it is stored in sorted order
print(data)