import multiprocessing,os,time

def calculate(no):
    res = 0

    for i in range(1, no + 1):
        res = res + (i ** 5)

    return res
        

def main():

    Data = [1000000,2000000,3000000,4000000,5000000]
    result = []

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()
    result = pobj.map(calculate,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print(result)
    print(f"Time require is : {end_time - start_time:.5f}seconds")


if __name__ == "__main__":
    main()