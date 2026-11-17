
def save_returns(books):
    try:
        with open("returns.log", "a", encoding="utf-8") as log:
            for book in books:
                if book.strip():
                    log.write(book.strip() + "\n")

    except OSError as error:
        with open("error.log", "a", encoding="utf-8") as error_log:
            error_log.write(f"Error saving returns: {error}\n")


def process(day_file):
    try:
        with open(day_file, "r", encoding="utf-8") as file:
            books = file.read().splitlines()

        save_returns(books)

    except FileNotFoundError:
        print("Missing file:", day_file)

    except PermissionError:
        print("Permission denied:", day_file)

    except OSError as error:
        print("File processing error:", error)


if __name__ == "__main__":
    process("day1.txt")
    process("day2.txt")
    process("day3.txt")

    print("Library return processing completed.")
