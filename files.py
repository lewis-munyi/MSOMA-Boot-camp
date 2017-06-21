def read_file(food):
    f = open(food, 'r')
    print(f.read())
    f.close()
read_file('food')