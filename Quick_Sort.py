import random
input_arr = [1, 2, 56, 4, 44, 12, 33838, 14, 15, 18, 199]


def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        index = random.randint(0, len(arr)-1)
        pivot = arr[index]
        left_arr = []
        right_arr = []
        #print(' ')
        #print(pivot)
        for i in range(len(arr)):
            if arr[i] < pivot:
                left_arr.append(arr[i])
            elif arr[i] > pivot:
                right_arr.append(arr[i])

        #left_arr = arr[pivot:]
        #right_arr = arr[0:pivot]
        #print(left_arr)
        #print(right_arr)

        return quick_sort(left_arr) + [pivot] + quick_sort(right_arr)


array = quick_sort(input_arr)
print(array)