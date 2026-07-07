""" Write a program which contains filter() map() and reduce() in it. python application which contains one
list of numbers. list contains the numbers which are accepted from user. filter should filterr out all prime
 no map function will multiply all no with 2 , reduce will return maximum no from list. """

from functools import reduce


def chkprime(no):

    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


Square = lambda no : no * 2
Maximun = lambda no1, no2 : no1 if no1>no2 else no2

def main():

    size = int(input("Enter number of elements : "))
    data = list()
    print("Enter the elements : ")
    for i in range(size):
        no = int(input())
        data.append(no)

    fdata = list(filter(chkprime,data))
    print("data after filter : ",fdata)

    mdata = list(map(Square,fdata))
    print("data after map : ",mdata)

    rdata = reduce(Maximun,mdata)
    print("Addition of elements : ",rdata)

if __name__ == "__main__":
    main()
    

    