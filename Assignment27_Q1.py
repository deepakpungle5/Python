class BookName:
    NoOfBooks = 0

    def __init__(self, Book, Author):
        BookName.NoOfBooks += 1
        self.Book = Book
        self.Author = Author

    def Display(self):
        print(f"{self.Book} by {self.Author} No of Books :{BookName.NoOfBooks}")
       


def main():
    obj1 = BookName("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookName("C Programming", "Denis Retiche")
    obj2.Display()

    obj3 = BookName("Java Programming", "James Gosling")
    obj3.Display()


if __name__ == "__main__":
    main()