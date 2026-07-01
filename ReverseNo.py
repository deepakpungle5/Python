# write a program which accepts one number and print reverse of that no.

def main():
    rev = 0
    no = int(input("Enter a number : "))

    while no > 0:
        n1 = no % 10
        rev = rev * 10 + n1

        no =  no // 10
        
    print(rev)


if __name__ == "__main__":      
    main()

