# write a program which accept one character and checks wheather it is vowel or consonant.

def main():
    a = input("Enter one Character : ")
    
   
    if (len(a) != 1):
        print("Please Enter Single Character")

    elif a in "aeiouAEIOU":
        print("Character is Vowel")

    else:
        print("Character is Consonant")


if __name__ == "__main__":
    main()