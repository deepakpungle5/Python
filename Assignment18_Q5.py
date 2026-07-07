""" write a program which accept N number from user and store it into list.
return addition of all prime number from that list.
main python file accept n number fromm user pass each no to chkprime() function which is part of our user define module name as marvellousNum. 
name of the function from main python file should be listprime() """


import MarvellousNum

def listprime(arr):

    sum = 0

    for i in arr:
        if MarvellousNum.chkprime(i):
            sum = sum + i

    return sum


def main():

    size = int(input("Enter number of elements : "))

    data = []

    print("Enter the elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    ret = listprime(data)

    print("Addition of all prime numbers is :", ret)


if __name__ == "__main__":
    main()
    
