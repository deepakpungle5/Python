import schedule
import time
import os
import shutil

Source = input("Enter Source Directory : ")
Destination = input("Enter Destination Directory : ")

def CopyFiles():
    try:
        if not os.path.isdir(Source):
            print("Source directory does not exist.")
            return

        if not os.path.isdir(Destination):
            print("Destination directory does not exist.")
            return

        fobj = open("CopyLog.txt", "a")

        for file in os.listdir(Source):
            if file.endswith(".txt"):
                SourcePath = os.path.join(Source, file)
                DestinationPath = os.path.join(Destination, file)

                try:
                    shutil.copy(SourcePath, DestinationPath)
                    print(file, "Copied Successfully")
                    fobj.write(file + " Copied Successfully\n")

                except Exception:
                    print(file, "Could not be copied")
                    fobj.write(file + " Could not be copied\n")

        fobj.close()

    except Exception as e:
        print(e)


def main():
    schedule.every(10).minutes.do(CopyFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()