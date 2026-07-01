# write a program which accepts one number and print its factors.

def main():
    no = int(input("Enter a Number : "))
    
    for i in range(1,no+1):
        if (no % i == 0):
            print(i)

if __name__ == "__main__":      
    main()

