import csv
import os


# Book Class
class Book:

    def __init__(self, book_id, title, author, borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed = borrowed


    def show_book(self):

        status = "Borrowed" if self.borrowed else "Available"

        print("------------------------------------")
        print("Book ID :", self.book_id)
        print("Title   :", self.title)
        print("Author  :", self.author)
        print("Status  :", status)
        print("------------------------------------")


# Library Class
class Library:

    def __init__(self):

        self.books = []

        self.load_books()


    # Register Book
    def add_book(self):

        book_id = int(input("Book ID : "))
        title = input("Title : ")
        author = input("Author : ")

        self.books.append(Book(book_id, title, author))

        print("Book registered successfully.")


    # Show All Books
    def show_books(self):

        if len(self.books) == 0:

            print("No books available.")
            return


        print("\n===== Book List =====")

        for book in self.books:

            book.show_book()


    # Search Book
    def search_book(self):

        title = input("Enter title : ")

        for book in self.books:

            if book.title.lower() == title.lower():

                print("\nBook Found")
                book.show_book()
                return


        print("Book not found.")


    # Borrow Book
    def borrow_book(self):

        book_id = int(input("Book ID : "))

        for book in self.books:

            if book.book_id == book_id:

                if book.borrowed:

                    print("Book is already borrowed.")

                else:

                    book.borrowed = True

                    print("Borrow completed.")

                return

        print("Book not found.")


    # Return Book
    def return_book(self):

        book_id = int(input("Book ID : "))

        for book in self.books:

            if book.book_id == book_id:

                if not book.borrowed:

                    print("Book is already available.")

                else:

                    book.borrowed = False

                    print("Return completed.")

                return

        print("Book not found.")


    # Delete Book
    def delete_book(self):

        book_id = int(input("Book ID : "))

        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                print("Book deleted.")

                return

        print("Book not found.")


    # Save CSV File
    def save_books(self):

        with open("books.csv", "w", newline="", encoding="utf-8") as file:

            writer = csv.writer(file)

            writer.writerow(
                ["ID", "Title", "Author", "Borrowed"]
            )

            for book in self.books:

                writer.writerow([
                    book.book_id,
                    book.title,
                    book.author,
                    book.borrowed
                ])

        print("Data saved.")


    # Load CSV File
    def load_books(self):

        if not os.path.exists("books.csv"):
            return

        with open("books.csv", "r", encoding="utf-8") as file:

            reader = csv.reader(file)

            next(reader, None)

            for row in reader:

                if len(row) == 4:

                    self.books.append(

                        Book(
                            int(row[0]),
                            row[1],
                            row[2],
                            row[3] == "True"
                        )

                    )


# Main Program
library = Library()

while True:

    print("\n===== Library Management System =====")
    print("1. Register Book")
    print("2. Show All Books")
    print("3. Search Book")
    print("4. Borrow Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Save File")
    print("8. Exit")

    menu = input("Select Menu : ")

    if menu == "1":

        library.add_book()

    elif menu == "2":

        library.show_books()

    elif menu == "3":

        library.search_book()

    elif menu == "4":

        library.borrow_book()

    elif menu == "5":

        library.return_book()

    elif menu == "6":

        library.delete_book()

    elif menu == "7":

        library.save_books()

    elif menu == "8":

        library.save_books()

        print("Program End")

        break

    else:

        print("Invalid Menu")
