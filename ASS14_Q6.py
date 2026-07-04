# Write a lambda function which accept one number and returns True if number is Odd otherwise False.

OddEven = lambda no : (no % 2 != 0)

def main():
    a = int(input("Enteer a  Number : "))
    ret = OddEven(a)
    print(ret)

if __name__ == "__main__":
    main()