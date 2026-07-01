# write a program which accepts one number and print sum of digits in that no.

def main():
    sum = 0

    no = int(input("Enter a number : "))

    while no > 0:
        n1 = no % 10
        sum = sum + n1

        no =  no // 10
        
    print(sum)


if __name__ == "__main__":      
    main()

