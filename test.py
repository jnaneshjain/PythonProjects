#This is class
class A:
    def __init__(self,n = 'jnanesh'):
        self.name = n
    def hi(self,message = 'hi'):
        return message




class B(A):
    def __init__(self, roll):
        A.__init__(self)
        self.roll = roll
    def hi(self,message = 'hi'):
        return "from child"


object = B(23)
print(object.name)
print(object.hi('Hello'))
