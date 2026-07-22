import sys

def main():
    try:
        File_name = sys.argv[1]
        New_File = sys.argv[2]

        fobj1 = open(File_name,"r")
        fobj2 = open(New_File,"r")

        if fobj1.read() == fobj2.read():
            print("Sucess")

        else:
            print("Failure")
    
        fobj1.close()
        fobj2.close()


    except FileNotFoundError:
        print(f"{File_name} does not exist")

    except Exception as e :
        print(e)


if __name__ == "__main__":
    main()