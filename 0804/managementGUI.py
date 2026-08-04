import csv
import os
import tkinter as tk
from tkinter import messagebox


# Book Class
class Book:

    def __init__(self, book_id, title, author, borrowed=False):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.borrowed = borrowed

    def get_status_str(self):
        return "Borrowed" if self.borrowed else "Available"


# Library GUI Application
class LibraryApp:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("600x550")

        self.books = []
        self.load_books()

        # 상단 입력 폼 프레임
        form_frame = tk.LabelFrame(root, text="Book Information", padx=10, pady=10)
        form_frame.pack(fill="x", padx=10, pady=10)

        tk.Label(form_frame, text="Book ID:").grid(
            row=0, column=0, sticky="w", pady=2
        )
        self.entry_id = tk.Entry(form_frame, width=30)
        self.entry_id.grid(row=0, column=1, pady=2)

        tk.Label(form_frame, text="Title:").grid(
            row=1, column=0, sticky="w", pady=2
        )
        self.entry_title = tk.Entry(form_frame, width=30)
        self.entry_title.grid(row=1, column=1, pady=2)

        tk.Label(form_frame, text="Author:").grid(
            row=2, column=0, sticky="w", pady=2
        )
        self.entry_author = tk.Entry(form_frame, width=30)
        self.entry_author.grid(row=2, column=1, pady=2)

        # 버튼 프레임
        btn_frame = tk.Frame(root, padx=10, pady=5)
        btn_frame.pack(fill="x", padx=10)

        tk.Button(
            btn_frame,
            text="Register",
            width=12,
            bg="#d1e7dd",
            command=self.add_book,
        ).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(
            btn_frame,
            text="Show All",
            width=12,
            bg="#cfe2ff",
            command=self.show_books,
        ).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(
            btn_frame,
            text="Search",
            width=12,
            bg="#fff3cd",
            command=self.search_book,
        ).grid(row=0, column=2, padx=5, pady=5)
        tk.Button(
            btn_frame,
            text="Delete",
            width=12,
            bg="#f8d7da",
            command=self.delete_book,
        ).grid(row=0, column=3, padx=5, pady=5)

        tk.Button(
            btn_frame,
            text="Borrow",
            width=12,
            bg="#e2d9f3",
            command=self.borrow_book,
        ).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(
            btn_frame,
            text="Return",
            width=12,
            bg="#fcf8e3",
            command=self.return_book,
        ).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(
            btn_frame,
            text="Save File",
            width=12,
            bg="#d1ecf1",
            command=self.save_books,
        ).grid(row=1, column=2, padx=5, pady=5)
        tk.Button(
            btn_frame,
            text="Exit",
            width=12,
            bg="#f8d7da",
            command=self.on_closing,
        ).grid(row=1, column=3, padx=5, pady=5)

        # 결과 출력 텍스트 상자
        output_frame = tk.LabelFrame(
            root, text="System Output & Book List", padx=10, pady=10
        )
        output_frame.pack(fill="both", expand=True, padx=10, pady=10)

        self.text_output = tk.Text(output_frame, wrap="word", height=15)
        self.text_output.pack(side="left", fill="both", expand=True)

        scrollbar = tk.Scrollbar(
            output_frame, command=self.text_output.yview
        )
        scrollbar.pack(side="right", fill="y")
        self.text_output.config(yscrollcommand=scrollbar.set)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def log(self, message):
        """텍스트 박스에 메시지 출력"""
        self.text_output.insert(tk.END, message + "\n")
        self.text_output.see(tk.END)

    def clear_inputs(self):
        """입력 필드 초기화"""
        self.entry_id.delete(0, tk.END)
        self.entry_title.delete(0, tk.END)
        self.entry_author.delete(0, tk.END)

    # 1. Register Book
    def add_book(self):
        try:
            book_id = int(self.entry_id.get())
            title = self.entry_title.get().strip()
            author = self.entry_author.get().strip()

            if not title or not author:
                messagebox.showerror(
                    "Error", "Title and Author cannot be empty."
                )
                return

            # 중복 ID 체크
            for book in self.books:
                if book.book_id == book_id:
                    messagebox.showerror("Error", "Book ID already exists.")
                    return

            self.books.append(Book(book_id, title, author))
            self.log(
                f"[Success] Book registered: ID({book_id}), Title({title})"
            )
            self.clear_inputs()
        except ValueError:
            messagebox.showerror("Error", "Book ID must be a valid number.")

    # 2. Show All Books
    def show_books(self):
        self.text_output.delete("1.0", tk.END)
        if not self.books:
            self.log("No books available.")
            return

        self.log("===== Book List =====")
        for book in self.books:
            self.log("-" * 40)
            self.log(f"Book ID : {book.book_id}")
            self.log(f"Title   : {book.title}")
            self.log(f"Author  : {book.author}")
            self.log(f"Status  : {book.get_status_str()}")
        self.log("-" * 40)

    # 3. Search Book
    def search_book(self):
        title = self.entry_title.get().strip()
        if not title:
            messagebox.showerror(
                "Error", "Please enter a title in the Title field to search."
            )
            return

        self.text_output.delete("1.0", tk.END)
        found = False
        for book in self.books:
            if book.title.lower() == title.lower():
                self.log("\n[Book Found]")
                self.log(f"Book ID : {book.book_id}")
                self.log(f"Title   : {book.title}")
                self.log(f"Author  : {book.author}")
                self.log(f"Status  : {book.get_status_str()}")
                found = True
                break

        if not found:
            self.log("Book not found.")

    # 4. Borrow Book
    def borrow_book(self):
        try:
            book_id = int(self.entry_id.get())
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid Book ID to borrow."
            )
            return

        for book in self.books:
            if book.book_id == book_id:
                if book.borrowed:
                    messagebox.showwarning("Warning", "Book is already borrowed.")
                else:
                    book.borrowed = True
                    self.log(
                        f"[Success] Borrow completed for ID: {book.book_id}"
                    )
                    self.clear_inputs()
                return
        messagebox.showerror("Error", "Book not found.")

    # 5. Return Book
    def return_book(self):
        try:
            book_id = int(self.entry_id.get())
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid Book ID to return."
            )
            return

        for book in self.books:
            if book.book_id == book_id:
                if not book.borrowed:
                    messagebox.showwarning(
                        "Warning", "Book is already available."
                    )
                else:
                    book.borrowed = False
                    self.log(f"[Success] Return completed for ID: {book.book_id}")
                    self.clear_inputs()
                return
        messagebox.showerror("Error", "Book not found.")

    # 6. Delete Book
    def delete_book(self):
        try:
            book_id = int(self.entry_id.get())
        except ValueError:
            messagebox.showerror(
                "Error", "Please enter a valid Book ID to delete."
            )
            return

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.log(f"[Success] Book deleted: ID {book_id}")
                self.clear_inputs()
                return
        messagebox.showerror("Error", "Book not found.")

    # 7. Save CSV File
    def save_books(self):
        try:
            with open("books.csv", "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Title", "Author", "Borrowed"])
                for book in self.books:
                    writer.writerow(
                        [book.book_id, book.title, book.author, book.borrowed]
                    )
            messagebox.showinfo("Saved", "Data successfully saved to books.csv")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

    # 8. Load CSV File
    def load_books(self):
        if not os.path.exists("books.csv"):
            return
        try:
            with open("books.csv", "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    if len(row) == 4:
                        self.books.append(
                            Book(
                                int(row[0]), row[1], row[2], row[3] == "True"
                            )
                        )
        except Exception as e:
            print(f"Error loading file: {e}")

    def on_closing(self):
        """프로그램 종료 시 자동 저장"""
        self.save_books()
        self.root.destroy()


# Main Program Execution
if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()