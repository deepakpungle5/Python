# write a program which accepts one number and print all odd no till that number.

def main():

    no = int(input("Enter a number : "))

    for i in range(no+1):
        if (i % 2 != 0):
            print(i)


if __name__ == "__main__":      
    main()

