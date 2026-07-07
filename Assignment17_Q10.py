# write a program which accept a no from user and print addition of its digits

def main():
    count = 0
    no = int(input("Enter a Number : "))

    while no>0:
        ld = no%10
        count = count + ld
        no = no // 10

    print("Addition of digits in given no is : ",count)

if __name__ == "__main__":
    main()
