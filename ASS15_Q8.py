# write a lambda function using filter() which accept a list of numbers and returns list of number divisible by both 3 and 5

Div = lambda no : no % 3 == 0 and no % 5 == 0

def main():
    data = list()
    n = int(input("Enter no of element : "))

    for i in range(1, n+1):
        lst = int(input("Enterr element : "))
        data.append(lst)

    fdata = list(filter(Div, data))
    print("Data After Filter : ",fdata)

if __name__ == "__main__":
    main()