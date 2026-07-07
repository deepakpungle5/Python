import threading

def EvenThread():
    print("First 10 even no are : ")
    for i in range(2,21,2):
         print(i)

def OddThread():
    print("Firsrt 10 odd numbers are : ")
    for i in range(1,21,2):
        print(i)
    


def main():
 
    t1 = threading.Thread(target=EvenThread)
    t2 = threading.Thread(target= OddThread)

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()