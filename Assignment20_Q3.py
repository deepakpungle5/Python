import threading

def EvenList(n):
    sum = 0
    for i in n:
        if i % 2 == 0:
            sum = sum + i
        
    print("Sum of Even No is : ",sum)
  

def OddList(n):
    sum = 0
    for i in n:
        if i % 2 != 0:
            sum = sum + i

    print("Sum of Odd No is : ",sum)
    


def main():
    Data = list()
    no = int(input("Enter a number : "))
    print("Enter Elements ")
    for i in range(no):
        value = int(input())
        Data.append(value)

    t1 = threading.Thread(target=EvenList, args=(Data,))
    t2 = threading.Thread(target= OddList, args=(Data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()