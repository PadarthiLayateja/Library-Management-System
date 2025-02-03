class Book:
    def __init__(self, id, title, author):
        self.id = id
        self.title = title
        self.author = author
        self.is_issued = False

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, id, title, author):
        self.books.append(Book(id, title, author))
        print("Book added successfully.")

    def search_book_by_id(self, id):
        for book in self.books:
            if book.id == id:
                print(f"Book found\nID: {book.id}\nTitle: {book.title}\nAuthor: {book.author}\nStatus: {'Issued' if book.is_issued else 'Available'}")
                return
        print("Book not found.")

    def search_book_by_title(self, title):
        for book in self.books:
            if book.title == title:
                print(f"Book found\nID: {book.id}\nTitle: {book.title}\nAuthor: {book.author}\nStatus: {'Issued' if book.is_issued else 'Available'}")
                return
        print("Book not found.")

    def issue_book(self, id):
        for book in self.books:
            if book.id == id:
                if not book.is_issued:
                    book.is_issued = True
                    print("Book issued successfully.")
                else:
                    print("Book is already issued.")
                return
        print("Book not found.")

    def return_book(self, id):
        for book in self.books:
            if book.id == id:
                if book.is_issued:
                    book.is_issued = False
                    print("Book returned successfully.")
                else:
                    print("Book was not issued.")
                return
        print("Book not found.")

    def list_all_books(self):
        self.books.sort(key=lambda x: x.id)
        for book in self.books:
            print(f"ID: {book.id}\nTitle: {book.title}\nAuthor: {book.author}\nStatus: {'Issued' if book.is_issued else 'Available'}")

    def delete_book(self, id):
        for i, book in enumerate(self.books):
            if book.id == id:
                del self.books[i]
                print("Book deleted successfully.")
                return
        print("Book not found.")

def main():
    library = Library()
    while True:
        print("Library Management System")
        print("1. Add New Book\n2. Search Book by ID\n3. Search Book by Title\n4. Issue Book\n5. Return Book\n6. List All Books\n7. Delete Book\n8. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            id = int(input("Enter Book ID: "))
            title = input("Enter Book Title: ")
            author = input("Enter Book Author: ")
            library.add_book(id, title, author)
        elif choice == 2:
            id = int(input("Enter Book ID: "))
            library.search_book_by_id(id)
        elif choice == 3:
            title = input("Enter Book Title: ")
            library.search_book_by_title(title)
        elif choice == 4:
            id = int(input("Enter Book ID to issue: "))
            library.issue_book(id)
        elif choice == 5:
            id = int(input("Enter Book ID to return: "))
            library.return_book(id)
        elif choice == 6:
            library.list_all_books()
        elif choice == 7:
            id = int(input("Enter Book ID to delete: "))
            library.delete_book(id)
        elif choice == 8:
            print("Thanks for using the library management system")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()