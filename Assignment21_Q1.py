import threading

def Prime(data):

    Prime = []

    for no in data:
        if no <= 1:
            continue

        for i in range(2, no):
            if no % i == 0:
                break
        else:
            Prime.append(no)

    print("Prime no is : ",Prime)

def NonPrime(data):
        
    Non_prime = []

    for no in data:
        if no <= 1:
            Non_prime.append(no)
            continue

        for i in range(2, no):
            if no % i == 0:
                Non_prime.append(no)
                break

    print("Non prime number is : ",Non_prime)
    

def main():
    data = list()
    n = int(input("Enter a Number : "))
    print("Enter Elements : ")
    for i in range(n):
        value = int(input())
        data.append(value)


    t1 = threading.Thread(target=Prime, args=(data,))
    t2 = threading.Thread(target= NonPrime, args=(data,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()


if __name__ == "__main__":
    main()