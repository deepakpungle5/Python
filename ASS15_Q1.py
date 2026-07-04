# write a lambda function using map() which accept a list of numbers and returns a list of Square of each numbers.

Square = lambda a : a * a

def main():
    Data = list()
    n = int(input("Enter no of element : "))

    for i in range(1, n+1):
        a = int(input("Enter Element : "))
        Data.append(a)

    mdata = list(map(Square,Data))
    print("Data after map : ",mdata)

if __name__ == "__main__":
    main()