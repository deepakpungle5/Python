def main():
    count = 0
    try:
        name = input("Enter File Name : ")

        fobj = open(name, "r")

        res = fobj.read()
        
        words = res.split()

        print(f"Total Number of Words in {name} is {len(words)}")

        fobj.close()

    except FileNotFoundError:
        print(f"{name} does not exist")


if __name__ == "__main__":
    main()