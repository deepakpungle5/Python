import threading

def Small(str):
    count = 0
    for char in str:
        if 'a' <= char <= 'z':
            count+=1

    print("Name of this thread is : ",threading.current_thread().name)
    print("Id of this thread is : ",threading.get_ident())
    print("Small Character in string : ",count)
    print()


def Capital(str):
    
    count = 0
    for char in str:
        if 'A' <= char <= 'Z':
            count+=1

    print("Name of this thread is : ",threading.current_thread().name)
    print("Id of this thread is : ",threading.get_ident())
    print("Capital Character in string : ",count)
    print()
    

def Digits(str):
    count = 0
    for char in str:
        if '0' <= char <= '9':
            count+=1

    print("Name of this thread is : ",threading.current_thread().name)
    print("Id of this thread is : ",threading.get_ident())
    print("total character in stiring : ",count)
    print()


def main():
    name = input("Enter a name : ")

    t1 = threading.Thread(target=Small, args=(name,))
    t2 = threading.Thread(target= Capital, args=(name,))
    t3 = threading.Thread(target= Digits, args=(name,))

    t1.start()
    t1.join()

    t2.start()
    t2.join()

    t3.start()
    t3.join()

if __name__ == "__main__":
    main()