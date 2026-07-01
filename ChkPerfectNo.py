# Write a program which accepts one number and checks wheather it is perfect no or not 

def main():
    sum = 0
    no = int(input("Enter a number : "))
    
    for i in range(1, no):
        if (no % i == 0):
            sum = sum + i

    if sum == no:
        print("Given no is Perfect")

    else:
        print("Given no is not perfect")



if __name__ == "__main__":
    main() 