# write a program which accept one number and prints cube of that number

def Cube(no):
    res =  no * no * no
    return res

def main():
    a = int(input("Enter Number : "))
    ret = Cube(a)
    print("Cube of the number is : ",ret)
    
if __name__ == "__main__":
    main()