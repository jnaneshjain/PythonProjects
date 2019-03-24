print("Only Global")
a = 5 #Global variable

def function():
    print(a)

function()
print(a)

print()
print("Global and Local")
b = 3

def function():
    b = 5
    print(f'B from local {b}') # it consider b as separe local variable inside the method


function()
print(b)

print()
print("Use case of Global")

name = 'Théo'

def change_name(new_name):
    name = new_name

print(name)

change_name('Karlijn')

print(name)

print()
print("To tell method to take Global variable")

name = 'JJ'

def change_name(new_name):
    global name
    name = new_name

print(name)
change_name('Jain')
print(name)


