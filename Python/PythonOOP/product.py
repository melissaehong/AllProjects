class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price = price
        self.name = name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = 'for sale'

    def sell(self):
        self.status = 'sold'
        return self

    def addTax(self, decimal):
        self.price += self.price*decimal
        return self

    def Return(self, reason):
        self.reason = reason
        if self.reason == 'defective':
            self.status = 'defective'
            self.price = 0
        if self.reason == 'box':
            self.status = 'for sale'
        if self.reason == 'opened':
            self.status = 'used'
            self.price = self.price*.2
        return self

    def displayInfo(self):
        print "Price: " + str(self.price)
        print "Name: " + str(self.name)
        print "Weight: " + str(self.weight) + ' lbs'
        print "Brand: " + str(self.brand)
        print "Cost: " + str(self.cost)
        print "Status: " + str(self.status)

melissa = Product(2000, 'Melissa', 20, 'Hong', 300)
melissa.sell().displayInfo()
melissa.addTax(.10).displayInfo()
melissa.Return('box').displayInfo()
melissa.Return('opened').displayInfo()
