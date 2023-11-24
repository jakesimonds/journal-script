'''
ChatGPT-assisted functions mainly to add, remove and list books in books.json
new books for testing: https://www.barnesandnoble.com/b/books/_/N-26Z29Z8q8#:~:text=,order%20today
'''


import json
import argparse
import sys
from libraryChecker import query_book

# Function to load books from JSON file
def load_books(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"books": []}

# Function to save books to JSON file
def save_books(filename, books):
    with open(filename, 'w') as file:
        json.dump(books, file, indent=4)

# Function to add a book
def add_book(books, book_title):
    formatted_title = book_title.replace(' ', '%20').lower()
    res = query_book(formatted_title)
    books["books"].append({"title": formatted_title, "res": res})
    print(f"'{book_title}' added to the book list.")

def list_books(books):
    for book in books["books"]:
        formatted_book = book["title"].replace('%20', ' ')
        print("\n", formatted_book)

def remove_book(books, book_title):

    formatted_title = book_title.replace(' ', '%20').lower()
    for book in books["books"]:
        if book["title"] == formatted_title:
            books["books"].remove(book)
            print(f"'{formatted_title}' removed from the book list.")
            return
    print(f"Book '{formatted_title}' not found in the list.")


# Main function

def main():
    parser = argparse.ArgumentParser(description="Manage a book list.")
    parser.add_argument('-add', metavar='BOOK', type=str, help='Add a book to the list')
    parser.add_argument('-list', action='store_true', help='List all books')
    parser.add_argument('-rm', metavar='BOOK', type=str, help='Remove a book from the list')
    args = parser.parse_args()

    filename = 'books.json'
    books = load_books(filename)

    if args.add:
        add_book(books, args.add)
        save_books(filename, books)

    elif args.list:
        print("Current books:")
        list_books(books)
    elif args.rm:
        remove_book(books, args.rm)
        save_books(filename, books)

    else:
        print("need a flag: -add, -list, or -rm")

if __name__ == "__main__":
    main()
