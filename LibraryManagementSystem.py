# Books: each book is a dictionary with title, author, and category
books = [
    {"title": "Python Programming", "author": "John Doe", "category": "Programming"},
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "category": "Novel"},
    {"title": "Deep Learning", "author": "Ian Goodfellow", "category": "AI"}
]

# Users: each user has a list of borrowed books
users = {}

# Book categories: a set of categories
categories = {"Programming", "Novel", "AI"}

# Function to add a new book to the library
def add_book(title, author, category):
    books.append({"title": title, "author": author, "category": category})
    if category not in categories:
        categories.add(category)
    print(f"The book '{title}' has been added to the library.")

# Function to borrow a book
def borrow_book(username, book_title):
    book_found = None
    # Search for the book in the library
    for book in books:
        if book['title'] == book_title:
            book_found = book
            break
    
    if book_found:
        if username not in users:
            users[username] = []
        users[username].append(book_found)
        books.remove(book_found)
        print(f"{username} has borrowed the book '{book_title}'.")
    else:
        print(f"The book '{book_title}' is not available in the library.")

# Function to return a book
def return_book(username, book_title):
    if username in users:
        for book in users[username]:
            if book['title'] == book_title:
                users[username].remove(book)
                books.append(book)
                print(f"{username} has returned the book '{book_title}'.")
                return
    print(f"The book '{book_title}' was not borrowed by {username}.")

# Function to list books by category
def list_books_by_category(category):
    print(f"Books in the category '{category}':")
    for book in books:
        if book['category'] == category:
            print(f" - {book['title']} by {book['author']}")

# Function to list books borrowed by users
def list_users_books():
    for user, borrowed_books in users.items():
        print(f"{user} has borrowed the following books:")
        for book in borrowed_books:
            print(f" - {book['title']} by {book['author']}")
