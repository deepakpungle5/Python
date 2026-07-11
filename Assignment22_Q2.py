# write a program that calculate  factorial of multiple numbers simultanously using Pool.map(). also display process_id, input no and factorial
import multiprocessing,os

def Factorial(no):
    fact = 1

    for i in range(1, no + 1):
        fact = fact * i

    print(f"PID : {os.getpid()}  Input : {no}  Factorial : {fact}")

    return fact

def main():
    Data = []   
    result = []

    no = int(input("Enter List Size : "))
    print("Enter List Element : ")
    for i in range(no):
        Data.append(int(input()))

    pobj =  multiprocessing.Pool()
    result = pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()
    
    print(f"Pid of main : {os.getpid()} ppid of main : {os.getppid()}")
    print("Input Data is : ",Data)
    print("Factorial of Numbers is : ",result)

if __name__ == "__main__":
    main()
