def get_greatest_numbers(x, y, z):
    least = min(x,y,z)
    if least == x:
        return y*y+z*z
    elif least == y:
        return x*x + z*z
    elif least == z:
        return x*x + y*y
    else:
        print("Error!")
    

def method2(x,y,z):
    return x**2 + y **2 + z ** 2- min(x,y,z)**2
    
