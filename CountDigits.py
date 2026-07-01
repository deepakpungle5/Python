# write a program which accepts one number and print count of digits in that no.

def main():
    count = 0

    no = int(input("Enter a number : "))

    while no > 0:
        no =  no // 10
        count = count + 1

    print(count)


if __name__ == "__main__":      
    main()

