# The modulo operator % shows the remainder when you divide by a number
#   15 % 5 = 0    (17 / 5 = 3 remainder 0      i.e. 0 means the dividing number fits an exact number of times)
#   17 % 5 = 2    (17 / 5 = 3 remainder 2      i.e. 2 is left over after dividing into 5)
#   22 % 5 = 2    (22 / 5 = 4 remainder 2      i.e. 2 is left over after dividing into 5)

for i in range(21):         # loops 21 times: i has the values from 0 to 20 in each loop
    print(i,"/2 remainder is ", i % 2)   # % is the modulo operator - returns the remainder when dividing by 2