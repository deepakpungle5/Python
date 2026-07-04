# write a lambda function using filter() which accept a list of numbers and returns the count of even no.

even = lambda no : no % 2 == 0

def main():
    count = 0
    data = list()
    n = int(input("Enter no of element : "))

    for i in range(1, n+1):
        lst = int(input("Enterr element : "))
        data.append(lst)

    fdata = list(filter(even, data))
    print("Data After Filter : ",fdata)
    
    for x in fdata:
        count = count + 1

    print("Count of even no is : ",count)

if __name__ == "__main__":
    main()
