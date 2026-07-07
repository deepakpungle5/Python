# write a program which accept n number from user and store it into the list, return minimum no from list.

from functools import reduce
minimum = lambda n1,n2 : n2 if n1 > n2 else n1

def main():
    Data = list()
    no = int(input("Enter Size of list : "))
    for i in range(no):
        value = int(input("Enter values in lisst : "))
        Data.append(value)

    ans = reduce(minimum,Data)
    print("Smalleest Number from the list is : ",ans)
        


if __name__ == "__main__":
    main()