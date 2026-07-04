# write a lambda function using filter() which accept a list of strings and returns list of strings having length greater than 5

greater = lambda st : len(st) > 5

def main():
    data = list()
    n = int(input("Enter no of strings : "))

    for i in range(1, n+1):
        lst = input("Enteer string : ")
        data.append(lst)

    fdata = list(filter(greater , data))
    print("Data After Filter is : ",fdata)

if __name__ == "__main__":
    main()
    