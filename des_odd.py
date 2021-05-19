"""Let all numbers come before even numbers, and sort the numbers in ascending order
  and even numbers in descending order."""


def oddAscEvenDesc(inp):
    oddsubstr = ''
    evensubstr = ''

    for char in inp:
        if int(char)%2==0:
            evensubstr += char
        else:
            oddsubstr += char

    temp = sorted(oddsubstr) + sorted(evensubstr, reverse=True)

    return ''.join(temp)


x = '978231456'
print(oddAscEvenDesc(x))