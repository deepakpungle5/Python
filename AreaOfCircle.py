# Write a program which accept radius of circle and print area of circle

def areaOfCircle(Radius):
    pi = 3.14 
    area = Radius * Radius * pi

    return areaOfCircle

def main():
    
    a = int(input("Enter Radius of Circle : "))
    ret = areaOfCircle(a)
    print("Area of Circle is : ",ret)


if __name__ == "__main__":
    main() 