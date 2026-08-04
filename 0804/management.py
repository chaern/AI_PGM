# Library Management System

import os


# Book Class
class Book:
    def __init__(self, book_id, title, author, borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed = borrowed


    # Show book information
    def show_book(self):
        status = "Borrowed" if self.borrowed else "Available"

        print(
            f"ID: {self.book_id}, "
            f"Title: {self.title}, "
            f"Author: {self.author}, "
            f"Status: {status}"
        )


    # Convert data for file saving
    def save_data(self):
        return f"{self.book_id},{self.title},{self.author},{self.borrowed}"



# Library Class
class Library:

    def __init__(self):
        self.books = []


    # Register book
    def add_book(self):

        book_id = int(input("Enter book ID: "))
        title = input("Enter book title: ")
        author = input("Enter author: ")


        book = Book(book_id, title, author)

        self.books.append(book)

        print("Book registered successfully.")



    # Search book
    def search_book(self):

        title = input("Enter title to search: ")


        for book in self.books:

            if book.title == title:

                print("Book found.")
                book.show_book()
                return


        print("Book not found.")



    # Borrow book
    def borrow_book(self):

        book_id = int(input("Enter book ID: "))


        for book in self.books:

            if book.book_id == book_id:


                if book.borrowed:
                    print("This book is already borrowed.")
                    return


                book.borrowed = True

                print("Borrow completed.")
                return


        print("Book not found.")



    # Return book
    def return_book(self):

        book_id = int(input("Enter book ID: "))


        for book in self.books:

            if book.book_id == book_id:


                if not book.borrowed:
                    print("This book is already available.")
                    return


                book.borrowed = False

                print("Return completed.")
                return


        print("Book not found.")



    # Delete book
    def delete_book(self):

        book_id = int(input("Enter book ID to delete: "))


        for book in self.books:

            if book.book_id == book_id:

                self.books.remove(book)

                print("Book deleted.")
                return


        print("Book not found.")



    # Show all books
    def show_books(self):

        if len(self.books) == 0:
            print("No books registered.")
            return


        print("\n===== Book List =====")

        for book in self.books:
            book.show_book()



    # Save data to file
    def save_file(self):

        file = open("books.txt", "w", encoding="utf-8")


        for book in self.books:
            file.write(book.save_data() + "\n")


        file.close()

        print("Data saved successfully.")



    # Load data from file
    def load_file(self):

        if not os.path.exists("books.txt"):
            return


        file = open("books.txt", "r", encoding="utf-8")


        for line in file:

            data = line.strip().split(",")

            book_id = int(data[0])
            title = data[1]
            author = data[2]
            borrowed = data[3] == "True"


            self.books.append(
                Book(book_id, title, author, borrowed)
            )


        file.close()




# Main Program
def main():

    library = Library()

    # Load saved books
    library.load_file()


    while True:

        print("\n===== Library Management System =====")
        print("1. Register Book")
        print("2. Search Book")
        print("3. Show All Books")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Delete Book")
        print("7. Save File")
        print("8. Exit")


        menu = input("Select menu: ")



        if menu == "1":

            library.add_book()


        elif menu == "2":

            library.search_book()


        elif menu == "3":

            library.show_books()


        elif menu == "4":

            library.borrow_book()


        elif menu == "5":

            library.return_book()


        elif menu == "6":

            library.delete_book()


        elif menu == "7":

            library.save_file()


        elif menu == "8":

            library.save_file()

            print("Program terminated.")

            break


        else:

            print("Invalid menu.")




main()