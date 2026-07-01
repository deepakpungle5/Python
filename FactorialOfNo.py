# write a program which accepts one number and print factorial of that no.

def main():

    fact = 1
    no = int(input("Enter a number : "))

    for i in range(1, no+1):
        fact = fact * i
    
    print("factorial of given no is : ",fact)

if __name__ == "__main__":      
    main()

