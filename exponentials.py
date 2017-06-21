key = 0
while key == 0:
    choice = int(input("1. Proceed\n2. Exit\n"))
    if choice == 1:
        base = input("Enter the base:\n")
        exponent = input("Enter the exponent:\n")
        output = int(base) ** int(exponent)
        print(str(base) + " to the power of " + str(exponent) + " is " + str(output) + "\n\n")
        pass
    else:
        key = 1
        pass
    pass
