x = [1,2,3,4,3,2,1]

def stars(num_list):
    for num in num_list:
        output = ''
        for i in range (num):
            output += '*'
        print output

stars(x)

y = [4, "Tom", 1, "Michael", 5, 6, "Jimmy Smith"]

def stars2(list1):
    for obj in list1:
        output = ''
        if type(obj) is str:
            first_letter = obj[0].lower()
            for i in range (len(obj)):
                output += first_letter
        elif type(obj) is int:
            for i in range (obj):
                output += '*'
        print output

stars2(y)
