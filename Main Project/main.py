from library import Library

def divider(title=""):
    print("\n" + "=" * 50)
    if title:
        print(f"🔷 {title}")
        print("=" * 50)

def main():
    library = Library()
    print("\n📚 Welcome to the 🌟 Community Library System 🌟")

    while True:
        divider("Main Menu")
        print("👤 Select your role:")
        print("1️⃣ Member")
        print("2️⃣ Librarian")
        print("3️⃣ Exit")
        choice = input("👉 Enter your choice (1/2/3): ")

        if choice == "1":
            member_name = input("🪪 Enter your name: ")
            while True:
                divider("Member Menu")
                print("📖 What would you like to do?")
                print("1️⃣ View available books")
                print("2️⃣ Borrow a book")
                print("3️⃣ Return a book")
                print("4️⃣ Back to main menu")
                action = input("👉 Your choice: ")

                if action == "1":
                    divider("Available Books")
                    library.view_available_books()
                elif action == "2":
                    title = input("📚 Enter book title to borrow: ")
                    library.borrow_book(member_name, title)
                elif action == "3":
                    title = input("📕 Enter book title to return: ")
                    library.return_book(member_name, title)
                elif action == "4":
                    break
                else:
                    print("❌ Invalid choice. Please try again.")

        elif choice == "2":
            while True:
                divider("Librarian Menu")
                print("🔧 Librarian Options:")
                print("1️⃣ Add book (fetches from Google Books API)")
                print("2️⃣ Remove book")
                print("3️⃣ View borrowed books")
                print("4️⃣ View most popular books")
                print("5️⃣ Back to main menu")
                action = input("👉 Your choice: ")

                if action == "1":
                    title = input("➕ Enter book title to add: ")
                    library.add_book(title)
                elif action == "2":
                    title = input("➖ Enter book title to remove: ")
                    library.remove_book(title)
                elif action == "3":
                    divider("Borrowed Books")
                    library.view_borrowed_books()
                elif action == "4":
                    divider("Most Popular Books")
                    library.view_most_popular_books()
                elif action == "5":
                    break
                else:
                    print("❌ Invalid choice. Please try again.")

        elif choice == "3":
            print("\n👋 Thank you for using the Community Library System. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
