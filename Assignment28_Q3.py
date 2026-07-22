def main():
    count = 0
    try:
        name = input("Enter a File Name : ")

        fobj = open(name,"r")

        res = fobj.read()

        print(res)

        fobj.close()


    except FileNotFoundError:
        print(f"{name} does not exist")


if __name__ == "__main__":
    main()