# Write a program which accept one number and prints that many numbers starting from 1

def main():
    no = int(input("Enter a number : "))
    for i in range(1, no+1):
        print(i)


if __name__ == "__main__":
    main()