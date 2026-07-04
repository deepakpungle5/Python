# Write a lambda function which accepts two number and returns minimum number.

MaximunNo = lambda no1, no2 : (no1 < no2)

def main():
    a = int(input("Enter First Number : "))
    b = int (input("Enter Second Number : "))

    ret = MaximunNo(a,b)
    if ret == True:
        print("Minimum No is : ",a)

    else :
        print("Minimum No is : ",b)


if __name__ == "__main__":
    main()
    