import requests



def query_book(bookTitle):
    try:
        from bs4 import BeautifulSoup
        url = f"https://portlandlibrary.bibliocommons.com/v2/search?query={bookTitle}&searchType=title"
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        results = soup.find_all('div', class_='cp-search-result-item-info')

        return len(results) if results else 0
    except Exception as e:
        print("Only an issue if you wanna query the library for books: ", e)
        return 0
        


def query_library(books):
    availableBooks = []

    for book in books:
        results = query_book(book["title"])
        if results != book["res"]:
            availableBooks.append(book)
        else:
            print(f" '{book['title']}' not available.")

    return availableBooks if len(availableBooks) > 0 else None

