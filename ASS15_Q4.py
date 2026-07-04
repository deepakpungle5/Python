# write a lambda function using reduce() which accept a list of numbers and returns Addition of all elements.

from functools import reduce

Add = lambda no1, no2 : no1 + no2

def main():
    data = []
    n = int(input("Enter no of element : "))

    for i in range(1, n+1):
        lst = int(input("Enter Elements : "))
        data.append(lst)

    rdata = (reduce(Add , data))
    print("data after reduce is : ",rdata)

if __name__ == "__main__":
    main()