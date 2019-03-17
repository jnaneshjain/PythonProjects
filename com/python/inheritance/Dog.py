class Mammal:
    def walk(self):
        print("walk")


class Dog(Mammal):
    pass #Python hates empty class

class Cat(Mammal):
    def walk(self):
        print("cat walks")
    def meow(self):
        print("cat sounds")


dog1 = Dog()
dog1.walk()

cat1= Cat()
cat1.walk()
cat1.meow()