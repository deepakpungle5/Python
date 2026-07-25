import schedule
import time
import os
import datetime

FileName = input("Enter File Name : ")

def MonitorFile():
    CurrentTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    try:
        Size = os.path.getsize(FileName)

        fobj = open("FileSizeLog.txt", "a")

        fobj.write(f"File Path : {FileName}\n")
        fobj.write(f"File Size : {Size} bytes\n")
        fobj.write(f"Date and Time : {CurrentTime}\n")
        fobj.write("---------------------------------\n")

        fobj.close()

        print("Log Updated.")

    except FileNotFoundError:
        print("File does not exist.")

def main():
    schedule.every(30).seconds.do(MonitorFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()