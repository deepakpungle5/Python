# Write a program which accept name from user and display length of its name.

def main():
    count = 0
    name = input("Enter Name : ")
    for i in name:
        count = count +1

    print("Length of Name is : ",count)
    
if __name__ == "__main__":
    main()
