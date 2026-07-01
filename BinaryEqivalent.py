# write a program which accept one number and print binary equivalent

def main():
    no = int(input("Enter any number :- "))
    Bin = 0
    pow = 0

    while no > 0:
        rem = no % 2
        Bin = Bin + (rem * (10 ** pow))
        pow = pow + 1
        no = no // 2

    print("Binary Equivalent of you number is :- ",Bin)

if __name__ == "__main__":
    main()