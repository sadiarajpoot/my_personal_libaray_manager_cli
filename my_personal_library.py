import json
import os 
# Yeh ek text file ka naam hai, jisme hum apni books store karenge.
data_file= "library.txt"

def load_library ():
    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open(data_file , "r") as file:
            return json.load(file)
    return[]

def save_library (library):
    with open(data_file,"w") as file:
        json.dump(library,file,indent=4)

    # function 1 for add book
def add_book(library):
    title = input("Enter the title of the book: ").strip()
    author = input("Enter the author of the book: ").strip()
    year = input("Enter the year of publication: ").strip()
    genre = input("Enter the genre of the book: ").strip()
    read = input("Have you read the book? (yes/no): ").strip().lower() == "yes"
    
    new_book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read": read
    }

    library.append(new_book)
    save_library(library)
    print(f"Book '{title}' added successfully!")

    # function 2 for remove book
def remove_book(library):
    title = input("Enter the title of the book to remove: ").strip().lower()
    initial_length = len(library)
    updated_library = [book for book in library if book['title'].lower() != title]

    if len(updated_library) < initial_length:
        save_library(updated_library)
        print(f"Book '{title}' removed successfully!")
        return updated_library
    else:
        print(f"Book '{title}' not found in the library.")
        return library

    # function 1 for search book
def search_book(library):
    search_by=input("Search by (Title/Author): ").strip().lower()
    if search_by not  in ["title","author"]:
        print("Invalid option! Please enter 'Title' or 'Author'.")
        return
    search_term = input(f"Enter the {search_by}: ").strip().lower()
    results = [book for book in library if search_term in book[search_by].lower()]

    if results:
        for book in results:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print(f"No book found matching '{search_term}' in {search_by} field.")

    # function 1 for display all book
def display_all_data (library):
    if library:
        for book in library:
            status = "Read" if book['read'] else "Unread"
            print(f"{book['title']} by {book['author']} - {book['year']} - {book['genre']} - {status}")
    else:
        print("The library is empty.")

#    # function 1 for book status
def display_main_status(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book['read'])
    
    print(f"Total Books: {total_books}")
    print(f"Read Books: {read_books}")
    print(f"Unread Books: {total_books - read_books}")

library = load_library()

while True:
    print("\nLibrary Menu:")
    print("1. Add a Book")
    print("2. Remove a Book")
    print("3. Search for a Book")
    print("4. Display All Books")
    print("5. Display Library Status")
    print("6. Exit")
    
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        add_book(library)
    elif choice == "2":
        library = remove_book(library)  
    elif choice == "3":
        search_book(library)
    elif choice == "4":
        display_all_data(library)
    elif choice == "5":
        display_main_status(library)
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")




    

