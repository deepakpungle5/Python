import multiprocessing,os

def SumEven(no):
    sum = 0
    for i in range(2,no+1,2):
        sum = sum + i

    return sum


def main():
    data = [1000000,2000000,3000000,4000000,5000000]
    result = []

    pobj = multiprocessing.Pool()
    result = pobj.map(SumEven,data)

    pobj.close()
    pobj.join()
    
    
    print("Process ID : ",os.getpid())
    print("Input Numbers : ",data)
    print("Sum of Even numbers : ",result)

if __name__ == "__main__":
    main()
