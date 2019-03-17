# tuple is same as list,but we cant modify tuples
numbers = (1,2,3)
print(numbers[0])
#numbers[0] = 10 #throws exception since we cant modify tuples

cordinates = (1,2,3)
x,y,z = cordinates #Unpacking feature applies to list also
print(x)