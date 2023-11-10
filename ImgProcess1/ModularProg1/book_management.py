library = []

def add_book():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    library.append({"title": title, "author": author})
    print(f"{title} by {author} has been added to the library.")

def search_book():
    title = input("Enter the title to search for: ")
    found_books = [book for book in library if book["title"] == title]

    if found_books:
        print("Matching books:")
        for book in found_books:
            print(f"{book['title']} by {book['author']}")
    else:
        print(f"No books with the title '{title}' found.")

def display_books():
    if library:
        print("Library Catalog:")
        for book in library:
            print(f"{book['title']} by {book['author']}")
    else:
        print("The library is empty.")
