import sqlite3

"""
Concerned with storing and retrieving books from a database.
"""


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)")

    connection.commit()
    connection.close()


def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    try:
        cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    except sqlite3.IntegrityError:
        return False

    connection.commit()
    connection.close()

    return True


def get_all_books():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM books')
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]

    connection.close()

    return books


def mark_book_as_read(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('UPDATE books SET read=1 WHERE name=?', (name,))

    connection.commit()
    connection.close()


def delete_book(name):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    cursor.execute('DELETE FROM books WHERE name=?', (name,))

    connection.commit()
    connection.close()
