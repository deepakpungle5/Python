
# write a program which accept n number from user and store it into list. return addition of all elements from that list.

from functools import reduce
Addition = lambda no1,no2 : no1 + no2

def main():
    Data = list()
    no = int(input("Enter size of list : "))
    for i in range(no):
        value = int(input("Enter Element of list : "))
        Data.append(value)

    SumData = reduce(Addition,Data)

    print("Addition of All the Elements in the list is : ",SumData)




if __name__ == "__main__":
    main()