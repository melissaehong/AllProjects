class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.tax = .15
        else:
            self.tax = .12
        self.displayAll()
    def displayAll(self):
        print 'Price: $' + str(self.price)
        print 'Speed: ' + str(self.speed) + ' mph'
        print 'Fuel: ' + str(self.fuel)
        print 'Mileage: ' + str(self.mileage) + ' miles'
        print 'Tax: ' + str(self.tax)
        return self

melissa = Car(2000, 200, 'Full', 0)

jeremy = Car(200000, 100, 'Kind of Full', 10)
