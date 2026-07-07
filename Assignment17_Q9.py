# write a program which accept a no from user and print no of digits in that numbers.

def main():
    count = 0
    no = int(input("Enter a Number : "))

    while no>0:
        no = no // 10
        count +=1

    print(f"Number of digits in given no is {count}")

if __name__ == "__main__":
    main()
