import sys
import os
from datetime import datetime
import requests
from dotenv import load_dotenv
import json

from libraryChecker import query_library
from weatherChecker import get_weather, get_temp

load_dotenv()



def process_template(file_path):
    with open(file_path, "r") as file:
        template = file.readlines()

    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S\n")
    
    weather = get_weather()
    if weather:
        temp = get_temp(weather)
    
    #book business
    books_available = None
    if os.path.exists("scripts/books.json"):
        with open("scripts/books.json", 'r') as file:
            data = json.load(file)
            books = data["books"]
        books_available = query_library(books)

    # write relevant data to file
    with open(file_path, "w") as file:
        if weather:
            file.writelines(f"Current temp: {temp} \n\n")
        file.writelines(f"Time: {date_str}")
        if books_available:
            for book in books_available:
                file.writelines(f"\n *yay* A book you're interested in is available! *yay* \n Book: {book['title'].replace('%20', ' ')}")
        file.writelines(template)


if __name__ == "__main__":
    process_template(sys.argv[1])
