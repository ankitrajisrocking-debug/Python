import tkinter as tk
from tkinter import ttk, messagebox

from books import (
    add_book,
    issue_book,
    return_book,
    search_books,
    get_all_books
)


class LibraryGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry("850x550")

        # Heading
        tk.Label(
            root,
            text="Library Management System",
            font=("Arial", 20, "bold")
        ).pack(pady=10)

        # Book Entry Frame
        entry_frame = tk.LabelFrame(
            root,
            text="Book Details",
            padx=10,
            pady=10
        )
        entry_frame.pack(fill="x", padx=20)

        tk.Label(entry_frame, text="Title:").grid(row=0, column=0)
        self.title_entry = tk.Entry(entry_frame, width=30)
        self.title_entry.grid(row=0, column=1, padx=10)

        tk.Label(entry_frame, text="Author:").grid(row=0, column=2)
        self.author_entry = tk.Entry(entry_frame, width=30)
        self.author_entry.grid(row=0, column=3, padx=10)

        tk.Button(
            entry_frame,
            text="Add Book",
            command=self.add_book
        ).grid(row=0, column=4, padx=10)

        # Issue / Return Frame
        action_frame = tk.LabelFrame(
            root,
            text="Issue / Return Book",
            padx=10,
            pady=10
        )
        action_frame.pack(fill="x", padx=20, pady=10)

        tk.Label(action_frame, text="Book ID:").grid(row=0, column=0)

        self.book_id_entry = tk.Entry(action_frame, width=10)
        self.book_id_entry.grid(row=0, column=1, padx=10)

        tk.Label(action_frame, text="Student Name:").grid(row=0, column=2)

        self.student_entry = tk.Entry(action_frame, width=25)
        self.student_entry.grid(row=0, column=3, padx=10)

        tk.Button(
            action_frame,
            text="Issue Book",
            command=self.issue_book
        ).grid(row=0, column=4, padx=5)

        tk.Button(
            action_frame,
            text="Return Book",
            command=self.return_book
        ).grid(row=0, column=5, padx=5)

        # Search Frame
        search_frame = tk.Frame(root)
        search_frame.pack(fill="x", padx=20, pady=5)

        tk.Label(search_frame, text="Search:").pack(side="left")

        self.search_entry = tk.Entry(search_frame, width=40)
        self.search_entry.pack(side="left", padx=10)

        tk.Button(
            search_frame,
            text="Search",
            command=self.search
        ).pack(side="left")

        tk.Button(
            search_frame,
            text="Show All",
            command=self.show_all
        ).pack(side="left", padx=5)

        # Table
        columns = (
            "ID",
            "Title",
            "Author",
            "Status",
            "Issued To"
        )

        self.table = ttk.Treeview(
            root,
            columns=columns,
            show="headings"
        )

        for column in columns:
            self.table.heading(column, text=column)

        self.table.column("ID", width=50)
        self.table.column("Title", width=220)
        self.table.column("Author", width=180)
        self.table.column("Status", width=100)
        self.table.column("Issued To", width=150)

        self.table.pack(
            fill="both",
            expand=True,
            padx=20,
            pady=10
        )

        self.show_all()

    def add_book(self):
        title = self.title_entry.get().strip()
        author = self.author_entry.get().strip()

        if not title or not author:
            messagebox.showwarning(
                "Input Error",
                "Please enter book title and author."
            )
            return

        add_book(title, author)

        messagebox.showinfo(
            "Success",
            "Book added successfully."
        )

        self.title_entry.delete(0, tk.END)
        self.author_entry.delete(0, tk.END)

        self.show_all()

    def issue_book(self):
        try:
            book_id = int(self.book_id_entry.get())
        except ValueError:
            messagebox.showwarning(
                "Input Error",
                "Enter a valid Book ID."
            )
            return

        student = self.student_entry.get().strip()

        if not student:
            messagebox.showwarning(
                "Input Error",
                "Enter student name."
            )
            return

        if issue_book(book_id, student):
            messagebox.showinfo(
                "Success",
                "Book issued successfully."
            )
            self.show_all()
        else:
            messagebox.showerror(
                "Error",
                "Book not found or already issued."
            )

    def return_book(self):
        try:
            book_id = int(self.book_id_entry.get())
        except ValueError:
            messagebox.showwarning(
                "Input Error",
                "Enter a valid Book ID."
            )
            return

        if return_book(book_id):
            messagebox.showinfo(
                "Success",
                "Book returned successfully."
            )
            self.show_all()
        else:
            messagebox.showerror(
                "Error",
                "Book not found or not currently issued."
            )

    def search(self):
        keyword = self.search_entry.get().strip()

        records = search_books(keyword)
        self.display_records(records)

    def show_all(self):
        records = get_all_books()
        self.display_records(records)

    def display_records(self, records):
        for item in self.table.get_children():
            self.table.delete(item)

        for record in records:
            self.table.insert("", tk.END, values=record)

