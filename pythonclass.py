class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def move(self):
        print("move")

    def draw(self):
        print("draw")

# point1 = Point()
# point1.x = 10 #we can assign a attribute with value for python class
# print(point1.x)
# point1.draw()

point2 = Point(30,40)
print(point2.x)



