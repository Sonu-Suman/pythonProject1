"""Given two sorted array of sizes m and n in which all elements are distinct,
   Find the union between them."""


def unionArray(x, y, m, n):
    union_arr = []

    for i in range(m):
        union_arr.append(x[i])

    for j in range(n):
        if y[j] not in union_arr:
            union_arr.append(y[j])

    print(union_arr)
    return

lst_a = [1, 2, 3, 4, 5]
lst_b = [2, 3, 5, 6]

unionArray(lst_a, lst_a, len(list_a), len(list_b))