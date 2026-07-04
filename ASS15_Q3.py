# write a lambda function using filter() which accept a list of numbers and returns a list of odd numbers.

odd = lambda no : no % 2 != 0
 
def main():
    data = list()
    n = int(input("Enter No of element : "))

    for i in range(1 ,n+1):
        lst = int(input("Enter Element : "))
        data.append(lst)

    fdata = list(filter(odd, data))
    print("Data after filter : ",fdata)

if __name__ == "__main__":
    main()