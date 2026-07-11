# write a program that accept list  of integer and uses Pool.map() to calculate the sum of squares from 1 to n 
# for every element in the list

import multiprocessing

def SumSquare(no):
    sum = 0
    for i in range(1,no+1):
        sum = sum +(i*i)
    return sum


def main():
    Data = list()

    no =  int(input("Enter List Size : "))
    print("Enter Elements : ")
    for i in range(no):
        Data.append(int(input()))


    result = list()
    pobj = multiprocessing.Pool()
    result = pobj.map(SumSquare,Data)

    pobj.close()
    pobj.join()

    print(result)
    

if __name__ == "__main__":
    main()