# File Creation
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with a mix of text and numbers: 9876\n")
        print("File created successfully.")
    except PermissionError:
        print("Permission denied to create the file.")
    except Exception as e:
        print("An error occurred:", e)


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            content = file.read()
            print("File content:\n", content)
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)


# File Appending
def append_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("Appending line 1\n")
            file.write("Appending line 2\n")
            file.write("Appending line 3\n")
        print("File appended successfully.")
    except PermissionError:
        print("Permission denied to append to the file.")
    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()
