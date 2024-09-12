try: 
    # File Creation
    with open("my_file.txt", "w") as file:
        file.write("Hello, World!\n")
        file.write("This is a test file.\n")
        file.write("The answer is 42.\n")

    # File Reading and Display
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File Contents:")
        print(content)

    # File Appending
    with open("my_file.txt", "a") as file:
        file.write("This is an appended line.\n")
        file.write("Another appended line.\n")
        file.write("The final appended line.\n")

except FileNotFoundError:
    print("The file was not found.")
except PermissionError:
    print("You do not have permission to access the file.")
except Exception as e:
    print("An error occurred: ", str(e))

finally:
    print("File handling operations are complete.")