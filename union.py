"""Given two sorted array of sizes m and n in which all elements are distinct,
   Find the union between them."""


def unionArray(x, y, m, n):
    union_arr = []

    for i in range(m):
        if x[i] not in union_arr:
            union_arr.append(x[i])

    for j in range(n):
        if y[j] not in union_arr:
            union_arr.append(y[j])

    
    return union_arr

lst_a = [1, 2, 2, 3, 4, 5]
lst_b = [2, 3, 5, 6]

print(unionArray(lst_a, lst_b, len(lst_a), len(lst_b)))

# This is the second array

def union_array(arr1, arr2):
    arr1 = set(arr1)
    arr2 = set(arr2)

    return arr1.union(arr2)


lst_a = [1, 2, 3, 4, 5]
lst_b = [2, 3, 5, 6]
print(union_array(lst_a, lst_b))