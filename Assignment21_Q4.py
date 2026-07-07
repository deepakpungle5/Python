import threading
from functools import reduce

Sum = lambda no1, no2 : no1 + no2
mul = lambda no1,no2 : no1 * no2

def Addition(data):
    ret = reduce(Sum,data)
    print("Addition of list element : ",ret)

def Product(data):
    ret = reduce(mul,data)
    print("Product of list elemets : ",ret)
    

def main():
    Data = list()
    no = int(input("Enter a number : "))
    print("Enter Elements ")
    for i in range(no):
        value = int(input())
        Data.append(value)

    t1 = threading.Thread(target=Addition, args=(Data,))
    t2 = threading.Thread(target= Product, args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()