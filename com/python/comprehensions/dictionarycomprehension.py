# Python Code to Demonstrate Dictionary comprehensions

# Lists to represent keys and values
keys = ['a', 'b', 'c', 'd', 'e']
values = [1, 2, 3, 4, 5]

# But this line shows dict compreHension here
myDict = {k: v for (k, v) in zip(keys, values)}

# We can use below method too
# myDict = dict(zip(keys, values))

print(myDict)
