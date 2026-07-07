# write a program which accept N Number from user and store it into list, accept one another number from user and return  'frequency' of that number from the list.

def Frequency(data,find):
    count = 0
    for i in data:
        if i == find:
            count = count + 1

    return count


def main():
 
    Data = list()
    no = int(input("Enter a Size of the list : "))
    for i in range(no):
        value = int(input("Enter a list element : "))
        Data.append(value)
    
    find = int(input("Enteer Element to search : "))
    
    count = Frequency(Data,find)

    print("Frequency of number in givven data is : ",count)
    

    
if __name__ == "__main__":
    main()