# for every no in given list, count how many prime numbers exists between 1 and n using multiprocessing pool.
import  multiprocessing
def PrimeCount(no):
    count = 0

    for i in range(2, no + 1):
        flag = True

        for j in range(2, i):
            if i % j == 0:
                flag = False
                break

        if flag:
            count = count + 1

    return count


def main():
    Data = list()
    result = list()

    size = int(input("Enter Size : "))
    print("Enter List Values : ")
    for i in range(size):
        Data.append(int(input()))
    
    pobj = multiprocessing.Pool()
    result = pobj.map(PrimeCount,Data)

    pobj.close()
    pobj.join

    print(result)
    

if __name__ == "__main__":
    main()