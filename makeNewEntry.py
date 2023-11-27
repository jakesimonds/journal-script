import sys
import os
from datetime import datetime
import requests
from dotenv import load_dotenv
import json

from scripts.libraryChecker import query_library
from scripts.weatherChecker import get_weather, get_temp

load_dotenv()


# grabs time, temperature & any available library books as variables
def get_info():
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S\n")

    # will be overwritten when API call executes flawlessly
    temp = "The Weather API Call failed. Consider journalling about any emotions that are coming up."
    weather = get_weather()
    if weather:
        temp = get_temp(weather)

    # book business
    books_available = None
    if os.path.exists("scripts/books.json"):
        with open("scripts/books.json", "r") as file:
            data = json.load(file)
            books = data["books"]
        books_available = query_library(books)

    return date_str, temp, books_available


# writes template & variables from get_info() to your .txt file
def process_template(file_path):
    with open(file_path, "r") as file:
        template = file.readlines()

    date_str, temp, books_available = get_info()

    # write relevant data to file
    with open(file_path, "w") as file:
        file.writelines(f"Current temp: {temp} \n\n")
        file.writelines(f"Time: {date_str}")
        if books_available:
            for book in books_available:
                file.writelines(
                    f"\n *yay* A book you're interested in is available! *yay* \n Book: {book['title'].replace('%20', ' ')}"
                )
        file.writelines(template)


if __name__ == "__main__":
    process_template(sys.argv[1])
