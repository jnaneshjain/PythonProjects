# Python code to illustrate cube of a number
# showing difference between def() and lambda().
def cube(y):
    return y * y * y;


g = lambda x: x * x * x
print(g(7))

print(cube(5))

print()
print("filter")
# Python code to illustrate
# filter() with lambda()
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]

new_list = list(filter(lambda x: (x%2 !=0),li))
print(new_list)


print()
print("map")
# Python code to illustrate
# map() with lambda()
# to get double of a list.
li = [5, 7, 22, 97, 54, 62, 77, 23, 73, 61]
final_list = list(map(lambda x: x*2 , li))
print(final_list)

print()
print("reduce")
# Python code to illustrate
# reduce() with lambda()
# to get sum of a list
from functools import reduce
li = [5, 8, 10, 20, 50, 100]
sum = reduce((lambda x, y: x + y), li)
print (sum)