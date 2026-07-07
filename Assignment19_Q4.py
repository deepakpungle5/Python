""" Write a program which contains filter() map() and reduce() in it. python application which contains one
list of numbers. list contains the numbers which are accepted from user. filter should filterr out all such 
element which are Even. map function will calculate it square, reduce will return addition of all element. """

from functools import reduce

chkno = lambda no : no % 2 == 0 
Square = lambda no : no ** 2
Addition = lambda no1, no2 : no1 + no2

def main():

    size = int(input("Enter number of elements : "))
    data = list()
    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    fdata = list(filter(chkno,data))
    print("data after filter : ",fdata)

    mdata = list(map(Square,fdata))
    print("data after map : ",mdata)

    rdata = reduce(Addition,mdata)
    print("Addition of elements : ",rdata)

if __name__ == "__main__":
    main()
    

    