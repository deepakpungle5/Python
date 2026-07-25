import schedule
import time
import shutil
import os
import datetime

def Backup():
    try:
        Source = input("Enter Source File Path : ")
        Destination = input("Enter Destination Directory : ")

        FileName = os.path.basename(Source)
        Name, Extension = os.path.splitext(FileName)

        CurrentTime = datetime.datetime.now().strftime("%d_%m_%Y_%H_%M_%S")

        BackupFile = f"{Name}_{CurrentTime}{Extension}"

        DestinationPath = os.path.join(Destination, BackupFile)

        shutil.copy(Source, DestinationPath)

        LogTime = datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

        with open("backup_log.txt", "a") as fobj:
            fobj.write(f"Backup completed successfully at {LogTime}\n")

        print("Backup completed successfully.")

    except Exception as e:
        print(e)


def main():
    schedule.every().hour.do(Backup)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()