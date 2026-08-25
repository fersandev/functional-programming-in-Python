from itertools import islice

def fibonacci():
    a = 0
    b = 1

    while True:
        yield a
        a, b = b, a + b

first_eight = list(islice(fibonacci(), 8))
print(first_eight) # [0, 1, 1, 2, 3, 5, 8, 13]