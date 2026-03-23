class Books:
    def __init__(self, title, author, genre, isbn_number, review="No review", rating=0):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn_number = isbn_number
        self.review = review
        self.rating = rating

    def add_review(self, new_review, new_rating):
        self.review = new_review
        self.rating = new_rating

    def fix_caps(self):
        self.title = self.title.title()
        self.author = self.author.title()

    def format_isbn(self):
        isbn = str(self.isbn_number).replace("-", "")
        if len(isbn) == 13:
            self.isbn_number = (
                isbn[0:3] + "-" +
                isbn[3:5] + "-" +
                isbn[5:10] + "-" +
                isbn[10:12] + "-" +
                isbn[12]
            )

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

# Displaying all books with reviews and ratings
print("====== BOOK COLLECTION ======")

for i, book in enumerate(books_list, start=1):
    print("Book", i)
    print(" Title :", book.title)
    print(" Author:", book.author)
    print(" Genre :", book.genre)
    print(" ISBN  :", book.isbn_number)

    if book.review != "No review":
        print(" Review:", book.review)
        print(" Rating:", book.rating)

    print("==============================")

while True:
    choice = input("Which book would you like to review? Enter number or 'done': ").lower()

    if choice == "done":
        break

    if not choice.isdigit():
        print("Please enter a number.")
        continue

    choice = int(choice)

    if choice < 1 or choice > len(books_list):
        print("Invalid book number.")
        continue

    book = books_list[choice - 1]

    new_review = input("Enter your review: ").strip()
    while new_review == "":
        print("Review cannot be empty.")
        new_review = input("Enter your review: ").strip()

    new_rating = input("Enter a rating out of 10: ")
    while not new_rating.isdigit() or int(new_rating) < 1 or int(new_rating) > 10:
        print("Rating must be between 1 and 10.")
        new_rating = input("Enter a rating out of 10: ")

    book.add_review(new_review, int(new_rating))
    print("Review added!\n")

# fixing capitilisation and formatting ISBN for all books
for book in books_list:
    book.fix_caps()
    book.format_isbn()