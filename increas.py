lst = [1, 2, 3, 4]

# Set is not true method for sorting bacause sorting methode of set is not working on negative integer.
while True:
    try:
        num = int(input("Enter your number for your set: "))

        if num in lst:
            print("This number is already in set")
            number = False

        if num not in lst:
            lst.append(num)
            print(set(lst))

    except:
        print("Please. Enter valid input")
