import multiprocessing,os

def SumOdd(no):
    sum = 0
    for i in range(1,no+1,2):
        sum = sum + i

    return sum


def main():
    data = [1000000,2000000,3000000,4000000,5000000]
    result = []

    pobj = multiprocessing.Pool()
    result = pobj.map(SumOdd,data)

    pobj.close()
    pobj.join()
    
    
    print("Process ID : ",os.getpid())
    print("Input Numbers : ",data)
    print("Sum of Odd numbers : ",result)

if __name__ == "__main__":
    main()
