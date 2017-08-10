class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *num1):
        for num in num1:
            if isinstance(num, list or tuple):
                for item in num:
                    self.result += item
            else:
                self.result += num
        return self
    def subtract(self, *num1):
        for num in num1:
            if isinstance(num, list or tuple):
                for item in num:
                    self.result -= item
            else:
                self.result -= num
        return self

md = MathDojo()

print md.add(2).add(2, 5).subtract(3, 2).result
print MathDojo().add([1],3,4).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract(2, [2,3], [1.1, 2.3]).result
