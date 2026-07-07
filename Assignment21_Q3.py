import threading
from functools import reduce

counter = 0
lock = threading.Lock()

def ThreadX():
    global counter 
    for i in range(5000000):
        with lock:
            counter += 1

  
def main():
    
    t1 = threading.Thread(target=ThreadX)
    t2 = threading.Thread(target=ThreadX)
    t3 = threading.Thread(target=ThreadX)

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

    print("Value of counter is : ",counter)


if __name__ == "__main__":
    main()