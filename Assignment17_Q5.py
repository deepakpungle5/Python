# write a program which accept a number from user and check it is prime or not.

def chkprime(n):
    
    for i in range(2,n):
        if n % i == 0:

            return False
        
    return True



def main():

    no = int(input("Enter a number : "))
    ret = chkprime(no)

    if ret:
        print("Given number is prime number ")

    else:
        print("Given number is not prime number ")

if __name__ =="__main__":
    main()