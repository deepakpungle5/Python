# write a program which accept no from user and return addition of its factors.

def AddFactors(no):
    sum = 0
    for i in range(1,(no // 2) + 1):
        if no % i == 0:
            sum = sum + i

    return sum


def main():
    n = int(input("Enter a number : "))
    ret = AddFactors(n)
    print("Addition of factors of given number is : ",ret)

if __name__ == "__main__":
    main()