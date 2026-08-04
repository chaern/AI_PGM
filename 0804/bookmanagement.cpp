#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;


// Book Class
class Book {
private:
    int id;
    string title;
    string author;
    bool borrowed;

public:

    Book(int id, string title, string author, bool borrowed = false) {
        this->id = id;
        this->title = title;
        this->author = author;
        this->borrowed = borrowed;
    }


    void showBook() {
        cout << "ID: " << id
            << ", Title: " << title
            << ", Author: " << author
            << ", Status: ";

        if (borrowed)
            cout << "Borrowed";
        else
            cout << "Available";

        cout << endl;
    }


    int getID() {
        return id;
    }


    string getTitle() {
        return title;
    }


    bool isBorrowed() {
        return borrowed;
    }


    void borrowBook() {
        borrowed = true;
    }


    void returnBook() {
        borrowed = false;
    }


    // 파일 저장용 데이터 반환
    string getData() {

        return to_string(id) + " "
            + title + " "
            + author + " "
            + to_string(borrowed);
    }
};




// Library Class
class Library {

private:
    vector<Book> books;


public:


    // Book Registration
    void addBook() {

        int id;
        string title;
        string author;


        cout << "Book ID: ";
        cin >> id;

        cout << "Book Title: ";
        cin >> title;

        cout << "Author: ";
        cin >> author;


        Book book(id, title, author);

        books.push_back(book);

        cout << "Book added successfully.\n";
    }



    // Show all books
    void showBooks() {

        if (books.empty()) {
            cout << "No books available.\n";
            return;
        }


        cout << "\n===== Book List =====\n";

        for (auto& book : books) {
            book.showBook();
        }
    }



    // Search Book
    void searchBook() {

        string title;

        cout << "Enter title to search: ";
        cin >> title;


        for (auto& book : books) {

            if (book.getTitle() == title) {

                cout << "Book found.\n";
                book.showBook();

                return;
            }
        }


        cout << "Book not found.\n";
    }




    // Borrow Book
    void borrowBook() {

        int id;

        cout << "Enter book ID: ";
        cin >> id;


        for (auto& book : books) {

            if (book.getID() == id) {

                if (book.isBorrowed()) {

                    cout << "Already borrowed.\n";
                    return;
                }


                book.borrowBook();

                cout << "Borrow completed.\n";
                return;
            }
        }


        cout << "Book not found.\n";
    }




    // Return Book
    void returnBook() {

        int id;

        cout << "Enter book ID: ";
        cin >> id;


        for (auto& book : books) {

            if (book.getID() == id) {


                if (!book.isBorrowed()) {

                    cout << "This book is already returned.\n";
                    return;
                }


                book.returnBook();

                cout << "Return completed.\n";
                return;
            }
        }


        cout << "Book not found.\n";
    }




    // Delete Book
    void deleteBook() {

        int id;

        cout << "Enter book ID to delete: ";
        cin >> id;


        for (int i = 0; i < books.size(); i++) {


            if (books[i].getID() == id) {


                books.erase(books.begin() + i);

                cout << "Book deleted.\n";

                return;
            }
        }


        cout << "Book not found.\n";
    }





    // Save to File
    void saveFile() {

        fstream file;

        file.open("books.txt", ios::out);


        if (!file) {

            cout << "File error.\n";
            return;
        }


        for (auto& book : books) {

            file << book.getData() << endl;
        }


        file.close();


        cout << "Data saved.\n";
    }





    // Load from File
    void loadFile() {

        fstream file;

        file.open("books.txt", ios::in);


        if (!file)
            return;


        int id;
        string title;
        string author;
        bool borrowed;


        while (file >> id >> title >> author >> borrowed) {

            books.push_back(
                Book(id, title, author, borrowed)
            );
        }


        file.close();
    }

};






int main() {

    Library library;


    // Load saved data
    library.loadFile();


    int menu;


    while (true) {


        cout << "\n===== Library Management System =====\n";
        cout << "1. Register Book\n";
        cout << "2. Search Book\n";
        cout << "3. Show Books\n";
        cout << "4. Borrow Book\n";
        cout << "5. Return Book\n";
        cout << "6. Delete Book\n";
        cout << "7. Save File\n";
        cout << "8. Exit\n";


        cout << "Select menu: ";
        cin >> menu;



        switch (menu) {


        case 1:
            library.addBook();
            break;


        case 2:
            library.searchBook();
            break;


        case 3:
            library.showBooks();
            break;


        case 4:
            library.borrowBook();
            break;


        case 5:
            library.returnBook();
            break;


        case 6:
            library.deleteBook();
            break;


        case 7:
            library.saveFile();
            break;


        case 8:
            library.saveFile();
            cout << "Program terminated.\n";
            return 0;


        default:
            cout << "Invalid menu.\n";
        }

    }


    return 0;
}
