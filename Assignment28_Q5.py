def main():
    try:
        File_name = input("Enter File Name : ")
        Find = input("Enter Word to find : ")

        fobj = open(File_name, "r")
        res = fobj.read()

        if Find in res:
            print(f"Word '{Find}' is found.")
        else:
            print(f"Word '{Find}' is not found in the file.")

        fobj.close()

    except FileNotFoundError:
        print(f"{File_name} does not exist")


if __name__ == "__main__":
    main()