# creat a simple function 
def mnil( list ): #a normal function definition
    max = list[ 0 ] #create a new variable called max
    for a in list:   #create a new variable called a
        if a > max:
            max = a
    return max
print(mnil([1.2, 2.1, -8.0, 3.3]))
print(mnil(["test", "hello", "no"]))
print(mnil([-1, -2, -8, 0]))
print(mnil([1, 2, -8, 0]))

# creat a simple function 
def number(list):
    total = 0
    for a in list:
        total += a
    return total
    
# creat a simple function
def add_number (list):
        total = a
        for a in list:
            total 
        return total

# creat a simple function
def max_and_min_number_in_list( list ) : #a normal function definition
    max = list[ 0 ] #create a new variable called max
    min = list[ 0 ]
    for a in list:  #for loop to iterate through the list
        if a > max:
            max = a
        if a < min:
            min = a
    return max, min
print(max_and_min_number_in_list([1,2,3,4,5]))
print(max_and_min_number_in_list([-1,-4,-5,-7]))


# Create a function; average_list(list), that takes a list as an input, and finds the average value, returning it as a float
def average_list (list):
    average = sum(list)/ len(list)
    return round (average, 3)
print(float(average_list([1,2,3,4,5,6,7,10.2])))
print(float(average_list([-3,-2,-1,0])))
    

def triangle_stars(n):
     # for loop to iterate through the range of 1 to n+1 and this is the outer loop
    for i in range(1,n+1):
        # for loop to iterate through the range of i and this is the inner loop which is controoling the number of stars
        for j in range(1,i+1): 
            print ("* ", end="") #note the use of the end function, which replaces the default /n with "". 
        print(i)

    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print("* ", end="")
        print(i)

triangle_stars(5)


def  triangle_stars(n): 
    for i in range(1,n+1): # note the use of the range function, to generate a list equal to [1,2,....,n,n+1]
        for j in range(1,i+1):
            print ("* ", end="") #note the use of the end function, which replaces the default /n with "". 
        print(i)
    for i in range(n-1,0,-1):
        for j in range(1,i+1):
            print ("*", end="") #note the use of the end function, which replaces the default /n with "". 
        print(i)
            

# While Looping in Python
i = 1          #Creates a variable
print("Starting the loop now!")                 #a debugging print statement                 
while i < 6:   #continues executing for as long as i is less than six
    print(i)       #prints out the value of i in the current loop
    i += 1         #adds one to the variable i
    if i == 4:     #if i is four
        continue         #continue causes the loop to stop executing, and restart (ie go back to the top)
    if i == 3:           #if the value of I is three
        print("i equals three")       #print
    print("I finished a loop!")       #notice the indentation - this is no longer within the if statement.
else:                                    #this else statement occurs when the loop condition is no longer true
    print("i is now larger than five")

print ("The loop successfully finished")         #a debugging print statement


# Try to answer the following questions about this loop - if you're struggling, then just try running it (it will tell you the answers!)
i = 0
print(i)
while i <= 10:
    if i == 1:
        print(str(i)+"st loop")
    if i == 2:
        print(str(i)+"nd loop")
    if i == 3:
        print(str(i)+"rd loop")
    if i > 3:
        print(str(i)+"th loop")
    if i == 5:
        break
    i+= 1
print(i)


# requirements
# Wrap the entire loop within a function foo_looper(n) which takes any integer input
# allow the loop to start from n
# allow the loop to run from n to 10
# when i equals 9 print "second to last loop" after printing "9th loop"

def foo_looper(n):
    i = n
    while i <= 10:
        if i == 1:
            print(str(i)+"st loop")
        if i == 2:
            print(str(i)+"nd loop")
        if i == 3:
            print(str(i)+"rd loop")
        if i > 3:
            print(str(i)+"th loop")
        if i ==9:
            print("second to last loop")
        i+= 1



# Create a function loop_printer(n) that takes any positive integer input n and prints the numbers from n to 1, each on their own line.
def loop_printer(n):
    i = n
    while i > 0:
        print(i)
        i -= 1

  
# create a while loop within a function foo_bounded_while(start,end) that takes two integer inputs, and squares start, until it is larger than the end number, printing the value at the start of each loop, and also the final(larger than end) value
# first method
def squareFunction(n):
    return n*n

def foo_bounded_while(start,end):
    result = start
    while result <= end:
        print(result)
        result = squareFunction(result)   
    print(result)

foo_bounded_while(2,256)

# second method
def foo_bounded_while(start,end):
    result = start
    while result <= end:
        print(result)
        result = result * result
    print(result)
    
foo_bounded_while(2,256)


# Write a function compare(a,b), that takes two integer variables, and returns the larger of the two values, or returns "these values are equal" if they are equal.
def compare(a,b):
        if a>b:
            return a
        if b>a:
            return b
        if a==b:
            return "these values are equal"
print(compare (1,1))


# Write a function bool_test that takes any data type as an input, and returns false if it is empty or 0, and true if not.
def bool_test(value):
    if not value:
        return False
    else:
        return True
    

# you can use the builtin type(variable) function in python to check what datatype a variable is. Using this builtin function, write a  function type_check that returns the string 
# "this variable type is: data_type" where data_type is Integer, String, Float, or List, as appropriate
def type_check(value):
    if type(value)==str:
        return "this variable type is: String"
    elif type(value)==int:
        return "this variable type is: Integer"
    elif type (value)==float:    
        return "this variable type is: Float"
    elif type(value)==list:
        return "this variable type is: List"


# A function in python is a named block of code that executes when "called". In python the syntax for creating a function is simple:
def function_name(variable_input):
    #This is my first function!

    print("I am running my function!")

    variable_output = variable_input + " Werld!"

    return(variable_output)


printing_var = function_name("Hello")
print(printing_var)


# create a simple function named double_input(input), which takes any input variable and returns that variable, times 2 
# first method
def double_input(input):
    return input*2
print(double_input("Hello")) 

# second method
def double(variable):
    return variable*2

def double_input(input):
    result=input
    result=double(input)
    return result
    print(double_input("Hello")) 


# Write a python function, multiple_input(var1,var2), that accepts an integer as the first variable, and a list as the second variable, and first prints the list, and then returns value at position var1 from list var2.
def multiple_input(var1,var2):
    print(var2)
    return(var2[var1])

print(multiple_input(0,[1,2,3,4]))