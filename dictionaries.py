#Dictionaries are key value pair,keys should be unique,we can modify dictionries
#None is objec in pyhton, that represents absence of the value

customer = {
    "name" : "John Smith",
    "age" : 30,
    "is_verfied" : True
}
print(customer["name"])
#print(customer["birthdate"]) #throws exception since this key is not present
print(customer.get("birthdate"))
print(customer.get("birthdate","Jun 25 1994"))