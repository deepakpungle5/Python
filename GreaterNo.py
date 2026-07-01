# Write a program which contains one function ChkGreater() that accept two numbers and print the greater number

def ChkGreater(n1,n2):

    if n1 > n2:
        return n1
    
    else:
        return n2

def main():
  
    no1 = int(input("Enter First number : "))
    no2 = int(input("Enter Second number : "))

    ret = ChkGreater(no1, no2)
    print(ret, "is Greater Number")

if __name__ == "__main__":
    main()