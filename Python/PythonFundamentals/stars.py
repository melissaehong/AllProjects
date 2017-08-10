arr = [3,4,1]

def draw_stars(arr):
    for num in arr:
        print '*' * num

draw_stars(arr)

arr = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars2(arr):
    for x in arr:
        if isinstance(x, int):
            print '*' * x
        if isinstance(x, str):
            length = len(x)
            letter = x[0].lower()
            print length * letter

draw_stars2(arr)
