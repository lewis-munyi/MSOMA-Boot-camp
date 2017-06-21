user_input = input("Enter number:\n")
try:
   val = int(user_input)
except ValueError:
    
   print("Enter a valid integer!")
   exit()

   # print("Enter a valid integer or a number thats greater than 0")
if val >= 0:
    while int(val) != 0:
        print(val)
        val = val - 1
    else:
        print("0\n Done!")
    pass
else:
    print("Enter a number that's greater than 0\n")
    exit()
    pass
