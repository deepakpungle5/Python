import schedule
import time
import os
import datetime

def ScanDirectory():
    Path = input("Enter Directory Path : ")

    Files = 0
    Directories = 0

    for item in os.listdir(Path):
        FullPath = os.path.join(Path, item)

        if os.path.isfile(FullPath):
            Files += 1
        elif os.path.isdir(FullPath):
            Directories += 1

    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    print("Directory Scanned :", Path)
    print("Total Files :", Files)
    print("Total Subdirectories :", Directories)
    print("Scan Time :", CurrentTime)
    print("----------------------------------")


def main():
    schedule.every(1).minutes.do(ScanDirectory)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()