# File Creation
def create_file():
    try:
        with open("my_file.txt", 'w') as file:
            file.write("This is line 1\n")
            file.write("12345\n")
            file.write("Another line with a mix of text and numbers: 9876\n")
        print("File is created.")
    except PermissionError:
        print("File not created.")
    except Exception as makosa:
        print("This an error:", makosa)


# File Reading and Display
def read_file():
    try:
        with open("my_file.txt", 'r') as file:
            Information = file.read()
            print("File content:\n", Information)
    except FileNotFoundError:
        print("File empty.")
    except Exception as makosa:
        print("Caused an Error:", makosa)


# File Appending
def append_file():
    try:
        with open("my_file.txt", 'a') as file:
            file.write("This an append 1\n")
            file.write("This an append 2\n")
            file.write("This an append 3\n")
        print("File appended.")
    except PermissionError:
        print("File cannot be opened")
    except Exception as makosa:
        print("Caused an error:", makosa)


if __name__ == "__main__":
    create_file()
    read_file()
    append_file()
    read_file()
