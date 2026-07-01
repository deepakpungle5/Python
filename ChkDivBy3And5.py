# write a program which accept one number and checks whether it is divisible by 3 and 5

def main():
    a = int(input("Enter Number : "))

    if (a % 3 == 0 and a % 5 == 0):
        print(a, "is Divisible by 3 and 5")

    else:
        print(a, "is not Divisible by 3 and 5")
      
if __name__ == "__main__":
    main()