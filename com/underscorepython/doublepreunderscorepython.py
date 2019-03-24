class Sample():

    def __init__(self):
        self.a = 1
        self._b = 2
        self.__c = 3
obj1 = Sample()
print(dir(obj1))

'''
If you carefully look at the attributes list, you will find an attribute called _Sample__c. 
This is the name mangling. It is to avoid the overriding of the variable in subclasses.
'''

class SampleTst(Sample):
    def __init__(self):
        super().__init__()
        self.a = "overridden"
        self._b = "overridden"
        self.__c = "overridden"


obj2 = SampleTst()
print(obj2.a)
print(obj2._b)
# print(obj2.__c) #It throws error,Here, the name mangling works again. It changes the obj2.__c to _SecondClass__c. Now, print that element using modified Attribute.
print(obj2._SampleTst__c) # To fix above error