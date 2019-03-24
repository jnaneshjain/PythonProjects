numbers = [1,2,3,4,5,6]
numbers.append(20) # append to the last
print(f'before deleting{numbers}')
del numbers[6]
print(f'aftr deleting{numbers}')
numbers.insert(2,34) #insert into the specified index
numbers.remove(34)
numbers.pop() #removes last element
print(numbers.index(5))
print(5 in numbers)
print(f'count{numbers.count(5)}')
numbers.sort()
numbers.reverse()
numbers2 = numbers.copy()
print(numbers2)
print(numbers)
numbers.clear()
print(numbers)
print(len(numbers))