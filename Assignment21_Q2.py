import threading
from functools import reduce


maximum = lambda no1,no2 : no1 if no1>no2 else no2
minimum = lambda no1,no2 : no1 if no1<no2 else no2
    
def MaxThread(data):
    ret =  reduce(maximum,data)
    print("max no is : ",ret)

def MinThread(data):

    ret =  reduce(minimum,data)
    print("min no is : ",ret)

   
def main():
    Data = list()
    no = int(input("Enter a number : "))
    print("Enter Elements ")
    for i in range(no):
        value = int(input())
        Data.append(value)

    t1 = threading.Thread(target=MaxThread, args=(Data,))
    t2 = threading.Thread(target= MinThread, args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()