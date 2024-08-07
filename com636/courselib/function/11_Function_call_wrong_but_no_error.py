# Function calls without brackets just return the name of the function and its location in memory.
# This doesn't raise an error, but it probably isn't what you're after

def my_function():      # a simple function that returns the value 1234
    x = 1234
    return x

# Correct call of my_function() - with brackets
print("Correct function call (with brackets):",my_function())
# Incorrect call of my_function - without brackets. This returns name and location of function, but no error
print("Incorrect function call (without brackets):",my_function) 

# If we try to add something to the function output, this works
print("Adding (with brackets):",my_function() + 1) 
# But this lines gives the error:  "TypeError: unsupported operand type(s) for +: 'function' and 'int' "
# because we are trying to add 1 to '<function my_function at 0x000002052F7FA340>', which isn't a number  
print("Adding (without brackets):",my_function + 1)
