import schedule
import time

FileName = input("Enter File Name : ")

def DisplayFile():
    try:
        fobj = open(FileName, "r")

        Data = fobj.read()

        if len(Data) == 0:
            print("File is empty.")
        else:
            print("File Contents: \n")
            print(Data)

        fobj.close()

    except FileNotFoundError:
        print("File does not exist.")

    except PermissionError:
        print("Permission denied.")

    except OSError:
        print("File cannot be opened.")

def main():
    schedule.every(1).minutes.do(DisplayFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()