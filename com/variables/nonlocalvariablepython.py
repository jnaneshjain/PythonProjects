x = 'a'


def outer():
    x = 'b'
    def inner():
        x = 'c'
        print(f'Inner x = {x}')
    inner()
    print(f'Outer x = {x}')

outer()
print(f'Global x = {x}')

print()
print('If we use nonlocal keyword')

x = 'a'


def outer():
    x = 'b'
    def inner():
        nonlocal x
        x = 'c'
        print(f'Inner x = {x}')
    inner()
    print(f'Outer x = {x}')

outer()
print(f'Global x = {x}')

print()
print('If we use global keyword')

x = 'a'


def outer():
    x = 'b'
    def inner():
        global x
        x = 'c'
        print(f'Inner x = {x}')
    inner()
    print(f'Outer x = {x}')

outer()
print(f'Global x = {x}')

