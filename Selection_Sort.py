def largest(arr):
    large = arr[0]
    large_index = 0
    for i in range(len(arr)):
        if large < arr[i]:
            large_index = i
            large = arr[i]
    return large_index


def selection_sort(arr):
    sorted_arr = []
    for i in range(len(arr)):
        sorted_arr.append(arr.pop(largest(arr)))
    return sorted_arr


input_arr = [1, 2, 56, 4, 44, 12, 33838, 14, 15, 18, 199]
output_arr = selection_sort(input_arr)
print(output_arr)
