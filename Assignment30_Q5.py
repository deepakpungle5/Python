import schedule
import time
import datetime

def task():
    try:
        fobj = open("Marvellous.txt", "a")

        CurrentTime = datetime.datetime.now()

        fobj.write(f"Task executed at : {CurrentTime}\n")

        fobj.close()

        print("Entry added successfully.")

    except Exception as e:
        print(e)


def main():
    schedule.every(5).minutes.do(task)

    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == "__main__":
    main()