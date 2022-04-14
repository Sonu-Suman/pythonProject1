a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# comman item in both list and also not repeating
# This is first type of solution
lst1 = []
lst2 = []

for i in a:
    if i in b:
        lst1.append(i)


for item in lst1:
    if item not in lst2:
        lst2.append(item)

print(lst2)

# less number of lines code compare to case 1.

lst3 = []

result = [number for number in a if number in b]

for i in result:
    if i not in lst3:
        lst3.append(i)

print(lst3)


# This is second type of solution
l1 = []

for i in a:
    if i in b:
        if i not in l1:
            l1.append(i)

print(l1)


# non-common item in both list 
# This is first type of solution
lst4 = []

for i in a:
    if i not in b:
        lst4.append(i)

for i in b:
    if i not in a:
        lst4.append(i)

print(lst4)

# This is also first type but in this less number lines code.

res = [item for item in a if item not in b]

for i in b:
    if i not in a:
        res.append(i)

print(res)