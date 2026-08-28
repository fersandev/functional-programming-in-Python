def flatten(nested_list):
    result = []

    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten(element))
        else:
            result.append(element)

    return result

resultado = flatten([1, [2, [3, 4], 5], [6]])
print(resultado)  # [1, 2, 3, 4, 5, 6]
