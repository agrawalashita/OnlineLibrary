import sqlite3

def create_database():
    # Create Users table in node1
    conn_users = sqlite3.connect('node1_users.db')
    conn_users.execute('''CREATE TABLE IF NOT EXISTS Users (
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT UNIQUE NOT NULL)''')
    conn_users.commit()
    conn_users.close()

    # Create Books table in node2
    conn_books = sqlite3.connect('node2_books.db')
    conn_books.execute('''CREATE TABLE IF NOT EXISTS Books (
                        book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        copies_total INTEGER,
                        copies_available INTEGER)''')
    conn_books.commit()
    conn_books.close()

    # Create Borrows table in node3
    conn_borrows = sqlite3.connect('node3_borrows.db')
    conn_borrows.execute('''CREATE TABLE IF NOT EXISTS Borrows (
                          borrow_id INTEGER PRIMARY KEY AUTOINCREMENT,
                          user_id INTEGER,
                          book_id INTEGER,
                          borrow_date DATE,
                          return_date DATE,
                          FOREIGN KEY (user_id) REFERENCES Users(user_id),
                          FOREIGN KEY (book_id) REFERENCES Books(book_id))''')
    conn_borrows.commit()
    conn_borrows.close()

create_database()
