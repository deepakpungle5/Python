import schedule
import time
import os

Directory = input("Enter Directory Path : ")

def DeleteEmptyFiles():
    try:
        fobj = open("DeleteLog.txt", "a")

        for FolderName, SubFolder, FileNames in os.walk(Directory):
            for File in FileNames:

                FilePath = os.path.join(FolderName, File)

                try:
                    if os.path.getsize(FilePath) == 0:
                        os.remove(FilePath)

                        print(FilePath, "Deleted")
                        fobj.write(FilePath + " Deleted\n")

                except PermissionError:
                    print("Permission Denied :", FilePath)

        fobj.close()

    except Exception as e:
        print(e)


def main():
    schedule.every().hour.do(DeleteEmptyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()