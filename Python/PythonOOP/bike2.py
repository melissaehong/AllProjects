class Bike(object):
    def __init__(self, price, speed):
        self.price = price;
        self.max_speed = speed;
        self.miles = 0
    def displayInfo(self):
        print self.price
        print self.max_speed
        print self.miles
        return self
    def ride(self):
        print "Riding"
        self.miles += 10
        return self
    def reverse(self):
        print "Reversing"
        self.miles -= 5
        return self

redBike = Bike(200, "25 mph")
redBike.ride().ride().ride().reverse().displayInfo()

blueBike = Bike(130, "15mph")
blueBike.ride().ride().reverse().reverse().displayInfo()

yellowBike = Bike(300, "30 mph")
yellowBike.reverse().reverse().reverse().displayInfo()
