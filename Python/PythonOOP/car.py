'''Create a class called  Car. In the__init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

Create six different instances of the class Car. In the class have a method called display_all() that returns all the information about the car as a string. In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.'''

class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.display_all()

    def display_all(self):
        print "Price: " + str(self.price)
        print "Speed: " + str(self.speed) + "mph"
        print "Fuel: " + str(self.fuel)
        print "Mileage: " + str(self.mileage) + " miles"
        print "Tax: " + str(self.tax)

car1 = Car(10000, 40, 'Full', 100000)
car2 = Car(10, 10, 'Not Full', 0)
car3 = Car(100000, 30, 'Kind of Full', 45)
car4 = Car(10001, 0, "Meh", 10)
car5 = Car(9999, 11, 'Empty', 100)
car6 = Car(1000000, 1000, 'Full', 1000000)
