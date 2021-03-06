"""
****** Indices and Slices ********
"""
some_list = [x for x in range(10)]
print(some_list)

print("The first index value")
print(some_list[1])

print("The last index value")
print(some_list[-1])

print("The second to last index value")
print(some_list[-2])

print("The indices 1 to 5(exclusive)")
print(some_list[1:5])

print("The indices less than 5")
print(some_list[:5])


line = "This is some text"
print(line)

print("The value at the 7th index position")
#PROBLEM1.1 Print the value at the 7th index
print(line[7])

print("The characters from indices 4 to 9")
#PROBLEM1.2 Print the characters from indices 4 to 9 characters
print(line[4:10])

print("The last 4 characters")
#PROBLEM1.3 Print the last 4 characters
print(line[-4:])

"""
****** Iterators ********
"""

#PROBLEM2.1 Iterate through TWO ways "some_list" to add the values. Then print the result
 #1. Iterate through the indices (using range)
# print("Using an index to iterate")
# for i in range(0, len(some_list)):
#     print(some_list[i])
 #2. Iterate using the keyword "in"
# print("Using in, iterate through list")
# for x in some_list:
#     print(x)


#Dictionary Examples
dict1 = {"fruit":"apple", "vegetable":"carrot", "meat":"chicken"}
dict2 = {(1,2):"x", (1,3):"y", (4,5):"z"}

#Problem2.2 iterate though dict1, dict2

#Functions and Generators
#PROBLEM3.1 Define a function that will print the list, dict1, and dict2

def print_values(param):
    for key in param:
        print(str(key) + " " + param[key])


#PROBLEM3.2 Define a generator that will print the list, dict1, and dict2
def gen_print_values(param):
    for key in param:
        yield str(key) + " " + param[key]
        
generator = gen_print_values(dict2)

print(next(generator))
print("break")
for value in generator:
    print(value)




