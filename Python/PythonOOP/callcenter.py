class Call(object):
    def __init__(self, id, name, phoneNum, time, reason):
        self.id = id
        self.name = name
        self.phoneNum = phoneNum
        self.time = time
        self.reason = reason
    def display(self):
        print self.id
        print self.name
        print self.phoneNum
        print self.time
        print self.reason

newCall = Call(1,"Melissa", "999-9999", "12:50pm", "Information").display()

class CallCenter(object):
    def __init__(self, calls):
        self.calls = calls
        self.call_count = len(calls)
    def add(self, id, name, phoneNum, time, reason):
        self.calls.append(Call(id, name, phoneNum, time, reason))
        self.call_count += 1
        return self
    def remove(self, phoneNum):
        for i in range(0, len(self.calls)-1):
            if phoneNum == self.calls[i].phoneNum:
                print "Removed phone number " + str(self.calls[i].phoneNum)
                self.calls.pop(i)
        self.call_count -= 1
        return self
    def info(self):
        for i in range(0, len(self.calls)):
            print "Id: " + str(self.calls[i].id)
            print "Name: " + str(self.calls[i].name)
            print "Phone Number: " + str(self.calls[i].phoneNum)
        print self.call_count
        return self
## come back after algorithms!!!
    def order(self):
        for i in range(0, len(self.calls)):
            if self.calls[i].time < self.calls[i-1].time:
                self.calls.sort(reverse=True)
        return self

call1 = Call(1,"Melissa", "999-9999", "1200", "Information")
call2 = Call(2, "Salvador", "555-5555", "200", "Random")
call3 = Call(3, "Freud", "571-2798", "1350", "wants tuna")
call4 = Call(4, "Mom", "123-4567", "300", "hi")

call_list = [call1, call2, call3, call4]

center = CallCenter(call_list)

center.info()
center.remove('555-5555')
center.info()
center.order()
center.info()
