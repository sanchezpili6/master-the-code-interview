arr1 = ['a', 'b', 'c', 'd', 'x']
arr2 = ['z', 'x', 'y']

def contains_common_item(arr1, arr2):
    big_array = arr1 + arr2
    big_set = set(big_array)
    if len(big_array) == len(big_set):
        return False
    return True


print(contains_common_item(arr1, arr2))
