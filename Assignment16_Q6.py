# Write a program which accept number from user and check wheather that number is positive or negative or zero

def ChkNo(no):
    if no == 0:
        print("Number is Zero ")
    
    elif no > 0 :
        print("Number is Positive ")
    
    elif no < 0:
        print("Number is Negative ")

    else:
        print("Please Enter Valid No ")


def main():
    no = int(input("Enter a number : "))
    ret = ChkNo(no)


if __name__ == "__main__":
    main()