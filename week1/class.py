class Animate:
    def __init__(self,age):
        self.age=age

class Mammalia:
    def run(self):
        print('run')
    def suckle(self):
        print('suckle')

class Dog(Animate,Mammalia):
    numberofleg=4
    def __init__(self,age):
        super().__init__(age)
    def getLegNumber():
        return Dog.numberofleg 

print(Dog.getLegNumber()) 

dog=Dog(4)
print(dog)