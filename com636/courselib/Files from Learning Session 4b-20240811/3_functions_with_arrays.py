# functions can accept arrays (list, tuples, dictionaries, sets) as arguments
# they can also return arrays

# Simple demonstration function to extract only the integers from a list
def remove_non_int(input_list):
    int_list = []
    for item in input_list:
        if type(item) == int:
            int_list.append(item)
    list_len = len(int_list)
    return (int_list, list_len)


int_only = remove_non_int([1, 2, 2.3, 'hello', 3, [1,2], 4, 'abc', 5])

print(int_only)
print(int_only[0])
print(f"Length: {int_only[1]}")
