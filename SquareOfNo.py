# write a program which accept one number and prints square of that number

def Square(no):
    res =  no * no
    return res

def main():
    a = int(input("Enter Number : "))
    ret = Square(a)
    print("Square of the number is : ",ret)
    
if __name__ == "__main__":
    main()