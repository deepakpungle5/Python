# Write a lambda function which accepts one number and returns cube of that number.

cube = lambda no : no * no * no

def main():
    a = int(input("Enter a Number : "))
    ret = cube(a)
    print("Cube of the nnumber is : ",ret)

if __name__ == "__main__":
    main()
    