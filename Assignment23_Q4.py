import multiprocessing,os

def CountOdd(no):
    count = 0
    for i in range(1,no+1,2):
        count = count + 1

    return count


def main():
    data = [1000000,2000000,3000000,4000000,5000000]
    result = []

    pobj = multiprocessing.Pool()
    result = pobj.map(CountOdd,data)

    pobj.close()
    pobj.join()
    
    
    print("Process ID : ",os.getpid())
    print("Input Numbers : ",data)
    print("Odd number Count : ",result)

if __name__ == "__main__":
    main()
