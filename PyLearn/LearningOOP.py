class Book:
    def __init__(self,title = "none", author = "none", pages = 0):
        self.title = title
        self.author = author
        self.pages = pages

    def info(self):
        print(f"Title: {self.title} ")
        print(f"Author: {self.author}")
        print(f"Pages: {self.pages}")

class Horror_Books(Book):
    def __init__(self, title="none", author="none", pages=0):
        super().__init__(title, author)

book1 = Book(title = "Communication English", pages = 500, author = "Darshan Shrestha")
book2 = Book()

book1.info()
book2.info()


h_book1 = Horror_Books()
        