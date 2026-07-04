# Write a lambda function which accepts one number and returns square of that number.

Square = lambda no : no * no

def main():
    a = int(input("Enter a Number : "))
    ret = Square(a)
    print("Square of the no is : ",ret)

if __name__ == "__main__":
    main()
    