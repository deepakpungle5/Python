import threading

def EvenFactor(n):
    sum = 0
    for i in range(2,n+1,2):
        sum = sum + i
        
    print("Sum of Even No is : ",sum)
  

def OddFactor(n):
    sum = 0
    for i in range(1,n+1,2):
       sum = sum + i

    print("Sum of Odd No is : ",sum)
    


def main():
    
    no = int(input("Enter a number : "))

    t1 = threading.Thread(target=EvenFactor, args=(no,))
    t2 = threading.Thread(target= OddFactor, args=(no,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()