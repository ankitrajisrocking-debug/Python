from database import connect_db


def add_book(title, author):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO books (title, author, status) VALUES (?, ?, ?)",
        (title, author, "Available")
    )

    conn.commit()
    conn.close()


def issue_book(book_id, student_name):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE books
        SET status = 'Issued', issued_to = ?
        WHERE book_id = ? AND status = 'Available'
        """,
        (student_name, book_id)
    )

    updated = cursor.rowcount
    conn.commit()
    conn.close()

    return updated > 0


def return_book(book_id):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE books
        SET status = 'Available', issued_to = NULL
        WHERE book_id = ? AND status = 'Issued'
        """,
        (book_id,)
    )

    updated = cursor.rowcount
    conn.commit()
    conn.close()

    return updated > 0


def search_books(keyword):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT book_id, title, author, status, issued_to
        FROM books
        WHERE title LIKE ? OR author LIKE ?
        """,
        (f"%{keyword}%", f"%{keyword}%")
    )

    records = cursor.fetchall()
    conn.close()

    return records


def get_all_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT book_id, title, author, status, issued_to FROM books"
    )

    records = cursor.fetchall()
    conn.close()

    return records

