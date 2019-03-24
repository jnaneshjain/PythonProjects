class Property:

    def __init__(self, var):
        ## initializing the attribute
        self._a = var

    @property
    def a(self):
        print("Printing inside getter method")
        return self._a

    ## the attribute name and the method name must be same which is used to set the value for the attribute
    @a.setter
    def a(self, var):
        if var > 0 and var % 2 == 0:
            self._a = var
        else:
            self._a = 2
prop = Property(10)
print(prop.a)