from functools import reduce

def flatten_max(list_of_lists):
    def keep_max(current_max, number):
        return number if number > current_max else current_max

    def max_all(current_max, sublist):
        return reduce(keep_max, sublist, current_max)

    return reduce(max_all, list_of_lists, float("-inf"))

result = flatten_max([[1, 5], [9, 2], [3]])
print(result)

# sublista [1,5] -> keep_max(-inf,1)=1 -> keep_max(1,5)=5 => acc=5
# sublista [9,2] -> keep_max(5,9)=9 -> keep_max(9,2)=9    => acc=9
# sublista [3]   -> keep_max(9,3)=9                       => acc=9
