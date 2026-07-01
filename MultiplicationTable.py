# write a program which accept one number and print multiplication table of that number.

def main():

    no = int(input("Enter a number : "))

    for i in range(1, 11):
        table = i * no
        print(table, end = " ")

if __name__ == "__main__":  
    main()

