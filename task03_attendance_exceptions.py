
import os
import tempfile


class InvalidRecord(Exception):
    """Raised when an attendance record is invalid."""


def parse_line(line):
    """Convert a valid attendance line into a tuple."""

    parts = [item.strip() for item in line.strip().split(",")]

    if len(parts) != 3:
        raise InvalidRecord(
            f"expected 3 fields, found {len(parts)}"
        )

    register_number, date, status = parts

    if status not in ("P", "A"):
        raise InvalidRecord(f"invalid status '{status}'")

    return register_number, date, status


def summarise(path):
    present = 0
    absent = 0
    errors = []

    try:
        with open(path, "r", encoding="utf-8") as file:

            for line_number, line in enumerate(file, start=1):

                if not line.strip():
                    continue

                try:
                    register_number, date, status = parse_line(line)

                except InvalidRecord as error:
                    errors.append((line_number, str(error)))

                else:
                    if status == "P":
                        present += 1
                    else:
                        absent += 1

    except FileNotFoundError as error:
        print("File not found:", path)
        return present, absent, errors

    except PermissionError as error:
        print("Permission denied:", error)
        return present, absent, errors

    except UnicodeDecodeError as error:
        print("Encoding error:", error)
        return present, absent, errors

    except OSError as error:
        print("File processing error:", error)
        return present, absent, errors

    else:
        print("Attendance file processed successfully.")

    finally:
        print("Processing attempt finished.")

    return present, absent, errors


data = (
    "192311001,2026-10-08,P\n"
    "192311002,2026-10-08,A\n"
    "192311003,2026-10-08\n"
    "192311004,2026-10-08,L\n"
)

with tempfile.NamedTemporaryFile(
    "w",
    suffix=".csv",
    delete=False,
    encoding="utf-8"
) as tmp:
    tmp.write(data)
    file_path = tmp.name

print(summarise(file_path))

os.remove(file_path)

# Test a file that does not exist
print("\nTesting a missing file:")
print(summarise("missing_attendance.csv"))
