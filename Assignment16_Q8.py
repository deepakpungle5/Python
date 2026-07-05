# Write a program which accept number from user and print that number of "*" on screen


def main():
    no = int(input("Enter a number : "))
    for i in range(no):
        print("*",end=" ")

    
if __name__ == "__main__":
    main()
