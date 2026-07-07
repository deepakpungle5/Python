""" Write a program which contains filter() map() and reduce() in it. python application which contains one
list of numbers. list contains the numbers which are accepted from user. filter should filterr out all such 
element which is greater than or equal to 70 and less than or equal to 90. map function will increase each
number by 10, reduce will return product of all element. """

from functools import reduce

chkno = lambda no1 : no1>=70 and no1<=90 
inc = lambda no : no+10
product = lambda no1, no2 : no1 * no2

def main():

    size = int(input("Enter number of elements : "))
    data = list()
    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    fdata = list(filter(chkno,data))
    print("data after filter : ",fdata)

    mdata = list(map(inc,fdata))
    print("data after map : ",mdata)

    rdata = reduce(product,mdata)
    print("Product of elements : ",rdata)

if __name__ == "__main__":
    main()
    

    