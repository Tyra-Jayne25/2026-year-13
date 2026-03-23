class Books:
    def __init__(self, title, author, genre, isbn_number, review="No review", rating=0):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn_number = isbn_number
        self.review = review
        self.rating = rating

    # Method to update review + rating
    def add_review(self, new_review, new_rating):
        self.review = new_review
        self.rating = new_rating

    # Method to capitalise title + author
    def fix_caps(self):
        self.title = self.title.title()
        self.author = self.author.title()

    # Method to format ISBN
    def format_isbn(self):
        isbn = str(self.isbn_number).replace("-", "")
        if len(isbn) == 13:
            self.isbn_number = isbn[0:3] + "-" + isbn[3:5] + "-" + isbn[5:10] + "-" + isbn[10:12] + "-" + isbn[12]
# list to store unlimited books
books_list = []

print("Enter your book collection information:")

while True:
    # Title
    title = input("Enter the book's title: ").strip()
    while title == "":
        print("Title cannot be empty.")
        title = input("Enter the book's title: ").strip()

    # Author
    author = input("Enter the book's author: ").strip()
    while author == "":
        print("Author cannot be empty.")
        author = input("Enter the book's author: ").strip()

    genre = input("Enter the book's genre: ")

    # ISBN must be numbers
    isbn_number = input("Enter the book's ISBN number (digits only): ")
    while not isbn_number.isdigit():
        print("ISBN must be numbers only.")
        isbn_number = input("Enter the book's ISBN number: ")

    # Create book object
    new_book = Books(title, author, genre, isbn_number)
    books_list.append(new_book)

    more = input("Do you have more books to enter? (yes/no): ").lower()
    if more != "yes":
        break
    print()

print("\n====== BOOK COLLECTION ======\n")

for i in range(len(books_list)):
    book = books_list[i]
    print("Book", i + 1)
    print(f" Title : {book.title}")
    print(f" Author: {book.author}")
    print(f" Genre : {book.genre}")
    print(f" ISBN  : {book.isbn_number}")
    print(f" Review: {book.review}")
    print(f" Rating: {book.rating}/5")
    print("==============================")