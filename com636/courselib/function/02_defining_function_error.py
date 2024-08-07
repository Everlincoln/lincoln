# This code will fail because the function hasn't been defined before it is called.
# (In some languages this is OK, but Python compiles the code sequentially.)

my_function()       # Python does not know what 'my_function()' is

def my_function():    # defined too late - after the call
    print("This won't be called.")
