class Dog:
    legs = 4
    def __init__(self, thename, thecolor):
        self.name = thename
        self.color = thecolor


rafi = Dog("rafik", "brown")
rafi.age=12


print(rafi.legs)
print(rafi.age)