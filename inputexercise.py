#This file demonstrates how to take input from the users
weight = int(input('Weight :'))
unit = input('(L)bs or (K)g: ')
if unit.upper() == 'L':
    converted = weight * 00.45
    print(f"Your are {converted} kilos")
else:
    converted = weight /0.45
    print(f"You are {converted} pounds")
