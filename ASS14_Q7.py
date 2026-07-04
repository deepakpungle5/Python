# Write a lambda function which accept one number and returns True if divisible by 5.

Divisible = lambda no : (no % 5 == 0)

def main():
    no = int(input("Enter a number : "))
    ret = Divisible(no)
    print(ret)

if __name__ == "__main__":
    main()