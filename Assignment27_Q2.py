class BankAccount:
    ROI = 10.5

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :", self.Name)
        print("Current Balance :", self.Amount)

    def Deposit(self):
        Value = int(input("Enter amount to deposit : "))
        self.Amount = self.Amount + Value
        print("Amount deposited successfully.")

    def Withdraw(self):
        Value = int(input("Enter amount to withdraw : "))

        if Value <= self.Amount:
            self.Amount = self.Amount - Value
            print("Withdrawal successful.")
        else:
            print("Insufficient Balance.")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():
    Obj1 = BankAccount("Deepak", 10000)

    Obj1.Display()

    Obj1.Deposit()
    Obj1.Display()

    Obj1.Withdraw()
    Obj1.Display()

    Interest = Obj1.CalculateInterest()
    print("Interest :", Interest)


if __name__ == "__main__":
    main()