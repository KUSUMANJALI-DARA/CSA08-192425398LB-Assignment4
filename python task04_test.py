
import os
import tempfile
from pathlib import Path

# Original defective functions
def save_returns(books):
    log = open("returns.log", "w")
    for b in books:
        log.write(b)
    log.close()


def process(day_file):
    try:
        books = open(day_file).read().split("\n")
        save_returns(books)
    except FileNotFoundError:
        print("missing")


# Test the program for three days
with tempfile.TemporaryDirectory() as temp_dir:
    original_directory = os.getcwd()
    os.chdir(temp_dir)

    try:
        daily_data = {
            "day1.txt": "The Hobbit\nDune",
            "day2.txt": "Hamlet\nMacbeth",
            "day3.txt": "1984\nAnimal Farm"
        }

        for filename, content in daily_data.items():
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)

        process("day1.txt")
        process("day2.txt")
        process("day3.txt")

        print("Final contents of returns.log:")

        with open("returns.log", "r", encoding="utf-8") as file:
            print(file.read())

    finally:
        os.chdir(original_directory)
