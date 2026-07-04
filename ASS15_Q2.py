# write a lambda function using filter() which accept a list of numbers and returns a list of even numbers.

Even = lambda no : no % 2 == 0

def main():
    Data = list()
    a = int(input("Enter No Of Element : "))
    for i in range(1,a+1):
        b = int(input("Enter Elements : "))
        Data.append(b)

    Fdata = list(filter(Even,Data))
    print("Data after filter : ",Fdata)

if __name__ == "__main__":
    main()