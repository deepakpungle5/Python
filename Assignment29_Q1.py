import os

def main():
    FileName = input("Enter File Name : ")

    if os.path.exists(FileName):
        print(f"{FileName} exists in the current directory.")
    else:
        print(f"{FileName} does not exist in the current directory.")

if __name__ == "__main__":
    main()