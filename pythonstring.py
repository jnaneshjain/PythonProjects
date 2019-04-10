#This file demonstrates some of the string methods in python
course = 'Python for Beginners'
print(course[0:3])
print(course[0])
print(course[0:])
print(course[:5])
print(course[:])
print(course[0:-1])

first = 'John'
last = 'Smith'

msg = f'{first} [{last}] is a coder'
print(msg) 

print(len(course))
print(course.upper())
print(course.find('P'))
print(course.replace('P','J'))
print('Python' in course)
