import schedule
import time
import datetime

def CreateLog():
    CurrentTime = datetime.datetime.now()

    FileName = "MarvellousLog_" + CurrentTime.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"

    fobj = open(FileName, "w")

    fobj.write("Log file created successfully.\n")
    fobj.write("Creation Time : " + CurrentTime.strftime("%d-%m-%Y %I:%M:%S %p"))

    fobj.close()

    print("Log file created successfully.")

def main():
    schedule.every(10).minutes.do(CreateLog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()