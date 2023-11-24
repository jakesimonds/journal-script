# process_template.py
import sys
from datetime import datetime
import requests
import os
from dotenv import load_dotenv
import json

from libraryChecker import query_library
from weatherChecker import get_temp
load_dotenv()



def process_template(file_path):
    # get the template
    with open(file_path, "r") as file:
        content = file.readlines()

    # get the date
    date = datetime.now()
    date_str = date.strftime("%Y-%m-%d %H:%M:%S\n")
    
    # get the temperature
    temp = get_temp()
    
    # get any available books
    with open("scripts/books.json", 'r') as file:
        data = json.load(file)
        books = data["books"]
    books_available = query_library(books)

    
    # write relevant data to file
    with open(file_path, "w") as file:
        file.writelines(f"Current temp: {temp} \n\n")
        file.writelines(f"Time: {date_str}")
        if books_available:
            file.writelines(f"\n *yay* A book you're interested in is available! *yay* \n {books_available}")
        file.writelines(content)


if __name__ == "__main__":
    process_template(sys.argv[1])
