class Books:
    def __init__(self, title, author, genre, isbn_number):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn_number = isbn_number

# list to store unlimited books
books_list = []

print("Enter your book collection information:")

while True:
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    genre = input("Enter the book's genre: ")
    isbn_number = input("Enter the book's ISBN number: ")

    new_book = Books(title, author, genre, isbn_number)
    books_list.append(new_book)

    more = input("Do you have more books to enter? (yes/no): ").lower()
    if more != "yes":
        break
    print()  # spacing

print("\n====== BOOK COLLECTION ======\n")

for i in range(len(books_list)):
    book = books_list[i]
    print("Book", i + 1)
    print(f" Title : {book.title}")
    print(f" Author: {book.author}")
    print(f" Genre : {book.genre}")
    print(f" ISBN  : {book.isbn_number}")
    print("==============================")