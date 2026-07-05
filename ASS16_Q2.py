""" write a program which contains one function name as ChkNum() which accepts one parameter as number.
If number is even then it should display "Even number" otherwise display "odd number on console" """

def ChkNum(no):
    if no % 2 == 0:
        return True
    
    else:
        return False
    

def main():
    num = int(input("Enter the number : "))
    ret = ChkNum(num)

    if ret == True:
        print("Even Number ")

    else:
        print("Odd Number")


if __name__ == "__main__":
    main()
