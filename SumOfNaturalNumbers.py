# write a program which accept one number and print sum of the first N natural numbers.

def main():

    total = 0
    no = int(input("Enter a number : "))

    for i in range(1, no+1):
        total = total + i
    
    print(total)

if __name__ == "__main__":  
    main()

