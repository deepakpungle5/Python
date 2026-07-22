def main():
    try:
        name = input("Enter File Name : ")

        fobj = open(name, "r")

        Lines = fobj.readlines()
        NoOfLines = len(Lines)

        print(f"Total Number of lines in {name} is {NoOfLines}")

        fobj.close()

    except FileNotFoundError:
        print(f"{name} does not exist")


if __name__ == "__main__":
    main()