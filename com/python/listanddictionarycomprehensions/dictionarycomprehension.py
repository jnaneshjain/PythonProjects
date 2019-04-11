# Python Code to demonstrate dictionary

# Lists to represent keys and values
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# but this line shows dict compreHension here
myDict = {k: v for (k, v) in zip(keys, values)}

# We can use below too
# myDict = dict(zip(keys, values))

print(myDict)
