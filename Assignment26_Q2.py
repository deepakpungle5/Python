class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):

        self.Radius = float(input("Enter Radius of Circle : "))
    
    def CalculateArea(self):

        self.Area = Circle.PI * self.Radius ** 2

    def CalculateCircumference(self):

        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):

        print("Radius of Circle is : ",self.Radius)
        print("Area of Circle is : ",self.Area)
        print("Circumference of Circle is : ",self.Circumference)

def main():
    c1 = Circle()
    c2 = Circle()

    c1.Accept()
    c1.CalculateArea()
    c1.CalculateCircumference()
    c1.Display()

    c2.Accept()
    c2.CalculateArea()
    c2.CalculateCircumference()
    c2.Display()

if __name__ == "__main__":
    main()
    


