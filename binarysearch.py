new_list = list(range(1, 257))

def binary_search(alist, item):
    low = 0
    high = len(alist) - 1
    for i in range(len(new_list)):
        mid = int(high/2)
        guess = alist[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else: 
            low = mid + 1
    return None

print(binary_search(new_list, 8))

