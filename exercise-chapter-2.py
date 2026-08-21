def apply_operations(value, operations):
    # The copy method is not needed because integers are immutable.
    value_to_operate = value 
    for operation in operations:
        # Immutability isn't violated because they are integers
        # It would be different if we used lists
        # However, it's still imperative style, later
        # we'll see that it's solved with reduce
        value_to_operate = operation(value_to_operate)
    
    return value_to_operate
    
operations = [lambda x: x + 1, lambda x: x * 2]
value = 3
result = apply_operations(value, operations)
print(result) # 8
