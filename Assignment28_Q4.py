def main():
    try:
        existing_file = input("Enter Existing File Name : ")
        new_file = input("Enter New File Name : ")

        fobj1 = open(existing_file, "r")
        content = fobj1.read()

        fobj2 = open(new_file, "w")
        fobj2.write(content)

        fobj1.close()
        fobj2.close()

        print(f"Data copied successfully from {existing_file} to {new_file}")

    except FileNotFoundError:
        print(f"{existing_file} does not exist")


if __name__ == "__main__":
    main()