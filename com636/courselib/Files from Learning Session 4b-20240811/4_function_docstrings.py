# functions can accept arrays (list, tuples, dictionaries, sets) as arguments
# they can also return arrays

# 
def remove_non_int(input_list):
    """This is a simple demonstration function to extract only the integers from a list. 
    
    This is also a 'docstring':  a function description in triple quotes, indented, straight after function definition.
    It shows up when you enter or mouse over a function call."""
    int_list = []
    for item in input_list:
        if type(item) == int:
            int_list.append(item)
    list_len = len(int_list)
    return int_list, list_len


int_only = remove_non_int([1, 2, 2.3, 'hello', 3, [1,2], 4, 'abc', 5])

print(int_only)
print(int_only[0])
print(f"Length: {int_only[1]}")
