import book_management

def main():
    print("Welcome to the Library Management System")

    while True:
        print("\nOptions:")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Display All Books")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            book_management.add_book()
        elif choice == "2":
            book_management.search_book()
        elif choice == "3":
            book_management.display_books()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
