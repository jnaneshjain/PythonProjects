'''
LEGB stands for: Local , Enclosed, Global, Built-in

Let's say you're calling print(x) within inner(), which is a function nested in outer().
Then Python will first look if x was defined locally in that inner(). If not, the variable defined in outer() will be used.
This is the enclosing function. If it also wasn't defined there, the Python interpreter will go up another level,
to the global scope. Above that you will only find the built-in scope,
which contains special variables reserverd for Python itself.

'''


# Global scope

x = 0

def outer():
    # Enclosed scope
    x = 1
    def inner():
        # Local scope
        print(x)



