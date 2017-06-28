def read_file(food):
    f = open(food, 'r')
    print(f.read())
    f.close()
try:
    read_file('food')
except: 
    print("Error")
else:
    print("Else")
finally:
        print("Finally")