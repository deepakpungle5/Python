# write a program which contains one function name as Add() which accepts  two number fromm user and return addition of that two number.

def Add(no1, no2):
    return no1 + no2

def main():
    n1 = int(input("Enter First Numbeer : "))
    n2 = int(input("Enter Second Number : "))
    ret = Add(n1,n2)

    print(f"Addition of {n1} and {n2} is : ",ret)



if __name__ == "__main__":
    main()