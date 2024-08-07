
print("\n------- Usual (and safest) way to use a function: pass value & return value -------")

def x_pass_value(a):
    a = 333         # a only exists inside this function
    return a

x = 10
y = x_pass_value(x)
print("Value passed:",x)
print("Value returned:",y)

print("\n------- Refer to global variable in function -------")

def x_global():
    print("In x_global():",x)       # prints the global x variable
    return x                        # also returns the value of x

x = 10
print("Main, before function:",x)
y = x_global()                  # y gets the value returned from the function
print("Main, after function:", y)

print("\n-------- Create new version of x in function ----------------------------")

def x_local():
    # print("Global x in function:",x)      # Causes an error because x is defined locally below
    x = 400                     # assigning a value locally creates a new x available only inside the function
    print("In x_local:",x)

x = 10
print("Main, before function:",x)
x_local()
print("Main, after function:",x)           # the global value of x hasn't changed (= 10)

print("\n--------- Change global x in function---------------------------")

def x_change_global():
    global x                    # same as above, but this time we say we are using the global x
    x = 400                     # this changes the global x
    print("In x_change_global:",x)

x = 10
print("Main, before function:",x)
x_change_global()
print("Main, after function:",x)    # now x = 400 from change to global variable in the function

print("")
