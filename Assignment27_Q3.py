class Numbers:
    def __init__(self, Value):
        self.Value = Value

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True

    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    def Factors(self):
        print("Factors are :")
        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")
        print()

    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


def main():
    No = int(input("Enter number : "))

    Obj = Numbers(No)

    if Obj.ChkPrime():
        print("Number is Prime")
    else:
        print("Number is Not Prime")

    if Obj.ChkPerfect():
        print("Number is Perfect")
    else:
        print("Number is Not Perfect")

    Obj.Factors()

    Ans = Obj.SumFactors()
    print("Sum of factors :", Ans)


if __name__ == "__main__":
    main()