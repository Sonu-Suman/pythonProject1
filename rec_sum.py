# Finding the sum of array using recuersive methode


def recur_sum(arr, i):
    if i<1:
        return arr[i]
    else:
        return arr[i] + recur_sum(arr, i-1)

arr = [-1, 2, -3, 4, 5]


print(recur_sum(arr, len(arr)-1))