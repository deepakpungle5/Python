# write a program which contain one lambda function which accepts one parameter and return power of two.

Square = lambda no : 2 ** no

def main():
    n = int(input("Enter a Number : "))
    ret = Square(n)
    print(ret)

if __name__ == "__main__":
    main()