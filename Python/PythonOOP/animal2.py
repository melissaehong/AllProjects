class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100
    def walk(self):
        self.health -= 1
        return self
    def run(self):
        self.health-=5
        return self
    def displayHealth(self):
        print "Health: " + str(self.health)
        return self

cat = Animal('Bingomango')

cat.walk().walk().run().run().displayHealth()

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.health = 150
    def pet(self):
        self.health += 5
        return self

dog1 = Dog('Barky')

dog1.displayHealth()
dog1.walk().walk().walk().run().run().pet().displayHealth()

class Dragon(Animal):
    def __init__(self, name):
        super(Dragon, self).__init__(name)
        self.health = 170
    def fly(self):
        self.health += 10
        return self

    def displayHealth(self):
        super(Dragon, self).displayHealth()
        print "I am a Dragon"

fakeDragon = Dragon("Dragon")

fakeDragon.fly()
fakeDragon.displayHealth()
