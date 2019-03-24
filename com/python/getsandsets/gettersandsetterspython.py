
#Java style
class Test:
    ## setter method to change the value 'a' using an object
    def set_a(self, a):
        self._a = a

    def get_a(self):
        return self._a


test = Test()
test.set_a(10)
print(test.get_a())


