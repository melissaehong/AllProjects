class Animal(object):
    def __init__(self, name):
        self.name = name
        self.health = 100

    def walk(self):
        self.health -= 1
        return self

    def run(self):
        self.health -=5
        return self

    def displayHealth(self):
        print "Name: " + self.name
        print "Health: " + str (self.health) + " health"

def cat():
    animal = Animal('Cat')
    animal.walk().walk().walk().run().run().displayHealth()
