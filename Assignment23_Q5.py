import multiprocessing,os

def Factorial(no):
    Fact = 1
    for i in range(1,no+1):
        Fact = Fact * i

    return Fact


def main():
    data = [5,10,15,20,25]
    result = []

    pobj = multiprocessing.Pool()
    result = pobj.map(Factorial,data)

    pobj.close()
    pobj.join()
    
    
    print("Process ID : ",os.getpid())
    print("Input Numbers : ",data)
    print("Factorial : ",result)

if __name__ == "__main__":
    main()
