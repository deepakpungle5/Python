import schedule
import time

def LunchTime():
    print("Lunch Time!")

def WrapTime():
    print("Wrap up work")

def main():
    schedule.every().day.at("13:00").do(LunchTime)
    schedule.every().day.at("18:00").do(WrapTime)

    while True:
        schedule.run_pending()
        time.sleep(5)

if __name__ == "__main__":
    main()