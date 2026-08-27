def make_accumulator():
    total = 0

    def add_x(x):
        nonlocal total
        total += x
        return total
    return add_x

acc = make_accumulator()
print(acc(10))  # 10
print(acc(5))   # 15
print(acc(3))   # 18
