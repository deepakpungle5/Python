# Write a program which accept marks and display grades

def main():
    marks = int(input("Enter Marks : "))    

    if (marks >= 75):
        print("Congratulation You Got Distinction ")

    elif(marks >= 60):
        print("Congratulation you got first class ")

    elif(marks >= 50):
        print("You Got Second Class ")

    else:
        print("Fail..!!!!")

 

if __name__ == "__main__":
    main() 