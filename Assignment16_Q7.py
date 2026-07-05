# Write a program which contains one function that accept one number from user and returns true if number is divisible by 5 otherwise return false

def Demo(no):
    if no % 5 == 0:
        return True 
    else:
        return False

def main():
    value = int(input("Enter a number : "))

    ret = Demo(value)

    if ret == True:
        print(f"{value} is divisible by 5 ")

    else:
        print(f"{value} is not divisible by 5 ")
        

if __name__ == "__main__":
    main()