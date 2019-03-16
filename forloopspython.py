for item in 'Python':
    print(item)

for item in range(10):
    print(item)

for item in range(5,10):
    print(item)

for item in range(5,10,2):
    print(item)

for x in range(4):
    for y in range(3):
        print(f'({x},{y})')

numbers = [5,2,5,2,2]
print(numbers[1:])

for x in numbers:
        print('*' * x)

for x in numbers:
    output = ''
    for count in range(x):
        output += 'x'
    print(output)