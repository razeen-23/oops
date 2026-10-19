class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = True


class Member:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = {}
        self.members = {}

    def add_book(self):
        book_id = input("Enter book ID: ")

        if book_id in self.books:
            print("Book ID already exists.")
            return

        title = input("Enter book title: ")
        author = input("Enter author name: ")

        self.books[book_id] = Book(book_id, title, author)
        print("Book added successfully!")

    def register_member(self):
        member_id = input("Enter member ID: ")

        if member_id in self.members:
            print("Member ID already exists.")
            return

        name = input("Enter member name: ")
        self.members[member_id] = Member(member_id, name)
        print("Member registered successfully!")

    def borrow_book(self):
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")

        if member_id not in self.members:
            print("Member not found.")
            return

        if book_id not in self.books:
            print("Book not found.")
            return

        book = self.books[book_id]
        member = self.members[member_id]

        if not book.available:
            print("Sorry, this book is already borrowed.")
            return

        book.available = False
        member.borrowed_books.append(book_id)
        print(f"'{book.title}' borrowed successfully!")

    def return_book(self):
        member_id = input("Enter member ID: ")
        book_id = input("Enter book ID: ")

        if member_id not in self.members:
            print("Member not found.")
            return

        member = self.members[member_id]

        if book_id not in member.borrowed_books:
            print("This member has not borrowed this book.")
            return

        member.borrowed_books.remove(book_id)
        self.books[book_id].available = True
        print("Book returned successfully!")

    def display_available_books(self):
        print("\n--- Available Books ---")
        available_books = [
            book for book in self.books.values()
            if book.available
        ]

        if not available_books:
            print("No books are currently available.")
            return

        for book in available_books:
            print(
                f"ID: {book.book_id} | "
                f"Title: {book.title} | "
                f"Author: {book.author}"
            )

    def display_all_books(self):
        print("\n--- All Books ---")

        if not self.books:
            print("No books have been added.")
            return

        for book in self.books.values():
            status = "Available" if book.available else "Borrowed"
            print(
                f"ID: {book.book_id} | "
                f"Title: {book.title} | "
                f"Author: {book.author} | "
                f"Status: {status}"
            )


def main():
    library = Library()

    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Member")
        print("3. Borrow Book")
        print("4. Return Book")
        print("5. Display Available Books")
        print("6. Display All Books")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.register_member()
        elif choice == "3":
            library.borrow_book()
        elif choice == "4":
            library.return_book()
        elif choice == "5":
            library.display_available_books()
        elif choice == "6":
            library.display_all_books()
        elif choice == "7":
            print("Thank you for using the Library Management System!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()