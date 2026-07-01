def primeno(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


def main():

    no = int(input("Enter a number : "))
    ret = primeno(no)

    if ret == True:
        print("Number is Prime")

    else:
        print("Number is not Prime")


if __name__ == "__main__":
    main()