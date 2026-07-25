import schedule
import time
import datetime

def CreateFile():
    CurrentTime = datetime.datetime.now()

    FileName = "File_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName, "w")

    fobj.write(f"Filename : {FileName}\n")
    fobj.write(f"Creation Date : {CurrentTime.strftime('%d-%m-%Y')}\n")
    fobj.write(f"Creation Time : {CurrentTime.strftime('%I:%M:%S %p')}")

    fobj.close()

    print(f"{FileName} created successfully.")

def main():
    schedule.every(1).minutes.do(CreateFile)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()