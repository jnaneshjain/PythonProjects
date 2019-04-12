

def outer(message):
    # enclosing function
    def inner():
        # nested function
        print(message)
    return inner

closure = outer("Hello world!")
print(closure)
closure()
