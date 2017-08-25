# binary search

def binary_search(list, item):
    low  = 0
    high = len(list) -1

    while low <= high:
        mid = int((low+ high)/2)
        guess = list[mid]
        if guess == item:
            return mid
        if guess > item:
            high = mid -1
        else:
            low = mid + 1

    return None

# test case:
my_list = [1,3,4,7,9]
print(binary_search(my_list, 3) ) # => 1
print(binary_search(my_list, -1 ))# => None
