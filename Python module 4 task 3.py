largest = 0
smallest = 0

number = int(input("Enter your number: "))
if number != "":
    smallest = largest = number
    while number != "":

        if number < smallest:
            smallest = number
        elif number > largest:
            largest = number
        number = int(input("Enter your number: "))
    else:
        print(largest & smallest)