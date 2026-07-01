# Write a program which accept one number and prints that many numbers in reverse

def main():
    no = int(input("Enter a number : "))
    for i in range(no, 0,  -1):
        print(i)


if __name__ == "__main__":
    main() 