my_dictionary = {"John":123,"Mike":456,"Lee":789}

my_dictionary.pop("John")
my_dictionary["Mika"] = 125

print(my_dictionary.keys())
print(my_dictionary.values())
print(my_dictionary.items())

for key in my_dictionary:
    print(key, my_dictionary[key])

