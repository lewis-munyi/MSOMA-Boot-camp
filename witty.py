def get_number():
    number = int(input("Enter number:\n"))
    while number % 2 != 0:
        print ("Come on")
        print(number%2)
        get_number()
        pass
    else:
        print("Yaay! You got it right.")
        exit()
        pass

get_number()
