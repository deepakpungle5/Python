# write a lambda function using reduce() which accept a list of numbers and returns maximum elements.

from functools import reduce

maximmum = lambda n1, n2 : n1 if n1 > n2 else n2

def main():
    data = list()
    n = int(input("Enter no of element : "))
    
    for i in range(1, n+1):
        lst = int(input("Enter Element : "))
        data.append(lst)

    rdata = reduce(maximmum , data)
    print("Data after reduce : ",rdata)

if __name__ == "__main__":
    main()