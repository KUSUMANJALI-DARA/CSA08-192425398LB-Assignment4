
from decimal import Decimal, InvalidOperation


def process_mess_file(file_name):
    total = Decimal("0.00")
    report_lines = []
    rejected_lines = []

    try:
        with open(file_name, "r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):

                if not line.strip():
                    continue

                try:
                    parts = line.strip().split(",")

                    if len(parts) != 3:
                        raise ValueError("Expected exactly 3 fields")

                    register_number = parts[0].strip()
                    name = parts[1].strip()
                    amount_text = parts[2].strip()

                    if not register_number or not name:
                        raise ValueError("Register number or name is missing")

                    amount = Decimal(amount_text)

                    if not amount.is_finite():
                        raise ValueError("Amount must be a finite number")

                    total += amount
                    report_lines.append(
                        f"{name} {amount:.2f}"
                    )

                except (ValueError, InvalidOperation) as error:
                    rejected_lines.append(
                        (line_number, line.rstrip("\n"), str(error))
                    )

        print("HOSTEL MESS BILL REPORT")
        print("----------------------")

        print("\nValid Records:")
        print("\n".join(report_lines))

        print("\nTotal Mess Bill: Rs.", f"{total:.2f}")

        print("\nRejected Records:")
        if rejected_lines:
            for number, rejected, reason in rejected_lines:
                print(
                    f"Line {number}: {rejected} | Reason: {reason}"
                )
        else:
            print("No rejected records.")

    except FileNotFoundError:
        print("Error: The specified file was not found.")

    except PermissionError:
        print("Error: Permission denied while accessing the file.")

    except UnicodeDecodeError:
        print("Error: The file contains invalid text encoding.")

    except OSError as error:
        print("File system error:", error)


if __name__ == "__main__":
    process_mess_file("mess_oct.txt")
