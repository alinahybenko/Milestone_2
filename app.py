from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    database.create_book_table()
    user_input = input(USER_CHOICE).strip().lower()
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_books()
        elif user_input == 'r':
            prompt_read_book()
        elif user_input == 'd':
            prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        user_input = input(USER_CHOICE).strip().lower()


def prompt_add_book():
    name = input("Book title: ").strip().title()
    author = input("Author: ").strip().title()

    if database.add_book(name, author):
        print()
    else:
        print("You've already got that book in your database.")


def list_books():
    books = database.get_all_books()
    if len(books) > 0:
        for book in books:
            read = 'YES' if book['read'] else 'NO'
            print(f"'{book['name']}' by {book['author']}, read: {read}")
    else:
        print("Your book list is empty.")


def prompt_read_book():
    name = input("Enter a name of the book you've just finished reading: ").strip().title()

    database.mark_book_as_read(name)


def prompt_delete_book():
    name = input("Enter a book name you want to remove from your list: ").strip().title()

    database.delete_book(name)


menu()
