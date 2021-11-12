import math

def binary_search(input_list, item):
    low = 0
    high = len(input_list) - 1

    while low < high:
        mid = math.ceil((low + high) / 2)
        guess = input_list[mid]
        if guess < item:
            low = mid
        elif guess > item:
            high = mid
        else:
            return mid


my_list = [1, 2, 4, 5, 6, 7, 12, 22, 25, 37, 82, 120]

answer = binary_search(my_list, 22)
print(answer)
