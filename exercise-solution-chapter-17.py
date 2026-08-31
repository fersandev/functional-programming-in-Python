def pipe(*funcs):
    def piped(x):
        result = x
        for f in funcs:
            result = f(result)
        return result
    return piped

def convert_to_int(strings):
    return [int(s) for s in strings]

def absolute_values(numbers):
    return [abs(n) for n in numbers]

def filter_even(numbers):
    return [n for n in numbers if n % 2 == 0]

def sum_numbers(numbers):
    return sum(numbers)

process_pipe = pipe(
    convert_to_int,
    absolute_values,
    filter_even,
    sum_numbers
)

numbers = ["3", "-1", "7", "-5", "2"]
result = process_pipe(numbers)
print(result) # 2
