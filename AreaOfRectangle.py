# Write a program which accept length and width of rectangle and print area 

def area(length,width):
    
    return length * width

def main():
    
    a = int(input("Enter Length of rectangle : "))
    b = int(input("Enter width of rectangle : "))
    ret = area(a,b)
    print("Area of rectangle is : ",ret)


if __name__ == "__main__":
    main() 