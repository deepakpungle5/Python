def main():
    try:
        File_name = input("Enter File Name : ")

        fobj = open(File_name,"r")
        print(fobj.read())

        fobj.close()

    except FileNotFoundError:
        print(f"{File_name} does not exist")


if __name__ == "__main__":
    main()