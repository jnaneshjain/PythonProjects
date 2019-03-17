#By default python returns None from the function

def greet_user(first_name,last_name = 'None'):
    print(f'Hi  {first_name} {last_name}')
    print("Welcome aboard")


print("Start")
greet_user('John','Smith')
greet_user(last_name='John',first_name='Smith') #keyword arguement
greet_user('Jj')
print("End")

def square(number):
    return  number * number

print(square(2))

