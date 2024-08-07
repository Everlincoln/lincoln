# Function from: https://www.geeksforgeeks.org/introduction-to-levenshtein-distance/

def levenshteinRecursive(str1, str2, m, n):
    #print(m,n)
    # str1 is empty
    if m == 0:
        return n
    # str2 is empty
    if n == 0:
        return m
    if str1[m - 1] == str2[n - 1]:
        return levenshteinRecursive(str1, str2, m - 1, n - 1)
    return 1 + min(
          # Insert     
        levenshteinRecursive(str1, str2, m, n - 1),
        min(
              # Remove
            levenshteinRecursive(str1, str2, m - 1, n),
          # Replace
            levenshteinRecursive(str1, str2, m - 1, n - 1))
    )
 
# Drivers code
str1 = "bad"
str2 = "bid"
distance = levenshteinRecursive(str1, str2, len(str1), len(str2))
print("Levenshtein Distance:", distance)

my_string = "The quick brown fox jumps over the lazy dog."
split_string = my_string.split()
for ctr in range(1,len(split_string)):
    str1 = split_string[ctr - 1]
    str2 = split_string[ctr + 0]
    distance = levenshteinRecursive(str1, str2, len(str1), len(str2))
    print(str1 + ' vs ' + str2,'=', distance)

