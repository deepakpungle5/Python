# write a program which accepts one number and check whether it is palindrome or not

def main():
    rev = 0
    no = int(input("Enter a Number : "))
    temp = no

    while no > 0:
        ld = no % 10
        rev = rev * 10 + ld
        
        no = no // 10

    if temp == rev:
        print("Given Integer is Palindome")

    else:
        print("nOT A Palindrome")

if __name__ == "__main__":      
    main()

