# write a lambda function using reduce() which accept a list of numbers and returns the product of all elements.

from functools import reduce

product = lambda n1, n2 : n1 * n2

def main():
    data = list()
    no = int(input("Enter no of element in list : "))

    for i in range(1,no+1):
        lst = int(input("Enter elements : "))
        data.append(lst)

    rdata = reduce(product,data)
    print("product of all elements is : ",rdata)
   

if __name__ == "__main__":
    main()