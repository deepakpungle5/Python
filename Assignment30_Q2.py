import schedule
import time
import datetime

def DisplayTime():
    print("Current Date And Time : ",datetime.datetime.now())

def main():
    schedule.every(1).minutes.do(DisplayTime)

    while True:
        schedule.run_pending()
        time.sleep(20)
        
if __name__ == "__main__":
    main()