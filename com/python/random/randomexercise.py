import random

class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first,second #if we do not put braces python treat it as tuple

dice = Dice()
print(dice.roll())
