import schedule
import time
import os
import datetime

Path = input("Enter Directory Path : ")

def CountFiles():
    Count = 0

    for item in os.listdir(Path):
        FullPath = os.path.join(Path, item)

        if os.path.isfile(FullPath):
            Count += 1

    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open("DirectoryCountLog.txt", "a")

    fobj.write(f"Directory : {Path}\n")
    fobj.write(f"Number of Files : {Count}\n")
    fobj.write(f"Date and Time : {CurrentTime}\n")
    fobj.write("---------------------------------\n")

    fobj.close()

    print("Directory details saved.")

def main():
    schedule.every(5).minutes.do(CountFiles)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()