import sys

def main():
    try:
        File_name = sys.argv[1]
        Find = sys.argv[2]

        fobj = open(File_name, "r")

        data = fobj.read()

        Words = data.split()

        Count = 0

        for word in Words:
            if word == Find:
                Count += 1

        print(f'"{Find}" appears {Count} time(s) in {File_name}')

        fobj.close()

    except FileNotFoundError:
        print(f"{File_name} does not exist")

    except IndexError:
        print("Usage : python Program.py <FileName> <String>")


if __name__ == "__main__":
    main()